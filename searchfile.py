from dependency import os,path,re
import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print(drives)

def searchfile(file_name):
    pass
