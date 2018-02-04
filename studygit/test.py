import os
import sys
import subprocess

#Obj=os.getcwd()
listpath = sys.argv[1:]
Obj= ' '.join(listpath)
print(Obj)
Obj = Obj[1]+':'+Obj[2:]
Obj = "\\\\".join(Obj.split("\\"))
print(Obj)
if os.path.exists(Obj):  #文件or 目录存在
    if os.path.isfile(Obj):
        import win32process
        try:   # 打开外部可执行程序
            win32process.CreateProcess(Obj, '',None , None , 0 ,win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())
        except Exception as e:
            print(e)
    else:
        os.startfile(str(Obj))  # 打开目录

else:  # 不存在的目录
    print('不存在的目录')