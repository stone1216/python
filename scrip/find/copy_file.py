import os
import shutil
def Process(src,dst):
    try:
        shutil.copy(src,dst)
    except:
        print("拷贝失败")
def CreateDir(dst):
    if os.path.exists(dst):
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        elif os.path.isfile(dst):
            os.remove(dst)
    os.mkdir(dst)


def WalkDir(dir,target,dst):
    count = 0
    names = target.split()
    for folderName, subfolders, filenames in os.walk(dir):
        for filename in filenames:
            if(filename in names):
                print("find " +folderName+"\\" +  filename + " Ok")
                count += 1
                Process(folderName +  "\\" + filename, dst)
    print("复制文件个数：%d" % count )


if __name__ == "__main__":

    file_object = open("input.txt")
    lines = []
    try:
        lines = file_object.readlines()
    except:
        print("打开文件失败！！！")
        file_object.close()
    dir = lines[0].replace('\n', '')
    target = lines[1].replace('\n', '')
    dst = lines[2].replace('\n', '')
    try:
        CreateDir(dst)
        WalkDir(dir,target,dst)
        print("find result OK!!!")
    except:
        print("find error!!!")
    input("")
#out00-EXE.toc  clear_code.exe