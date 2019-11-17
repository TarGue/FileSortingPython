import os
import shutil

path = os.path.dirname(os.path.abspath(__file__))+'\\'
names = os.listdir(path)

folder_name = ['1-Word','2-Praesentation','3-Excel','4-PDFs']
for x in range(0,4):
    if not os.path.exists(path+'\\'+folder_name[x]):
        os.makedirs(path+'\\'+folder_name[x])
for files in names:
    if ".docx" in files and not os.path.exists(path+'1-Word\\'+files):
        shutil.move(path+files, path+'1-Word\\'+files)
    if ".pptx" in files and not os.path.exists(path+'2-Praesentation\\'+files):
        shutil.move(path+files, path+'2-Praesentation\\'+files)
    if ".xlsx" in files and not os.path.exists(path+'3-Excel\\'+files):
        shutil.move(path+files, path+'3-Excel\\'+files)
    if ".pdf" in files and not os.path.exists(path+'4-PDFs\\'+files):
        shutil.move(path+files, path+'4-PDFs\\'+files)
