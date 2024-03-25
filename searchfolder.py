from dependency import os,path,re,string
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


def normalize_folder(folder_name):
    return folder_name.lower()
     


def folder_existence(drive,folder_name):
    s_folder = normalize_folder(folder_name)
    folders = []
    for drive in available_drives:
        for root, dirs, files in os.walk(drive):
            for dir in dirs:
                if normalize_folder(dir) == s_folder:
                    folder_path = find_folder_path(root, folder_name) 
                    folders.append(folder_path) 

    print(s_folder)
    return folders 



def searchfolder(folder_name):
    folder_path=folder_existence("C:",folder_name)
    
    if folder_path: 
        print("Search results: ")
        for folder in folder_path:
            print(folder)
    else:
        print("Folder not found")


def find_folder_path(root_path, folder_name):
   abc = os.path.join(root_path, folder_name)
   if os.path.exists(abc):
       return abc
   else:
       return None


