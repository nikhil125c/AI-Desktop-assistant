from tkinter import*
from PIL import ImageTk, Image
import speech_to_text
import action
root = Tk()
root.title("NIXON")
root.geometry("570x675")
root.resizable(False , False)
root.config(bg="#050505")

#ask
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END , 'User---->'+ user_val+"\n")
    if bot_val != None:
        text.insert(END , "BOT <---"+str(bot_val)+"\n")
    if bot_val =="ok sir":
        root.destroy()
    
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END , 'User---->'+ send+"\n")
    if bot != None:
        text.insert(END , "BOT <---"+str(bot)+"\n")
    if bot =="ok sir":
        root.destroy()
def del_text():
    text.delete('1.0', "end")





# frame

frame = LabelFrame(root , padx =100 , pady = 7 , borderwidth = 3 ,relief = "raised")
frame.config(bg="#3F3F3F")
frame.grid(row = 0,column=1,padx = 55,pady=10)

#text lable
text_label = Label(frame , text="NIXON", font=("Roboto" , 15 , "bold"), bg="#3F3F3F",fg="white")
text_label.grid(row=0 , column = 0 , padx = 20, pady=10)

#image
image = Image.open("image/AI.jpeg")
new_width = 180  # Adjust these values as needed
new_height = 200

# Resize the image
resized_image = image.resize((new_width, new_height))

# Convert the resized image to a format suitable for Tkinter
photo = ImageTk.PhotoImage(resized_image)
image_label = Label(frame, image=photo)
image_label.image = photo  # Keep a reference
image_label.grid(row=1, column=0, pady=20)

#ADDING  A text widget
text = Text(root , font = ('courier 10 bold'),bg = "#356695")
text.grid(row = 2,column=0)
text.place(x=60,y=350,width=375,height=100)

#entry wiget
entry = Entry(root , justify=CENTER)
entry.place(x=75,y=480,width = 350 , height = 30)

#button
button1 = Button(root,text="ASK", bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=70, y=575)

#button2
button2 = Button(root,text="SEND", bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
button2.place(x=315, y=575)

#button3
button3 = Button(root,text="Delete", bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
button3.place(x=187, y=575)



root.mainloop()