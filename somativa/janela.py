from tkinter import *
import bd
from threading import *



class tela:

    def __init__(self):
        self.root = Tk()
        self.users = ["multilaser", "Samsung", "motorola", "Apple", "Xiaomi"]
        self.users_l = [str(i) for i in range(len(self.users))]
        self.selected_users = []
        self.bda = bd.bd()
        self.tela()
        self.frames()
        self.botoes()
        self.checkbox()
        self.root.mainloop()

    def tela(self):
        self.root.title("Amazon SmartPhone Filter")
        self.root.geometry("800x600")
        self.root.configure(background='#bdbcb3')
        self.frames()

    def frames(self):
        self.frame1 = Frame(self.root, bg="#b0afa9")
        self.frame1.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.08)

        self.frame2 = Frame(self.root, bg="#b0afa9")
        self.frame2.place(relx=0.03, rely=0.14, relwidth=0.94, relheight=0.75)

    def threading(self):
        self.btScrap["state"] = "disabled"
        t1 = Thread(target=self.chama)
        t1.start()


    def chama(self):
        self.bda.atualiza()
        self.btScrap["state"] = "normal"



    def botoes(self):
        self.btScrap = Button(self.frame1, text="SCRAP", command=self.threading)
        self.btScrap.place(relx=0.05, rely=0.20, relwidth=0.1, relheight=0.50)

    def add_remove(self, user, var):
        if var.get() == 0:
            self.selected_users.remove(user)
        else:
            self.selected_users.append(user)
        


    def checkbox(self):
        for x in range(len(self.users)):
            self.users_l[x] = IntVar()
            l = Checkbutton(self.frame1, text=self.users[x], variable=self.users_l[x], offvalue=0, onvalue=1,
                            command=lambda x=self.users[x], y=self.users_l[x]: self.add_remove(x, y))
            l.pack(side= RIGHT)



tela()