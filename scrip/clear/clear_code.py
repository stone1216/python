
import paramiko

##OSN8800R12C10Private_Code

dir = "/usr1/pom"

def ExeCmd(ssh,cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.readlines()


def ClearCode(ip,user,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, 22, user, password,timeout= 5 )
    except:
        print("connect error!!!")

    ExeCmd(ssh,"rm -rf %s/OSN8800R12C10Private_Code" % dir)
    r = ExeCmd(ssh,"ls %s" % dir)
    if "OSN8800R12C10Private_Code" not in "".join(r):
        print("Clear ok!!!")
    else:
        print("Clear error!!!")
    ssh.close()

if  __name__=="__main__":
    ip = input("请输入要清理pom机ip：")
    user = "root"
    password = "mima2013"
    ClearCode(ip,user,password)
    input("")

