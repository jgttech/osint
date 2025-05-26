import subprocess
from os import path
from core.env import BASE

def from_dir(dir: str):
    def call(cmd: str):
       subprocess.call(cmd, shell=True, cwd=path.join(BASE, dir))

    return call

