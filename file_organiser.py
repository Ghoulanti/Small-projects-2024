import os
import shutil

class File:
    def __init__(self,name):
        self.name=name
        self.type=os.path.splitext(name)[-1]

file_types={
    '.txt':'Docs',
    '.png':'Images',
    '.jpeg':'Images',
    '.jpg':'Images',
    '.exe':'Executable Files',
    '.apk':'Executable Files',
    '.msi':'Executable Files',
    '.zip':'Zips',
    '.torrent':'Archive Files',
    '.csv':'Data Files',
    '.py':'Python',
    '.ini':'Configuration Files',
    '.hex':'Hexadecimal Files',
    '.pdf':'PDF Files',
}

directory=r'C:\Users\'

for file in os.listdir(directory):
    filename=os.fsdecode(file)
    file_obj=File(filename)
    
    if file_obj.type in file_types:
        folder_name=file_types[file_obj.type]
        folder_path=os.path.join(directory,folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        

        shutil.move(os.path.join(directory,filename),os.path.join(folder_path,filename))
