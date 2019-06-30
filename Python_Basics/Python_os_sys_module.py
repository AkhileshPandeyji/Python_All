import os
import sys

######################  OS #########################
#how to get current working directory
#cwd = os.getcwd()
#print(str(cwd))

#how to make a directory in CWD
#os.mkdir(os,"PythonBasics")

#how to rename a directory in CWD
#os.rename("PythonBasics","PythonAdvanced")

#how to remove directories in CWD
#os.rmdir("PythonBasics")
#os.rmdir("PythonAdvanced")

#how to make a directory anywhere
#os.mkdir("C:/Users/Akhilesh Kr. Pandey/Desktop/PythonBasics")

#how to rename a directory anywhere
#os.rename("C:/Users/Akhilesh Kr. Pandey/Desktop/PythonBasics","C:/Users/Akhilesh Kr. Pandey/Desktop/PythonAdvanced")

#how to remove directories anywhere
#os.rmdir("C:/Users/Akhilesh Kr. Pandey/Desktop/PythonAdvanced")

################################  SYS ###########################

def main(args):
    print(args)

#sys.stderr.write("Output in RED? ")
#sys.stderr.flush()

#sys.stdout.write("Output in BLACK?")
#sys.stdout.flush()

#command line arguments
arg = sys.argv[2]
main(arg)

