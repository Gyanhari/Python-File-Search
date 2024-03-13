import os 
import os.path as path
from searchfile import searchfile
from searchfolder import searchfolder

def main():
    dir_or_file = 0
    filename = str(input("Enter File/Directory name: "))
    print("Select If your search is file or a directory\n")
    while(dir_or_file !=1 and dir_or_file !=2):
        try:
            dir_or_file = int(input("Enter 1 for file and 2 for directory: "))
        except ValueError:
            print("Enter a Number 1 or 2 \n")
            
    if dir_or_file == 1: #If It is a File        
        print(f'Searching For The file {filename}. Please wait a moment')
        searchfile(filename)

    else: #If It is a Folder
        print(f'Searching For The folder {filename}. Please wait a moment')
        searchfolder(filename)
    
    
if __name__ == "__main__" :
	main()
	print("\nThank you for using our system")
