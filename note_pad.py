import tkinter as TK  
import os  
from tkinter import *  
from tkinter.messagebox import *  
from tkinter.filedialog import *  
  
class Notepad_file:  
  
    __root = Tk()  
  
    # default window width and height  
    __thisWidth = 350  
    __thisHeight = 350  
    __thisTextArea = Text(__root)  
    __thisMenuBar = Menu(__root)  
    __thisFileMenu = Menu(__thisMenuBar, tearoff = 0)  
    __thisEditMenu = Menu(__thisMenuBar, tearoff = 0)  
    __thisHelpMenu = Menu(__thisMenuBar, tearoff = 0)  
      
    # For adding the scrollbar  
    __thisScrollBar = Scrollbar(__thisTextArea)   
    __file = None  
  
    def __init__(self, **kwargs):  
  
        # Here, we will Set the icon  
        try:  
                self.__root.wm_iconbitmap("Notepad.ico")  
        except:  
                pass  
  
# here, we will set the window size, the default window size is 300 x 300  
  
        try:  
            self.__thisWidth = kwargs['width']  
        except KeyError:  
            pass  
  
        try:  
            self.__thisHeight = kwargs['height']  
        except KeyError:  
            pass  
  
        # here, we will set the window text  
        self.__root.title("Untitled- Notepad File")  
  
        # here, we will set the center the window  
        screenWidth = self.__root.winfo_screenwidth()  
        screenHeight = self.__root.winfo_screenheight()  
      
        # For left-align  
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        # For right-align  
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        # For top and bottom  
        self.__root.geometry('%d x %d + %d + %d' % (self.__thisWidth,  
                                            self.__thisHeight,  
                                            left, top))  
  
    # Here, we are making the text-area auto resizable  
        self.__root.grid_rowconfigure(0, weight = 1)  
        self.__root.grid_columnconfigure(0, weight = 1)  
  
        # Here, we will add the controls such as widgets  
        self.__thisTextArea.grid(sticky = N + E + S + W)  
          
        # For opening the new file  
        self.__thisFileMenu.add_command(label = "New FIle",  
                                        command = self.__newFile1)  
          
        # For opening the already existing file from the menu  
        self.__thisFileMenu.add_command(label = "Open File",  
                                        command = self.__openFile1)  
          
        # For saving the current working file  
        self.__thisFileMenu.add_command(label = "Save File",  
                                        command = self.__saveFile1)  
  
        # For creating the line in the dialog Box     
        self.__thisFileMenu.add_separator()                                       
        self.__thisFileMenu.add_command(label = "Exit File",  
                                        command=self.__quitApplication1)  
        self.__thisMenuBar.add_cascade(label = "File Menu",  
                                    menu = self.__thisFileMenu)   
          
        # for giving the feature of cutting in Files  
        self.__thisEditMenu.add_command(label = "Cut in File",  
                                        command = self.__cut1)            
      
        # For giving the feature of copying in file  
        self.__thisEditMenu.add_command(label = "Copy in File",  
                                        command = self.__copy1)       
          
        # for giving the feature of pasting in file  
        self.__thisEditMenu.add_command(label = "Paste in File",  
                                        command = self.__paste1)          
          
        # for giving the feature of editing in file  
        self.__thisMenuBar.add_cascade(label = "Edit in File",  
                                    menu = self.__thisEditMenu)   
          
        # FOr creating the feature of description of the notepad File  
        self.__thisHelpMenu.add_command(label = "About Notepad File",  
                                        command = self.__showAbout1)  
        self.__thisMenuBar.add_cascade(label = "Help in File",  
                                    menu = self.__thisHelpMenu)  
  
        self.__root.config(menu = self.__thisMenuBar)  
  
        self.__thisScrollBar.pack(side = RIGHT,fill=Y)                
# Here, the scroll-bar will get adjusted automatically according to the content   
# of the file  
        self.__thisScrollBar.config(command = self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)  
      
          
    def __quitApplication1(self):  
        self.__root.destroy()  
        # exit()  
  
    def __showAbout1(self):  
        showinfo("Notepad File","Javatpoint")  
  
    def __openFile1(self):  
          
        self.__file = askopenfilename(defaultextension = ".txt",  
                                    filetypes = [("All Files","*.*"),  
                                        ("Text Documents","*.txt")])  
  
        if self.__file == "":  
              
            # If there is no file to open  
            self.__file = None  
        else:  
              
            # For trying to open the file set the window title  
            self.__root.title(os.path.basename(self.__file) + " - Notepad File")  
            self.__thisTextArea.delete(1.0, END)  
  
            file = open(self.__file, "r")  
  
            self.__thisTextArea.insert(1.0, file.read())  
  
            file.close()  
  
          
    def __newFile1(self):  
        self.__root.title("Untitled- Notepad File")  
        self.__file = None  
        self.__thisTextArea.delete(1.0, END)  
  
    def __saveFile1(self):  
  
        if self.__file == None:  
            # For Saving as new file  
            self.__file = asksaveasfilename(initialfile = 'UntitledFile.txt',  
                                            defaultextension = ".txt",  
                                            filetypes = [("All Files","*.*"),  
                                                ("Text Documents", "*.txt")])  
  
            if self.__file == "":  
                self.__file = None  
            else:  
                  
                # For trying to  save the file  
                file = open(self.__file,"w")  
                file.write(self.__thisTextArea.get(1.0, END))  
                file.close()  
                  
                # For changing the window title  
                self.__root.title(os.path.basename(self.__file) + " - Notepad File")  
                  
              
        else:  
            file = open(self.__file,"w")  
            file.write(self.__thisTextArea.get(1.0, END))  
            file.close()  
  
    def __cut1(self):  
        self.__thisTextArea.event_generate("<<Cut in File>>")  
  
    def __copy1(self):  
        self.__thisTextArea.event_generate("<<Copy in File>>")  
  
    def __paste1(self):  
        self.__thisTextArea.event_generate("<<Paste in File>>")  
  
    def run1(self):  
  
        # For running the main application  
        self.__root.mainloop()  
  
  
  
  
# For running the main application  
notepad1 = Notepad_file(width = 650, height = 450)  
notepad1.run1()  