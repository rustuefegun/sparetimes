from tkinter import*

window = Tk()
window.title("Afghanistan Simulator")

photo = PhotoImage(file='soldier.png')
photo_2 = PhotoImage(file='bullet.png')

def clickbro():
    f = "Taliban Victory\n died a lot of\nchildren..."
    label.configure(text = f)
    print('You clicked the button')

def clickbro_2():
    f = "Distributing\nDemocracy!"
    label.configure(text = f)
    print('You clicked the button')


label = Label(window,
              text="Afghanistan War",
              font=('Arial',40,'italic'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=5,
              pady=5,
              image=photo,
              compound='bottom'
              )
label.pack()


button = Button(window,
                text='Vote the Others',
                fg='#00FF00',
                bg='black',
                font=('Comic Sans',30),
                relief=RAISED,
                bd=10,
                command=clickbro_2,
                activebackground='black',
                activeforeground='#00FF00',
                state=ACTIVE,
                image=photo_2,
                compound='right')
button.pack()
#label.place(x=0,y=0)
button_2 = Button(window,
                text='Vote Joe Biden',
                fg='#00FF00',
                bg='black',
                font=('Comic Sans',30),
                relief=RAISED,
                bd=10,
                command=clickbro,
                activebackground='black',
                activeforeground='#00FF00',
                state=ACTIVE,
                image=photo_2,
                compound='right')
button_2.pack()
window.mainloop()
