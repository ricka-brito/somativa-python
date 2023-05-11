from tkinter import *
from tkinter.ttk import Treeview, Progressbar
import locale
import bd
from threading import *
import webscrap




class tela:

    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        self.root = Tk()
        self.users = ["multilaser", "Samsung", "motorola", "Apple", "Xiaomi"]
        self.users_l = [str(i) for i in range(len(self.users))]
        self.selected_users = []
        self.bda = bd.bd()
        self.tela()
        self.frames()
        self.botoes()
        self.checkbox()
        self.lista_frame2()
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
        self.open_win()
        self.btScrap["state"] = "disabled"
        self.t1 = Thread(target=self.chama)
        self.t1.start()

    def chama(self):
        self.bda.atualiza()
        self.btScrap["state"] = "normal"
        self.pb.stop()
        self.pb['mode'] = 'determinate'
        self.pb['value'] = 100
        self.labelcar['text'] = "PRONTO"
        self.b = Button(self.new, text='OK', command=self.new.destroy)
        self.b.grid(column=0, row=2, columnspan=2, padx=10, pady=20)



    def botoes(self):
        self.btScrap = Button(self.frame1, text="SCRAP", command=self.threading)
        self.btScrap.place(relx=0.05, rely=0.20, relwidth=0.1, relheight=0.50)

    def add_remove(self, user, var):
        if var.get() == 0:
            self.selected_users.remove(user)
        else:
            self.selected_users.append(user)
        if len(self.selected_users) == 0:
            self.listaCli.delete(*self.listaCli.get_children())
        else:
            self.select_list(self.bda.listafiltro(tuple(self.selected_users)))



        
    def lista_frame2(self):
        self.listaCli = Treeview(self.frame2, height=3, columns=('col1', 'col2', 'col3'), show='headings', )
        self.listaCli.heading('#1', text='MARCA', anchor=CENTER)
        self.listaCli.heading('#2', text='MODELO')
        self.listaCli.heading('#3', text='VALOR', anchor=CENTER)

        self.listaCli.column('#1', width=11, anchor=CENTER)
        self.listaCli.column('#2', width=300)
        self.listaCli.column('#3', width=12, anchor=CENTER)


        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def select_list(self, a):
        self.listaCli.delete(*self.listaCli.get_children())
        for i in reversed(a):
            i = list(i)
            i[2] = locale.currency(i[2], grouping=True)
            self.listaCli.insert(parent='', index=0, values=i)

    def open_win(self):
        self.new = Toplevel(self.root)
        self.new.geometry("300x250")
        self.new.title("Carregando")
        self.new.transient(self.root)
        self.new.focus_force()
        self.new.grab_set()
        self.labelcar = Label(self.new , text="FAZENDO O WEBSCRAPPING", font=('Helvetica 11 bold'))
        self.labelcar.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        self.pb = Progressbar(
            self.new,
            orient='horizontal',
            mode='indeterminate',
            length=280
        )
        self.pb.grid(column=0, row=1, columnspan=2, padx=10, pady=20)
        self.pb.start()


    def checkbox(self):
        for x in range(len(self.users)):
            self.users_l[x] = IntVar()
            l = Checkbutton(self.frame1, text=self.users[x], variable=self.users_l[x], offvalue=0, bg="#b0afa9", onvalue=1,
                            command=lambda x=self.users[x], y=self.users_l[x]: self.add_remove(x, y))
            l.pack(side= RIGHT)
