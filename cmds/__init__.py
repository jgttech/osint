from .group import *
from .run import *
from .install import command as install
from .version import command as version

cli.add_command(run)
cli.add_command(install)
cli.add_command(version)
