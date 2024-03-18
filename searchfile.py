from dependency import os,path,re,string
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

def searchfile(file_name):
    file_existence("sample",file_name)




def file_existence(drive,file_name):
    matched_files = [] 
    for root, dirs, files in os.walk(drive):
        for file in files:
            if file == file_name:
                temp=fun_name(root,file)
                matched_files.append(temp)
               
           


