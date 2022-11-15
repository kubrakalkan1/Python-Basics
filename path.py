from pathlib import  Path
#Absolute path -- C:\Program Files\Microsoft
#Relative path -- in the project

path0 = Path("ecommerce")
path1 = Path("ecommerce1")
path2 = Path("emails")
print(path0.exists()) #True
print(path1.exists()) #False
# print(path2.mkdir()) #create directory
# print(path2.rmdir()) #delete directory

path = Path()
for file in path.glob('*'): #search all path current directory
    print(file)

