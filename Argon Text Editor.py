import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog,messagebox
import os
import webbrowser as wb
from ttkthemes import ThemedTk
#import tkFont
#creating window
main_application = ThemedTk(theme = "radiance")
main_application.geometry("1200x800")
main_application.title("Argon Text Editor")
main_application.wm_iconbitmap("Ar.ico")

'''Main menu'''
#menu
main_menu = tk.Menu()       #main menu that holds other menu


############# FILE MENU ########################
file = tk.Menu(main_menu, tearoff = False)   #file menu
#icons image files
new_icon = tk.PhotoImage(file = "icons/new.png")
open_icon = tk.PhotoImage(file = "icons/open.png")
exit_icon = tk.PhotoImage(file = "icons/exit.png")
save_icon = tk.PhotoImage(file = "icons/save.png")
save_as_icon = tk.PhotoImage(file = "icons/save_as.png")



################# edit menu #############

edit = tk.Menu(main_menu, tearoff = False)   #edit menu
#icons
copy_icon = tk.PhotoImage(file = "icons/copy.png")
cut_icon = tk.PhotoImage(file = "icons/cut.png")
paste_icon = tk.PhotoImage(file = "icons/paste.png")
clear_all_icon = tk.PhotoImage(file = "icons/clear_all.png")
find_icon = tk.PhotoImage(file = "icons/find.png")
undo_icon = tk.PhotoImage(file = "icons/undo.png")
redo_icon = tk.PhotoImage(file = "icons/redo.png")


##### VIEW #####
view = tk.Menu(main_menu,tearoff = False)   #view
#view icons
tool_bar_icon = tk.PhotoImage(file = "icons/tool_bar.png")
status_bar_icon = tk.PhotoImage(file = "icons/status_bar.png")



###### VIEW ENDS ########

###### COLOR THEME #########
color_theme = tk.Menu(main_menu,tearoff = False)    #color menu
#theme icons/images
light_default_icon = tk.PhotoImage(file = "icons/light_default.png")
light_plus_icon = tk.PhotoImage(file = "icons/light_plus.png")
dark_icon = tk.PhotoImage(file = "icons/dark.png")
night_blue_icon = tk.PhotoImage(file = "icons/night_blue.png")
red_icon = tk.PhotoImage(file = "icons/red.png")
monokai_icon = tk.PhotoImage(file = "icons/monokai.png")
#ends here

theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_default_icon,dark_icon,night_blue_icon,red_icon,monokai_icon)

color_dict = {                              
    "Light Default" : ("#000000","#ffffff"),            ## (textcolor,background color)
    "Light Plus" : ("#474747","#e0e0e0"),
    "Dark" : ("#c4c4c4","#2d2d2d"),
    "Red" : ("#2d2d2d","#ffe8e8"),
    "Monokai" : ("#d3b774","#474747"),
    "Night Blue" : ("#ededed","#6b9dc2")

}
#about menu
def about():
    new_window = tk.Toplevel()
    new_window.geometry("240x100")
    new_window.title("Argon Text Editor")
    name_label = ttk.Label(new_window,text = "Developed by Shaikh Sajid\n version : v1.0")
    def follow():
        wb.open("https://www.instagram.com/shaikhsajid1111")
    follow_button = ttk.Button(new_window,text = "Follow",width = 20,command = follow)
    follow_button.pack(pady = 10)
    name_label.pack(pady = 5,padx= 5)
help_user = tk.Menu(main_menu,tearoff = False)
help_user.add_command(label = "About",compound = tk.LEFT,command = about)
#toolbar 
#main toolbar
tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP,fill = tk.X)
#main_toolbar ends

#font box for user choice
font_tuple = tk.font.families()             #contains all font families names
font_family = tk.StringVar()            #string variable for storing value of font options from user
font_box = ttk.Combobox(tool_bar,width = 30,textvariable = font_family,state = "readonly") #combobox
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row = 0,column = 0,padx = 5)
#font box ends here

#font size box
font_size = tk.IntVar()
font_size_box = ttk.Combobox(tool_bar,width = 14,textvariable = font_size,state = "readonly")
font_size_box["values"] = tuple(range(2,120,4))
font_size_box.current(2)
font_size_box.grid(row = 0, column = 1,padx = 5)


#buttons icons
bold_icon = tk.PhotoImage(file = "icons/bold.png")
italic_icon = tk.PhotoImage(file = "icons/italic.png")
underline_icon = tk.PhotoImage(file = "icons/underline.png")
font_color_icon = tk.PhotoImage(file = "icons/font_color.png")
#buttons icons ends here

#creating buttons

#bold button
bold_btn = ttk.Button(tool_bar,image = bold_icon)
bold_btn.grid(row = 0,column = 2,padx = 5)
#bold over

#italic button
italic_btn = ttk.Button(tool_bar,image = italic_icon)
italic_btn.grid(row = 0,column = 3,padx = 5)
#italic ends here

#underline button
underline_btn = ttk.Button(tool_bar,image = underline_icon)
underline_btn.grid(row = 0,column = 4,padx = 5)
#ends buttons

#font color
font_color_btn = ttk.Button(tool_bar,image = font_color_icon)
font_color_btn.grid(row = 0,column = 5,padx = 5)
#ends

#text align items icons
align_left_image = tk.PhotoImage(file = "icons/align_left.png")
align_center_image = tk.PhotoImage(file = "icons/align_center.png")
align_right_image = tk.PhotoImage(file = "icons/align_right.png")
#ends here

#align icons
align_left_btn = ttk.Button(tool_bar,image = align_left_image)
align_left_btn.grid(row = 0,column = 6,padx = 5)

align_center_btn = ttk.Button(tool_bar,image = align_center_image)
align_center_btn.grid(row = 0,column = 7,padx = 5)

align_right_btn = ttk.Button(tool_bar,image = align_right_image)
align_right_btn.grid(row = 0,column = 8,padx = 5)
#icons



###toolbar
################## Text Editor ########
text_editor = tk.Text(main_application,undo = True)
text_editor.config(wrap = 'word',relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.focus_set()
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

################## Text Editor ends ##########

#####font family and functionalities
current_font_family = "Arial"
current_font_size = 12
text_editor.configure(font = ("Arial",12))


#function to change font family 
def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

#change font size
def change_font_size(event=None):
    global current_font_size
    current_font_size = font_size.get()
    text_editor.configure(font=(current_font_family, current_font_size))

#change to bold
"""def change_bold(event=None):
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == "normal":
        text_editor.configure(font = (current_font_family,current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text_editor.configure(font = (current_font_family,current_font_size, "normal"))"""
def change_bold(event = None):
    """toggle only selected text"""
    try:
        current_tags = text_editor.tag_names("sel.first")
        if "bold" in current_tags:
            text_editor.tag_remove("bold","sel.first","sel.last")
        else:
            text_editor.tag_add("bold","sel.first","sel.last")
            bold_font = tk.font.Font(text_editor,text_editor.cget("font"))
            bold_font.configure(weight = "bold")
            text_editor.tag_configure("bold",font= bold_font)
    except tk.TclError:
        pass        

bold_btn.configure(command = change_bold)           

#change to italic
def change_italic(event=None):
    """making italic the selected text""" 
    try:
        current_tags = text_editor.tag_names("sel.first")
        if "italic" in current_tags:
            text_editor.tag_remove("italic","sel.first","sel.last")
        else:
            text_editor.tag_add("italic","sel.first","sel.last")
            italic_font = tk.font.Font(text_editor,text_editor.cget("font"))
            italic_font.configure(slant = "italic")
            text_editor.tag_configure("italic",font = italic_font)
    except tk.TclError:
        pass               
italic_btn.configure(command = change_italic)           

#change to underline
def underline_text(event=None):
   try:
        current_tags = text_editor.tag_names("sel.first")
        if "underline" in current_tags:
            text_editor.tag_remove("underline","sel.first","sel.last")
        else:
            text_editor.tag_add("underline","sel.first","sel.last")
            underline_font = tk.font.Font(text_editor,text_editor.cget("font"))
            underline_font.configure(underline = 1)
            text_editor.tag_configure("underline",font = underline_font)
   except tk.TclError:
        pass            
underline_btn.configure(command = underline_text)        

#change font color
def change_font_color(event=None):
    try:
        (rgb,hx) = tk.colorchooser.askcolor()
        text_editor.tag_add("color","sel.first","sel.last")
        text_editor.tag_configure("color",foreground = hx)
    except tk.TclError:
        pass    
font_color_btn.configure(command = change_font_color)

#left alignment
def align_left(event=None):
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command = align_left)    

#center alignment
def align_center(event=None):
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command = align_center) 

#text alignment right
def align_right(event=None):
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
align_right_btn.configure(command = align_right)

font_box.bind("<<ComboboxSelected>>", change_font)
font_size_box.bind("<<ComboboxSelected>>", change_font_size)
##### ends
    #status bar
status_bar = tk.Label(text = "Status")
status_bar.pack(side = tk.BOTTOM)

text_change = False
def changed(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        words = len(text_editor.get(1.0,"end-1c").split())
        characters = len(text_editor.get(1.0,"end-1c"))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",changed)    

#status bar ends

#cascading/adding it to main menu
main_menu.add_cascade(label = "File",menu = file)
main_menu.add_cascade(label = "Edit",menu = edit)
main_menu.add_cascade(label = "View",menu = view)
main_menu.add_cascade(label = "Theme",menu = color_theme)
main_menu.add_cascade(label = "Help",menu = help_user)


#adding all the dropdown menu in file menu
url = ""
#new file functionality
def new_file(event = None):
    global url
    text_editor.delete(1.0,tk.END)
file.add_command(label = "New", image = new_icon,compound = tk.LEFT,accelerator = "Ctrl + N",command = new_file)

#open file function
def open_file(event = None):
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select File",filetypes = (("Text File","*.txt"), ("All Files","*.*")))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
file.add_command(label = "Open",image = open_icon,compound = tk.LEFT,accelerator = "Ctrl + O",command = open_file)

def save_file(event = None):
    global url
    try: 
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding = 'utf-8') as file_write:
                file_write.write(content)
        else:
            url = filedialog.asksaveasfile(mode= 'w',defaultextension = '.txt',filetypes = (("Text File","*.txt"),("All Files","*.*")))
            content_2 = tk.get(1.0,tk.END)
            url.write(content_2)
            url.close()
    except:
        return                
file.add_command(label = "Save",image = save_icon,compound = tk.LEFT,accelerator = "Ctrl + S",command = save_file)

#save as functionality
def save_as(event = None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w',defaultextension = ".txt",filetypes = (("Text Files","*.txt"), ("All Files","*.*")))
        url.write(content)
        url.close()
    except:
        return    

file.add_command(label = "Save as",image = save_as_icon,compound = tk.LEFT,accelerator = "Ctrl + Alt + S",command = save_as)
file.add_separator()   #seperator in menu

def exit_func(event=None):
    global url,text_change
    if text_change:                 #if text is written in notepad or modified
        #prompt user before exiting about saving the file
        mbox = messagebox.askyesnocancel("Warning","Do you want to save this file ? ") 
        #if user modified texts and wants changes in the same file and wants to save the changes
        if mbox is True:
            if url:                     #url is file location and if file already exists
                #getting all the contents of the notepad area in a content variable
                content = text_editor.get(1.0,tk.END)   
                #saving the file
                with open(url,'w',encoding = 'utf-8') as file_write:    #opening file as file_write
                    file_write.write(content)               #copying all the content to the file
                    main_application.destroy()          #exiting the file
            #if file doesn't exist and user wants to save this file 
            else:
                content_2 = str(text_editor.get(1.0,tk.END))        #gets all the values in a content variable
                #asking for location, where files needs to saved
                url = filedialog.asksaveasfile(mode ='w',defaultextension = ".txt",filetypes = (("Text Files","*.txt"), ("All Files","*.*"))) 
                #copying all the content in the file
                url.write(content_2)
                #closing the file location
                url.close()
                #exiting
                main_application.destroy()       
        elif mbox is False:
            main_application.destroy()
    else:
            main_application.destroy()    
file.add_command(label = "Exit",image = exit_icon,compound = tk.LEFT,accelerator = "Ctrl + Q",command = exit_func)

############ FILE MENU ENDS ##########
#adding all the dropdowns in edit menu
edit.add_command(label = "Copy",image = copy_icon,compound = tk.LEFT,accelerator = "Ctrl + C",command = lambda : text_editor.event_generate("<Control c>"))
edit.add_command(label = "Cut",image = cut_icon,compound = tk.LEFT,accelerator = "Ctrl + X",command = lambda : text_editor.event_generate("<Control x>"))
edit.add_command(label = "Paste",image = paste_icon,compound = tk.LEFT,accelerator = "Ctrl + V",command = lambda : text_editor.event_generate("<Control v>"))
def undo(event = None):
    try:
        text_editor.edit_undo()
    except tk.TclError:
        
            pass    
edit.add_command(label = "Undo",compound = tk.LEFT,image = undo_icon,accelerator = "Ctrl + Z",command = undo)

def redo(event = None):
    try:
        text_editor.edit_redo()
    except tk.TclError:
        pass    
edit.add_command(label = "Redo",image = redo_icon,compound = tk.LEFT,accelerator = "Ctrl + Y",command = redo)    
def clear_all(event = None):
    text_editor.delete(1.0,tk.END)

edit.add_command(label = "Clear all",image = clear_all_icon,compound = tk.LEFT,accelerator = "Ctrl + Alt + x",command = clear_all)
#lambda : text_editor.delete(1.0,tk.END)

"""Find function functionality"""
def find_function(event = None):

    #find function
    def find():
        word = find_input.get()                         #take input from find_input
        text_editor.tag_remove("match",'1.0',tk.END)        
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END) #searching for the word
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config("match",foreground = "red",background = "yellow")
    def replace():
        word = find_input.get()                 #getting input from variable
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialogue = tk.Toplevel()   #inside find windows
    find_dialogue.geometry("450x250+500+200")   #window size
    find_dialogue.title("Find/replace") #title of the window
    find_dialogue.resizable(0,0)        #cannot be resized
    #frame 
    #making find replace label
    find_frame = ttk.LabelFrame(find_dialogue,text = "Find/replace")
    #putting it in window
    find_frame.pack(pady = 20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find',command = find)
    replace_button = ttk.Button(find_frame, text= 'Replace',command = replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()
    

edit.add_command(label = "Find",image = find_icon,compound = tk.LEFT,accelerator = "Ctrl + F",command = find_function)

#view button
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:        #if show_toolbar is clicked
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill = tk.BOTH,expand = True)
        show_toolbar = True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True    

################### EDIT ENDS ##########

#checkbutton for selecting
view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)
#checkbutton ends

#color theme

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color) 


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image =color_icons[count], variable = theme_choice,compound = tk.LEFT,command = change_theme)
    count += 1

main_application.config(menu = main_menu)

main_application.protocol('WM_DELETE_WINDOW',exit_func)
#shortcuts
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_function)
main_application.bind("<Control-b>",change_bold)
main_application.bind("<Control-i>",change_italic)
main_application.bind("<Control-u>",underline_text)
main_application.bind("<Control-Alt-x>",clear_all)
main_application.bind("<Control-z>",undo)
main_application.bind("<Control-y>",redo)
main_application.mainloop()
