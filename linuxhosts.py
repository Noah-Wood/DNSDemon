import os
import subprocess

def linux():
    path = os.path.join(os.path.expanduser('~'), 'Downloads', 'HostScript', 'IPaddresses')
    command = ["sudo", "--", "sh", "-c", "cat " + path + " >> /etc/hosts"]
    output,error  = subprocess.Popen(
        command, universal_newlines=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print ("Done!")
