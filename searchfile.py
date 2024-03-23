""" Imported The os, string and the concurrent.futures module """
import os
import string
import concurrent.futures



def get_available_drives():
	if (os.name == 'posix'):
		drives = os.listdir('/home/');
		available_drives = []
		for drive in drives:
			available_drives.append("/home/"+drive)
	else : 
		a_available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
		available_drives = [drive + '\\' for drive in a_available_drives]
	print(available_drives)
	return (available_drives)

def search_file(drive, file_name):
    """ Used to search file that is inputed by the user """
    all_matched_files = []
    # print(drive)
    matched_files = file_existence(drive, file_name)
    all_matched_files.extend(matched_files)
    return all_matched_files

def file_existence(drive, file_name):
    """ Uses os.walk to check whether the file exists ot not """
    matched_files = []
    for root, dirs, files in os.walk(drive):
        for file in files:
            if file == file_name:
                temp = file_address(root, file)
                matched_files.append(temp)
    return matched_files

def file_address(root, file_name):
    """ Used to make a path to found file """
    return os.path.join(root, file_name)


def multiprocess_search(file_name):
    """ Use to run the 'search_file' function over at differnt cpu cores"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        drives = get_available_drives()
        results = executor.map(search_file, drives, [file_name]*len(drives))
        matched_files = []
        for result in results:
            matched_files.extend(result)
        return matched_files
