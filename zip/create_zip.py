#Zipfile - Code Adhyayana

import zipfile

files = ['file1.txt', 'file2.txt', 'file3.txt']

zip_file = 'files.zip'

#Create zip file
with zipfile.ZipFile(zip_file, 'w') as zip:
    for file in files:
        zip.write(file)


#Extract zip files
with zipfile.ZipFile(zip_file, 'r') as zip:
    zip.extractall(path='./')