import importlib
from pathlib import Path

from assembler.target_parser import TargetInfo

from .abstract_code_segments import IAlignedSegment, IAlignmentPaddingSegment, ICodeSegment, IVaryingLengthSegment
from .target_instructions_protocol import TargetInstructions


def list_assembler_targets() -> set[str]:
    """Returns a set of supported assembler targets. Takes submodules of assembler/target module"""
    targets_dir = Path(__file__).parent.absolute()
    targets = map(lambda x: x.name, filter(lambda x: x.is_dir(), targets_dir.glob("[!_]*")))
    return set(targets)

def load_extensions(ext_list):
    all_handlers = []
    for ext in ext_list:
        mod = importlib.import_module(f".{ext}.target_instructions",
                            package="cocas.assembler.targets.cdm16.extensions")
        all_handlers.extend(mod.handlers)
    return all_handlers

def import_target(target: TargetInfo) -> TargetInstructions:
    module = importlib.import_module(f'.{target.base}', __package__)
    base_handlers = module.handlers
    if target.base == "cdm16" and target.extensions:
        ext_handlers = load_extensions(target.extensions)
        merged_map: dict[object, dict[str, int]] = {}
        for h in base_handlers:
            merged_map.setdefault(h.handler, {}).update(h.instructions)
        for h in ext_handlers:
            merged_map.setdefault(h.handler, {}).update(h.instructions)
        from cocas.assembler.targets.cdm16.target_instructions import Handler
        merged_handlers = [Handler(handler_callable, instr_dict)
                        for handler_callable, instr_dict in merged_map.items()]
        module.handlers = merged_handlers
    if isinstance(module, TargetInstructions):
        return module
    else:
        raise TypeError("Module is not a valid target")


def standard_mlb(target: str) -> Path:
    return Path(__file__).parent / target / "standard.mlb"
