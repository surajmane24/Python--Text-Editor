from tkinter import *
from tkinter import filedialog, messagebox

class TextEditor:
    current_file="No-File"


    def clear(self):
        self.txt_area.delete(1.0,END)

    def open_file(self,event=""):
        R = filedialog.askopenfile(initialdir="/",title="Open file",filetypes=(("Text File","*.txt"),("All File","*.*")))
        for data in R:
            self.txt_area.insert(INSERT,data)
        self.current_file=R.name

    def saveas_file(self):
       # f = filedialog.asksaveasfile(mode="w", defaultextension="*.txt")
        f = filedialog.asksaveasfile(mode="w", defaultextension=(("Text File","*.txt"),("All File","*.*")))
        data=self.txt_area.get(1.0,END)
        f.write(data)
        self.current_file=f.name
        f.close()

    def save_file(self):
        if self.current_file=="No-File":
            self.saveas_file()
        else:
            f = open(self.current_file,mode="w")
            f.write(self.txt_area.get(1.0,END))
            f.close()

    def new_file(self):
        s=self.txt_area.get(1.0,END)
        if not s.strip():
            pass
        else:
            R=messagebox.askyesnocancel("Save","DO You Want TO Save")
            if R==True:
                self.saveas_file()
                self.clear()
            elif R==False:
                self.clear()

    def exit_file(self):
        s = self.txt_area.get(1.0, END)
        if not s.strip():
            quit()
        else:
            R=messagebox.askyesnocancel("Save","DO You Want TO Save")
            if R==True:
                self.saveas_file()
                quit()
            elif R == False:
                quit()

    def copy(self):
        self.txt_area.clipboard_clear()
        self.txt_area.clipboard_append(self.txt_area.selection_get())

    def paste(self):
        self.txt_area.insert(INSERT,self.txt_area.clipboard_get())

    def cut(self):
        self.copy()
        self.txt_area.delete('sel.first','sel.last')

    def delete(self):
        self.txt_area.delete('sel.first','sel.last')


    def __init__(self,window):
        self.window = window
        self.window.title("Text Editor")
        self.txt_area=Text(window, padx = 5, pady = 5, wrap = WORD, bd = 2,undo = True)
        self.txt_area.pack(fill = BOTH, expand = 1)

        self.main_menu = Menu()
        self.window.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu,tearoff = FALSE)
        self.main_menu.add_cascade(label ="FILE", menu = self.file_menu)
        self.file_menu.add_command(label = "New", accelerator = "Ctrl+n", command = self.new_file)
        self.window.bind("<Control-n>", self.new_file)
        self.file_menu.add_command(label = "Open", accelerator = "Ctrl+o", command = self.open_file)
        self.window.bind("<Control-o>", self.open_file)
        self.file_menu.add_command(label = "Save", accelerator = "Ctrl+s",command = self.save_file)
        self.window.bind("<Control-s>", self.save_file)
        self.file_menu.add_command(label = "Save as", command = self.saveas_file)
        self.file_menu.add_command(label = "Exit", accelerator = "Ctrl+e",command = self.exit_file)
        self.window.bind("<Control-e>", self.exit_file)


        self.edit_menu = Menu(self.main_menu, tearoff=FALSE)
        self.main_menu.add_cascade(label="EDIT", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command = self.txt_area.edit_undo)
        self.edit_menu.add_command(label="Red0", command = self.txt_area.edit_redo)
        self.edit_menu.add_command(label="Cut",accelerator = "Ctrl+x", command = self.cut)
        self.window.bind("<Control-x>", self.cut)
        self.edit_menu.add_command(label="Copy",accelerator = "Ctrl+c", command = self.copy)
        self.window.bind("<Control-c>", self.copy)
        self.edit_menu.add_command(label="Paste",accelerator = "Ctrl+v", command = self.paste)
        self.window.bind("<Control-v>", self.paste)
        self.edit_menu.add_command(label="Delete",accelerator = "Ctrl+u", command = self.delete)
        self.window.bind("<Control-u>", self.delete)

root = Tk()
b = TextEditor(root)
root.mainloop()
