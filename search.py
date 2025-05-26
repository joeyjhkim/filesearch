import os

def search_files(directory, keyword):
    print(f"\nSearching for '{keyword}' in files under '{directory}'...\n")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))
    print(f"\nSearch completed.\n")

#Usage
directory = input("Enter the directory path to search in: ")
keyword = input("Enter the keyword to search for: ")
search_files(directory, keyword)


#Notes
#importing the os package allows interaction with the operating system
#os.walk(<directory>) returns a tuple