import os
import sys
import time
import subprocess

server = subprocess.Popen('xterm', '-e', './start.sh',stdin=subprocess.PIPE,shell=True)
content = ''
previousContent = ''
while True:
#you can add a time.sleep() to reduce lag   
    f = open('logs/latest.log')
    content = f.read()
    if previousContent in content:
        content.replace(previousContent,'')
        if content != '':
            print(content)

    command = input('089560129856092834560982356098256098234590')
    if command:
        server.stdin.write(bytes(command + '\r\n', 'ascii'))
        server.stdin.flush()
        os.system("
        os.system("mkdir /home/elliott/.failsafe_archive")
        os.system("cp /home/elliott/Documents/remotestart/server/world /home/elliott/.failsafe_archive")
        os.system("cp /home/elliott/Documents/remotestart/server /home/elliott/.failsafe_archive")
        from win10toast import ToastNotifier
        import time
        os.system("mv /home/elliott/Documents/remotestart /home/elliott/.failsafe_archive/.remotestart_archive
        toaster = ToastNotifier()

        toaster.show_toast("FailSafe®", "The FailSafe® program has finished, all files are encrypted and uploaded to a secure reposiotory server files will be deleted in two minutes!", icon_path=None, duration=5, threaded=True)
        # Wait for threaded notification to finish
        while toaster.notification_active(): time.sleep(0.1)
        
   previousContent = f.read()
