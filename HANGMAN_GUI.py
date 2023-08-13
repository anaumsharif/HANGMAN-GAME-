from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import Image,ImageTk

main =Tk()
main.title("HANGMAN")
main.geometry("800x600")

imageList =[]
for i in range(1,8):
    imageList.append(Image.open("images/hangman0"+str(i)+".png"))
    
# image1 = Image.open("images/hangman01.png")
test =ImageTk.PhotoImage(imageList[0])
label1 = Label(image=test)
label1.image = test
label1.place(x=0,y=0)




MAX_GUESSES = 6
tries = 0
word = "loop"
word = word.lower()
print(word)
while True :
    key = simpledialog.askstring("GUESS","Guess the letter :")
    if key in word:
        messagebox.showinfo("HANGMAN"," The word contains " +key)
        word = word.replace(key,"")
        print(f"Number of words left = {len(word)}")
        if len(word)== 0:
            messagebox.showinfo("HANGMAN","YOU WIN ")
            break
    else:
        messagebox.showinfo("HANGMAN","Wrong guess")
        tries = tries+1
        test = ImageTk.PhotoImage(imageList[tries])
        label1 = Label(image=test)
        label1.image = test
        label1.place(x=0, y=0)
        
        if tries>= MAX_GUESSES:
            messagebox.showinfo("HANGMAN","YOU LOST ")
            break 