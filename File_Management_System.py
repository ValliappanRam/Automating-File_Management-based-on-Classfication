import os 
import shutil

file_path = os.path.expanduser("~")
file_name = file_path+"\\"+"Rules.txt"
file_t = open(file_name,'r')
path = file_t.readline()
path1 = path.strip("\n")
mode = file_t.readline()


#Creating a Dictionary for File extension and Their Respective Rule location rules
def rule():
    di = {}
    for each in file_t:
        each = each.strip("\n")
        if  each.split(":",1)[0]:
            ext,loc = each.split(":",1)
            ext = ext.strip()
            loc = loc.strip()
        di[ext]=loc
        if os.path.exists(loc):
            pass
        else:
            os.mkdir(loc)
    return di

di = rule() 
def move(files_list):
    for file in files_list:
        if "." in file:
            fext = file.rsplit(".",1)[1]
            fext = fext.strip()
        if fext in di:
            dst = di[fext]
            try:
                print(file)
                shutil.move(file,dst)
            except Exception as e:
                print(e)

def single_dir(path1):
    os.chdir(path1)
    files = os.listdir(".")
    move(files)

def rec_dir(path1):
    for root,dirs,files in os.walk(path1,topdown=False,onerror=None,followlinks= False):
        os.chdir(root)
        move(files)
        os.chdir(dirs)
        move(files)
        print('Files are Moved')

if mode.lower()=='r':
    rec_dir(path1)
else:
    single_dir(path1)

file_t.close()

    
            
    




