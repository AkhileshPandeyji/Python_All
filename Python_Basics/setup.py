import os
from cx_Freeze import setup,Executable

# os.environ['TCL_LIBRARY'] =

setup(name="Paint",author='Akhilesh Pandey',version="0.0.1",description='Paints and draws',executables=[Executable('Python_Paint.py')])

# Traceback (most recent call last):
#   File "setup.py", line 4, in <module>
#     setup(name="Paint",author='Akhilesh Pandey',version="0.0.1",description='Paints and draws',executables=[Executable('Python_Paint.py')])
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\dist.py", line 349, in setup
#     distutils.core.setup(**attrs)
#   File "C:\Users\Akhilesh Kr. Pandey\AppData\Local\Programs\Python\Python37-32\lib\distutils\core.py", line 148, in setup
#     dist.run_commands()
#   File "C:\Users\Akhilesh Kr. Pandey\AppData\Local\Programs\Python\Python37-32\lib\distutils\dist.py", line 966, in run_commands
#     self.run_command(cmd)
#   File "C:\Users\Akhilesh Kr. Pandey\AppData\Local\Programs\Python\Python37-32\lib\distutils\dist.py", line 985, in run_command
#     cmd_obj.run()
#   File "C:\Users\Akhilesh Kr. Pandey\AppData\Local\Programs\Python\Python37-32\lib\distutils\command\build.py", line 135, in run
#     self.run_command(cmd_name)
#   File "C:\Users\Akhilesh Kr. Pandey\AppData\Local\Programs\Python\Python37-32\lib\distutils\cmd.py", line 313, in run_command
#     self.distribution.run_command(command)
#   File "C:\Users\Akhilesh Kr. Pandey\AppData\Local\Programs\Python\Python37-32\lib\distutils\dist.py", line 985, in run_command
#     cmd_obj.run()
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\dist.py", line 219, in run
#     freezer.Freeze()
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\freezer.py", line 626, in Freeze
#     self._FreezeExecutable(executable)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\freezer.py", line 206, in _FreezeExecutable
#     finder.IncludeFile(exe.script, exe.moduleName)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 637, in IncludeFile
#     deferredImports)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 475, in _LoadModule
#     self._ScanCode(module.code, module, deferredImports)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 565, in _ScanCode
#     module, relativeImportIndex)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 311, in _ImportModule
#     deferredImports, namespace = namespace)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 404, in _InternalImportModule
#     parentModule, namespace)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 417, in _LoadModule
#     namespace)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 486, in _LoadPackage
#     self._LoadModule(name, fp, path, info, deferredImports, parent)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 464, in _LoadModule
#     self._RunHook("load", module.name, module)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\finder.py", line 537, in _RunHook
#     method(self, *args)
#   File "C:\Users\Akhilesh Kr. Pandey\PycharmProjects\Python_Basics\venv\lib\site-packages\cx_Freeze\hooks.py", line 615, in load_tkinter
#     tclSourceDir = os.environ["TCL_LIBRARY"]
#   File "C:\Users\Akhilesh Kr. Pandey\AppData\Local\Programs\Python\Python37-32\lib\os.py", line 678, in __getitem__
#     raise KeyError(key) from None
# KeyError: 'TCL_LIBRARY'
