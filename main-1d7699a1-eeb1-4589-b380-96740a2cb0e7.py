from tkinter import *#import all from tkinter
from PIL import ImageTk, Image#import 2 items from PIL

class Book():#Create Book Class
    def __init__(#initializaion function
            self, #Used to tie arguments to class variables
            title_var,#Book Title
            author_var,#Book Author
            price_var, #Book Price
            image_var):#Book Image
        self.title_var = title_var#Argument assigned to class variable
        self.author_var = author_var#Argument assigned to class variable
        self.price_var = price_var#Argument assigned to class variable
        self.image_var = image_var#Argument assigned to class variable
    def get_title(self):#Define get_title Function
        return self.title_var#Return title_var
    def get_author(self):#Define get_author Function
        return self.author_var# Return author_var
    def get_price(self):#Define get_price Function
        return self.price_var# Return price_var
    def get_image(self):#Define get_image Function
        return self.image_var# Return image_var

root = Tk()#Create window variable
root.title('Book Database')#Assign Title to window
root.geometry("+600+100")#Change location of window
root.iconbitmap('Book_Databases_Icon.ico')#Assign icon to window

book_var_001 = Book(#Initilize book
    "Title: Homeland",#Set Title
    "Author: R.A. Salvatore",#Set Author
    "Price: $1.98",#Set Price
    ImageTk.PhotoImage(Image.open(#Set Image
    "homeland_rasalvatore2.png")))#Image Title

book_var_002 = Book(#Initilize book
    "Title: Exile",#Set Title
    "Author: R.A. Salvatore",#Set Author
    "Price: $2.98",#Set Price
    ImageTk.PhotoImage(Image.open(#Set Image
    "exile_rasalvatore2.png")))#Image Title

book_var_003 = Book(#Initilize book
    "Title: Sojurn",#Set Title
    "Author: R.A. Salvatore",#Set Author
    "Price: $3.98",#Set Price
    ImageTk.PhotoImage(Image.open(#Set Image
    "sojurn_rasalvatore2.png")))#Image Title

book_var_004 = Book(#Initilize book
    "Title: The Crystal Shard",#Set Title
    "Author: R.A. Salvatore",#Set Author
    "Price: $4.98",#Set Price
    ImageTk.PhotoImage(Image.open(#Set Image
    "thecrystalshard_rasalvatore2.png")))#Image Title

book_var_005 = Book(#Initilize book
    "Title: Streams of Silver",#Set Title
    "Author: R.A. Salvatore",#Set Author
    "Price: $5.98",#Set Price
    ImageTk.PhotoImage(Image.open(#Set Image
    "streamsofsilver_rasalvatore2.png")))#Image Title

#Create list to store books
book_list = [book_var_001,
             book_var_002,
             book_var_003,
             book_var_004,
             book_var_005]

#Create list to hold book images
image_list = [book_var_001.get_image(),
              book_var_002.get_image(),
              book_var_003.get_image(),
              book_var_004.get_image(),
              book_var_005.get_image()]

#Create string variables that can be modified as application runs
output_string_price = StringVar(
    value=book_list[0].get_price())#Set initial value of variable
output_string_title = StringVar(
    value=book_list[0].get_title())#Set initial value of variable
output_string_author = StringVar(
    value=book_list[0].get_author())#Set initial value of variable

image_label = Label(#Create label to hold image
    image=book_list[0].get_image())
#Choose location for label
image_label.grid(#Set location of label
    row=0,#Set location of label
    column=0,#Set location of label
    columnspan=3)#Set location of label
#Create label for price
price_label = Label(
    textvariable=output_string_price,#Text displayed on label
    font=("Ariel", #font to be used
          12),#font size
    bd=1)
#Choose location for label
price_label.grid(#Set location of label
    row=1,#Set location of label
    column=0)#Set location of label
#Create label for title
title_label = Label(
    textvariable=output_string_title,#Text displayed on label
    font=("Ariel", #font to be used
          12),#font size
    bd=1)
#Choose location for label
title_label.grid(#Set location of label
    row=1,#Set location of label
    column=1)#Set location of label
#Create label for Author
author_label = Label(
    textvariable=output_string_author,#Text displayed on label
    font=("Ariel",#font to be used
        12),#font size
    bd=1)
#Choose location for label
author_label.grid(#Set location of label
    row=1,#Set location of label
    column=2)#Set location of label
#Define function for forward button
def forward(image_number):
    image_label = Label(
        root,
        image=book_list[
            image_number-1].get_image())
    image_label.grid(#Set location of label
        row=0,#Set location of label
        column=0,#Set location of label
        columnspan=3)#Set location of label
    output_string_price.set(
        str(book_list[
                image_number - 1].get_price()))
    output_string_title.set(
        str(book_list[
                image_number - 1].get_title()))
    output_string_author.set(
        str(book_list[
                image_number - 1].get_author()))
    button_forward = Button(
        root,
        text=">>",#Text displayed on button
        command=lambda: forward(image_number+1),#function to be called
        font=("Ariel", #font to be used
              12))#font size
    button_back = Button(
        root,
        text="<<",#Text displayed on button
        command=lambda: back(image_number-1),#function to be called
        font=("Ariel", #font to be used
              12))#font size
    if image_number == 5:#if image_number is 5, run the following
        button_forward = Button(
            root,
            text=">>",#Text displayed on button
            state=DISABLED,
            font=("Ariel", #font to be used
                  12))#font size
    image_label.grid(#Set location of label
        row=0,#Set location of label
        column=0,#Set location of label
        columnspan=3)#Set location of label
    button_back.grid(#Set location of button
        row=2,#Set location of button
        column=0)#Set location of button
    button_forward.grid(#Set location of button
        row=2,#Set location of button
        column=2)#Set location of button

    # Define function for back button
def back(image_number):
    image_label = Label(
        image=book_list[
            image_number - 1].get_image())
    image_label.grid(#Set location of label
        row=0,#Set location of label
        column=0,#Set location of label
        columnspan=3)#Set location of label
    output_string_price.set(
        book_list[
            image_number - 1].get_price())
    output_string_title.set(
        book_list[
            image_number - 1].get_title())
    output_string_author.set(
        book_list[
            image_number - 1].get_author())
    button_forward = Button(
        root,
        text=">>",#Text displayed on button
        command=lambda: forward(#function to be called
            image_number+1),
        font=("Ariel", #font to be used
              12))#font size
    button_back = Button(
        root,
        text="<<",#Text displayed on button
        command=lambda: back(#function to be called
            image_number-1),
        font=("Ariel", #font to be used
              12))#font size
    if image_number == 1:#if image_number is 1, run the following
        button_back = Button(
            root,
            text="<<",#Text displayed on button
            state=DISABLED,
            font=("Ariel", #font to be used
                  12))#font size
    image_label.grid(#Set location of label
        row=0,#Set location of label
        column=0,#Set location of label
        columnspan=3)#Set location of label
    button_back.grid(#Set location of button
        row=2,#Set location of button
        column=0)#Set location of button
    button_forward.grid(#Set location of button
        row=2,#Set location of button
        column=2)#Set location of button
#Create button and store it in button_back variable
button_back = Button(
    root,#root is the window that this button will be linked to
    text="<<",#Text displayed on button
    command=back,#function to be called
    font=("Ariel",#font to be used
        12))#font size
#Create button and store it in button_exit variable
button_exit = Button(
    root,#root is the window that this button will be linked to
    text="Exit Program",#Text displayed on button
    command=root.quit,#function to be called
    font=("Ariel",#font to be used
        12))#font size
#Create button and store it in button_forward variable
button_forward = Button(
    root,#root is the window that this button will be linked to
    text=">>",#Text displayed on button
    command=lambda: forward(2),#function to be called
    font=("Ariel",#font to be used
        12))#font size
button_back.grid(#Assign position of button_back
    row=2,
    column=0)
button_exit.grid(#Assign position of button_exit
    row=2,
    column=1)
button_forward.grid(#Assign position of button_forward
    row=2,
    column=2)
root.mainloop()#Begin main loop of application and lauch window