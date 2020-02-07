import pdfkit as pdf
import wikipediaapi
import wikipedia
import tkinter as TK
import os


def printArtical():
    #Find a random artical
    ranWiki = wikipedia.random(pages=1)
    print(ranWiki)

    wiki = wikipediaapi.Wikipedia('en')

    #Making the name of the page into a URL
    page_py = wiki.page(ranWiki)
    print(page_py)
    url = page_py.fullurl

    #Print the artical
    pdf.from_url(url, ranWiki + '.pdf')

    #Opens the PDF file
    os.startfile(ranWiki + '.pdf')

#Tkinter GUI 
root = TK.Tk()
root.geometry("300x300")


btnText = "Random Wiki Artical Generator"
btn = TK.Button(root, text=btnText, pady=20, command=printArtical)
btn.place(relx=0.25, rely=0.25)


root.mainloop()

