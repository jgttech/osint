from click import Context
from core import exec, osint, sys
from cmds.run.group import run

name = "recon-ng"
cmd = f"docker run --rm jgttech/osint.{name}"

@osint.command(run, name)
def command(_: Context):
    argv = " ".join(sys.argv)
    exec.call(f"{cmd} {argv}")
