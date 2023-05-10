import os

print("**Add a '\\' at the end of the file.**")

path = input("Enter the path: ")
path.replace('\\','/')

def main():
    i = 0
    ext = input("Enter the extention for you file: ")
    name = input("Enter new file name: ")
    for filename in os.listdir(path):
        new_name = path+name+str(i)+ext
        i += 1
        old_name = path+filename
        os.rename(old_name,new_name)
main()