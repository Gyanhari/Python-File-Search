from searchfile import search_file
from searchfolder import searchfolder

def main():
	choice = 0
	name = ''
	while (choice not in [1,2]):
		try: 
			choice = int(input("\nEnter the choice : \n1. File \n2. Folder \n -> "))
		except ValueError:
			print(f"\nThe value you have entered {choice} is not the valid input choose either 1 or 2")

	title_data = "File" if (choice == 1) else "Folder"

	while (len(name) == 0):
		print(f"\nEnter the name of the {title_data} to be searched :  ")
		name = str(input())

	if (choice == 1): #If It is a File
		print(f'Searching For The file {name}. Please wait a moment')
		search_file(name)

	else: #If It is a Folder
		print(f'Searching For The folder {name}. Please wait a moment')
		searchfolder(name)
    
    
if __name__ == "__main__" :
	main()
	print("\nThank you for using our system")
