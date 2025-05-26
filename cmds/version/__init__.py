from cmds import cli
from core import exec
from cmds.run.phoneinfoga import cmd as cmd_phoneinfoga, name as name_phoneinfoga
from cmds.run.recon_ng import cmd as cmd_recon_ng, name as name_recon_ng
from cmds.run.theharvester import cmd as cmd_theharvester, name as name_theharvester

@cli.command("version")
def command():
    print(f"[{name_phoneinfoga}]")
    exec.call(f"{cmd_phoneinfoga} version")
    print("")

    print(f"[{name_recon_ng}]")
    exec.call(f"{cmd_recon_ng} --version")
    print("")

    print(f"[{name_theharvester}]")
    exec.call(f"{cmd_theharvester}")
