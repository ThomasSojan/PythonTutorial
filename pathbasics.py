from pathlib import Path


#check the file
path1 = Path("modules")
print(path1.exists())


#new directory
path2 = Path("NewDirectory")
path2.mkdir()  #rmdir() for deleting


path = Path()
for file in path.glob("*"):
    print(file)


