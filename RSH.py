import sys,os,socket,subprocess

def Connections():
    global Host
    global port
    global sock
    #this creates a TCP socket for connections
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#This gets the hosts address for connections or your devices ip
    Host = socket.gethostbyname(socket.gethostname())
    port  = 1337
#binds port and host to setup a connection
    sock.bind((Host,port))

def accept_con():
    global clientaddr
    global clientsock
#listens for an incoming connection
    listener = sock.listen(1)
    print("listening for connections..")
#accepts connection from client
    clientsock,clientaddr = sock.accept()
    print("{} has connected".format(clientaddr[0]))
#client socket is the clients socket connection which controls its data flow
#client addr is the clients ip address which tells us the devices name that has connected

#all commands and processes that can be performed on the host or sent to/performed on the client
help_menu = ["[command] -send or -s: to send something to the client",
             " -ping: to ping the client",
             "-exit or exit to kill connection"]


#stop words that cant be included in a command call
stop_words = ["send","-send","-s"]
def getridofwords(command,lib):
    ls = command.split(" ")
    for word in ls:
        if word in lib:
            ls.remove(word)
        else:
            pass
    cmd = " ".join(ls)
    return cmd


#gets client info sent from the client after a command or info grab
def  client_info(s):
    data =str(s.recv(1024),"utf-8")
    return data

def commands(command):
    #displays all help menu commands
    if "help" in command or "-h" in command or "?" in command:
        for item in help_menu:
            print(item)

    #pings the client to see latency and to get info
    if "-ping" in command and "-send" not in command:
        os.system("ping {}".format(clientaddr[0]))
    elif "ping" in command  and "-send"not in command:
        os.system("ping {}".format(clientaddr[0]))
    elif "ping" in command and "send" not in command:
        os.system("ping {}".format(clientaddr[0]))
    elif "-ping" in command and "send" not in command:
         os.system("ping {}".format(clientaddr[0]))

    #sends commands and os calls to client
    if "-send" in command:
        command = getridofwords(command,stop_words)
        os.sytem("cls")
        #data sent has to be encoded and then decoded when received
        clientsock.send(command.encode("utf-8"))
        print(client_info(clientsock))
    elif "send" in command:
        command = getridofwords(command,stop_words)
        os.system("cls")
        #data sent has to be encoded and then decoded when received
        clientsock.send(command.encode("utf-8"))
        print(client_info(vlientsock))
    elif "-s" in command:
        command = getridofwords(command,stop_words)
        os.system("cls")
    #data sent has to be encoded and then decoded when received
        clientsock.send(command.encode("utf-8"))
        print(client_info(clientsock))

    if "exit" in command or "-exit" in command:
        clientsock.close()
        sys.exit()

    
def accept():
    passwd = "Kr4nk"
    Con = clientsock.recv(1024).decode("utf-8")
    Con = Con[0]+Con[4]+Con[12]+Con[19]+Con[20]
    if Con == passwd:
        return "accept"
    else:
        return "deny"
def Main():
    ip = socket.gethostbyname(socket.gethostname())
    print("Host {} is running".format(ip))

    Connections()
    accept_con()
    if accept() == "accept":
        #runs shell until conn breaks
        while True:
            command = input(">>")
            if "cls" in command or "clear" in command and "-send" not in command:
                try:
                    os.system("cls")
                except:
                    os.system("clear")
            elif "cls" in command or "clear" in command and "send" not in command:
                try:
                    os.system("cls")
                except:
                    os.system("clear")
            elif "cls" in command or "clear" in command and "-s" not in command:
                try:
                    os.system("cls")
                except:
                    os.system("clear")
            else:
                try:
                    commands(command)
                except socket.error:
                    print("client has disconnected")
                    accept_con()
    else:
        sock.close()
Main()
