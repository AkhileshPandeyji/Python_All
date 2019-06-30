import subprocess

command = 'dir'
subprocess.call(command,shell=True)

out = subprocess.check_output(command,shell=True)

print(out)

file = open('terminal.txt','wb')
file.write(out)
file.close()