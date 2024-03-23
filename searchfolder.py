from dependency import * 

def get_available_drives():
	if (os.name == 'posix'):
		drives = os.listdir('/home/');
		available_drives = []
		for drive in drives:
			available_drives.append("/home/"+drive)
	else : 
		available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
	print(available_drives)
	return (available_drives)

def normalize_folder(folder_name):
    return folder_name.lower()
     


def folder_existence(drive,folder_name):
	s_folder = normalize_folder(folder_name)
	folders = []
	for root, dirs, files in os.walk(drive):
		for dir in dirs:
			if normalize_folder(dir) == s_folder:
				folder_path = find_folder_path(root, folder_name) 
				folders.append(folder_path) 
	return folders 



def searchfolder(folder_name):
	folders = multiprocessing_search(folder_name)
	if len(folders):
		print("Search results: ")
		display_all(folders)
	else:
		print("Folder not found")


def find_folder_path(root_path, folder_name):
   abc = os.path.join(root_path, folder_name)
   if os.path.exists(abc):
       return abc
   else:
       return None

def multiprocessing_search(folder_name):
	match_folder = []
	with concurrent.futures.ProcessPoolExecutor() as executor:
		drives = get_available_drives()
		results = executor.map(folder_existence,drives,[folder_name]*len(drives))
		for result in results:
			match_folder.extend(result)
		return match_folder

def display_all(folders):
	i:int =0
	for data in folders: 
		print(f"{i}. {data}")
		i +=1 
	
