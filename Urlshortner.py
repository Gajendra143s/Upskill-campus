from tkinter import *

import pyshortner
import pyperclip

root = Tk()
root.tittle("URL SHORTNER")
root.configure(bg = "yellow")

url = StringVar()
shortUrl = StringVar()

def urlshort():
    shortUrl = url.get()
    generatedurl = pyshortners.shortener().tinyurl.short(shortUrl)
    shortUrl.set(generatedurl)

def copy():
    generatedurl = shortUrl.get()
    pyperclip.copy(generatedurl)

label = label(root,text = "Url shortner App", font ="Arial")
label.pack(pady = 10)

Entry(root,textvariable = url).pack(pady = 5)
Button(root,text= "generate url", command = urlshort).pack(pady = 5)

Entry(root,textvariable = shortUrl).pack(pady = 5)
Button(root,text= "generate url", command = copy).pack(pady = 5)

root.mainloop()
