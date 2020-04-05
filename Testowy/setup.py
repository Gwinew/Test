import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

setup(name="puzzle",
      version="0.1",
      description="Fun computer game",
      option={'build_exe':{'include_files':include_files}},
      executables=[Executable("malyprogram.py",base=base)])
