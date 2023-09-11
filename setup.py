from cx_Freeze import setup, Executable

setup(name='BIOscope',
      version='1.0',
      description='微生物扫描系统',
      executables=[Executable('main.py')])
