import requests
import subprocess
import admin
import ctypes,sys

def download_certificate():
    URL = "http://webcast.pu.ac.in/cert/Fortinet_CA_SSL.cer"
    response = requests.get(URL)
    if response.status_code == 200:
        with open("Fortinet.cer","wb") as cert:
            cert.write(response.content)
        print "Download Complete!"
    elif response.status_code == 404:
        print "File not found!!"
    else:
        print "Download Failed!"
        print response.status_code

def install_certificate():
    from subprocess import Popen,PIPE
    process = Popen(['runas','/user:Administrator','certutil','-addstore','Root','Fortinet.cer'],stdout=PIPE,stderr=PIPE,shell=True)
    stdout,stderr = process.communicate()
    print stdout
    print "Err: ",stderr
    import os

def list_certificates():
    print ""

install_certificate()