from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("AI GROUND")
        self.root.geometry("830x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue', width=610)
        main_frame.pack()


        img_chat=Image.open('hotel5.jpg')
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=830,image=self.photoimg,text='Ask Me',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=115,height=20,bd=3,relief=RAISED,font=('arial',13),yscrollcommand=self.scroll_y.set,fg='yellow',bg='dimgrey')
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white', width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Your Questions:",font=('arial',12,'bold'),fg='white',bg='tomato')
        label_1.grid(row=0,column=0,padx=5,sticky=W)



        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('arial',14,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',14,'bold'),width=8,fg='darkblue',bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear = Button(btn_frame, text="Info Clear", command=self.clear,font=('arial', 14, 'bold'), width=8, bg='black',fg='yellow')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)


        self.msg=''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 12, 'bold'), fg='green', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)



    #function declaration


    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')


    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please Enter Your Queries'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        #for greetings
        if(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n\n'+'Bot: Hi')
        elif(self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n\n'+'Bot: Hello')
        elif (self.entry.get() == 'hi'):
            self.text.insert(END, '\n\n\n' + 'Bot: Hello')

        elif(self.entry.get()=='how are you?'):
            self.text.insert(END,'\n\n\n'+'Bot: I am fine and you?')
        elif(self.entry.get()=='fine'):
            self.text.insert(END,'\n\n\n'+'Bot: Nice to hear')
        elif(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n\n'+'Bot: Hi')
        elif (self.entry.get() == 'what is your name?'):
            self.text.insert(END, '\n\n\n' + 'Bot: My name is Hotel_helping_chatbot')

        #for room
        elif (self.entry.get() == 'how many rooms are available?'):
            self.text.insert(END, '\n\n\n' + 'Bot: 5 rooms are available sir/mam')
        elif (self.entry.get() == 'can I get a single room?'):
            self.text.insert(END, '\n\n\n' + 'Bot: Yes sir/mam single room is available.')
        elif (self.entry.get() == 'can I get a double bed room?'):
            self.text.insert(END, '\n\n\n' + 'Bot: yes sir/mam double bed room is available.')
        elif (self.entry.get() == 'is luxary room available?'):
            self.text.insert(END, '\n\n\n' + 'Bot: yes sir/mam luxary room is available.')
        elif (self.entry.get() == 'how much does it cost to make a single room?'):
            self.text.insert(END, '\n\n\n' + 'Bot: sir/mam it will take 500tk.')
        elif (self.entry.get() == 'how much does it cost to make a double bed room?'):
            self.text.insert(END, '\n\n\n' + 'Bot: sir/mam it will take 1000tk.')
        elif (self.entry.get() == 'how much does it cost to make a luxary room?'):
            self.text.insert(END, '\n\n\n' + 'Bot: sir/mam it will take 1500tk.')
        elif (self.entry.get() == 'bye'):
            self.text.insert(END, '\n\n\n' + "Bot: Thank you for your chatting.")

        #for meal
        elif (self.entry.get() == 'how many times of meal do you provide?'):
            self.text.insert(END, '\n\n\n' + "Bot: We provide 3 times of meal.")
        elif (self.entry.get() == 'can I get breakfast?'):
            self.text.insert(END, '\n\n\n' + "Bot: Yes, you can have breakfast.")
        elif (self.entry.get() == 'can I get Lunch?'):
            self.text.insert(END, '\n\n\n' + "Bot: Yes, you can have Lunch.")
        elif (self.entry.get() == 'can I get dinner?'):
            self.text.insert(END, '\n\n\n' + "Bot: Yes, you can have dinner.")
        else:
            self.text.insert(END,"\n\n\n"+"Bot: Sorry I didn't get it.")





if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()