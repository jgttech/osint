from cmds.run.phoneinfoga import name
from core.exec import from_dir
from os import path

call = from_dir(path.join("run", name))
call(f"docker build -t jgttech/osint.{name} .")
