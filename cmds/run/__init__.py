from .group import *
from .phoneinfoga import command as phoneinfoga
from .recon_ng import command as recon_ng
from .theharvester import command as theharvester

run.add_command(phoneinfoga)
run.add_command(recon_ng)
run.add_command(theharvester)
