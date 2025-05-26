from importlib.machinery import ModuleSpec
from importlib.util import spec_from_file_location, module_from_spec
from types import ModuleType
import sys

type DynamicModule = tuple[ModuleSpec | None, ModuleType | None];

def load_module(module_name: str, module_path: str) -> DynamicModule:
    module_spec = spec_from_file_location(module_name, module_path)
    module_type = None

    if module_spec != None:
        module_type = module_from_spec(module_spec)

        sys.modules[module_name] = module_type

        if module_spec.loader != None:
            module_spec.loader.exec_module(module_type)

    return (module_spec, module_type)
