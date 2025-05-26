from cmds.run.recon_ng import name
from core.exec import from_dir
from os import path

call = from_dir(path.join("run", "recon_ng"))
call(f"docker build -t jgttech/osint.{name} .")
