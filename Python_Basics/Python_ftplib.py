from ftplib import FTP

ftp = FTP('www.pythonprogramming.net')

ftp.login(user='Mark Zukerburg',passwd='password')
ftp.cwd('Mark/cgi-bin/html')

def grab(loadFile):
    localFile = open('copy.html','rb')
    ftp.retrbinary('RETR '+loadFile,localFile.write,1024)
    ftp.close()
    localFile.close()


def transfer(transferFile):
    storefile = 'index.html'
    localFile = open(transferFile)
    ftp.storbinary('STOR '+storefile,localFile)
    ftp.close()
    localFile.close()



    text1 = input('Which File u want to grab?:')
    grab(text1)

    text2 = input('Which File u want to store?:')
    transfer(text2)






