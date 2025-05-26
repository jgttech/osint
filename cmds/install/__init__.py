from os import getcwd, path
from pathlib import Path
from cmds.group import cli
from core.env import BASE
from core.sys import load_module

@cli.command("install")
def command():
    cwd = path.join(getcwd(), BASE)
    files = list(Path(cwd).rglob("__install__.py"))

    for file in files:
        mod_name = f"{BASE}.{file.parent.name}"
        mod_path = str(file.absolute())

        load_module(mod_name, mod_path)
