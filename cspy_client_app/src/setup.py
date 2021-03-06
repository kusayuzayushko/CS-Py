import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

files = ['static/', 'templates/', 'gamestate_integration_main.cfg', 'run.py', '__init__.py', 'README.txt',
         'VCRUNTIME140.dll']

cspy_exe = Executable(script="main.py", base=base, targetName="CS-Py.exe")

setup(name="CS-Py",
      version="1.2",
      author="Parkkeo1",
      description="v1.2",
      options={
          'build_exe': {
              'packages': ['jinja2.ext', 'jinja2', 'asyncio', 'numpy', 'pandas', 'sqlite3'],
              'excludes': ['Tkinter', 'PyQt4', 'gtk', 'PyQt5', 'wx'],
              'include_files': files,
              'include_msvcr': True,
          }},
      executables=[cspy_exe], requires=['flask']
      )
