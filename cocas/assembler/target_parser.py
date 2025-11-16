"""
--target argument parser for CdM architectures.
Example:
  cdm16e   -> base = "cdm16", extensions = ["e"]
  cdm16em  -> base = "cdm16", extensions = ["e", "m"]
  cdm8     -> base = "cdm8", extensions = []
"""

from typing import Tuple, List

def parse_target(target: str) -> Tuple[str, List[str]]:
    """
    Parse the --target argument and return:
        (base_target, list_of_extensions)
    """
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
    return base, extensions
