import win32gui
import win32con

import  rarfile

rar = rarfile.RarFile('G:\\333.zip')
rar.extractall('G:\\heihei')

