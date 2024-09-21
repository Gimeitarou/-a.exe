import subprocess

f = open('D:\\pic_name.txt', 'r', encoding='UTF-8')
basename = f.read() #read the note text of the file name of the pic
f.close()

subprocess.run('attrib -r -h d:\\Do_not_misuse.exe' #hide Do_not_misuse.exe
                +f'&& attrib -r -h d:\\{basename}' #hide the pic
                +'&& attrib -r -h d:\\pic_name.txt', shell=True)