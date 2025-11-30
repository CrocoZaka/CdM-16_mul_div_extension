from dataclasses import dataclass

@dataclass
class TargetInfo:
    base: str
    extensions: list[str]

# --target argument parser for CdM architectures.
# Example:
#   cdm16   -> TargetInfo(base = "cdm16", extensions = [])
#   cdm16em  -> TargetInfo(base = "cdm16", extensions = ["e", "m"])
#   cdm8     -> TargetInfo(base = "cdm8", extensions = [])
# ! cdm8e    -> TargetInfo(base = "cdm8e", extensions = [])

def parse_target(target: str) -> TargetInfo:
    target = target.replace("-", "").lower()

    if not target.startswith("cdm"):
        target = "cdm" + target

    if target.startswith("cdm16"):
        base = "cdm16"
        suffix = target[len(base):]
    elif target == "cdm8":
        base = "cdm8"
        suffix = ""
    elif target == "cdm8e":
        base = "cdm8e"
        suffix = ""
    else:
        base = target
        suffix = ""

    extensions = list(suffix)
    return TargetInfo(base=base, extensions=extensions)

