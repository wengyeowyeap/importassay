from tkinter import *  
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pyuac
import os
from ttkthemes import ThemedTk

def backupdb():
  dbfile = askopenfilename()
  os.system(f"mysql -uroot -pAssay123! assay < {dbfile}")
  root.destroy()

root = ThemedTk(theme="radiance")
root.title("Import database")
importbutton = ttk.Button(root, text = 'Import database', command = backupdb)
importbutton.grid(column = 0,  row = 0, padx = 15)

def runadmin():
  if not pyuac.isUserAdmin():
    return pyuac.runAsAdmin()
  else:
    root.destroy()

runadmin()

root.mainloop()  
