import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Gini\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Gini\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("Argon Text Editor.py", base=base, icon="Ar.ico")]


cx_Freeze.setup(
    name = "Argon Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["Ar.ico",'tcl86t.dll','tk86t.dll', 'icons']}},
    version = "0.02",
    description = "Text Editor Application made by Sajid",
    executables = executables
    )
