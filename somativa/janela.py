from tkinter import *
from tkinter.ttk import Treeview, Progressbar, Combobox
import locale
import bd
from threading import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import webscrap
import exporta




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
        self.grafico()
        self.dropdown()
        self.root.mainloop()

    def tela(self):
        self.root.title("Amazon SmartPhone Filter")
        self.root.geometry("800x900")
        self.root.configure(background='#bdbcb3')
        self.root.resizable(False, False)
        self.root.iconbitmap("2742085.ico")
        self.frames()

    def frames(self):
        self.frame1 = Frame(self.root, bg="#b0afa9")
        self.frame1.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.08)

        self.frame2 = Frame(self.root, bg="#b0afa9")
        self.frame2.place(relx=0.03, rely=0.14, relwidth=0.94, relheight=0.45)

        self.frame3 = Frame(self.root, bg="#b0afa9")
        self.frame3.place(relx=0.03, rely=0.62, relwidth=0.94, relheight=0.35)

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
        self.tkwid.destroy()
        self.grafico()
        self.b.grid(column=0, row=2, columnspan=2, padx=10, pady=20)



    def botoes(self):
        self.btScrap = Button(self.frame1, text="SCRAP", command=self.threading, height=2, width=13)
        self.btScrap.pack(side= LEFT, padx=10)

        self.btExport = Button(self.frame1, text="EXPORTAR", height=2, width=13, command=self.open_win2)
        self.btExport.pack(side= LEFT, padx=10)

    def grafico(self):
        self.figura = plt.Figure(figsize=(10, 5), dpi=60)
        self.grafic = self.figura.add_subplot(111)
        self.figura.suptitle("Comparação de preços entre marcas")

        self.canva = FigureCanvasTkAgg(self.figura, self.frame3)
        self.tkwid = self.canva.get_tk_widget()
        self.tkwid.pack(anchor=CENTER, pady=10)

        listas = {
            "Xiaomi": 0,
            "samsung": 0,
            "Apple": 0,
            "multilaser": 0,
            "motorola": 0,
        }


        for i in self.bda.listatudo():
            listas[i[0]] = listas[i[0]] + i[2]
        for i in listas:
            listas[i] = listas[i]/10


        x = np.array(["Xiaomi", "Samsung", "Apple", "multilaser", "Motorola"])
        y = np.array(list(listas[i] for i in listas))


        self.grafic.bar(x,y)


    def add_remove(self, user, var):
        if var.get() == 0:
            self.selected_users.remove(user)
        else:
            self.selected_users.append(user)
        if len(self.selected_users) == 0:
            self.listaCli.delete(*self.listaCli.get_children())
        else:
            self.select_list(self.bda.listafiltro(tuple(self.selected_users), self.ordem()))

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
        self.new.resizable(False, False)
        self.new.iconbitmap("2742085.ico")
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

    def open_win2(self):
        self.exp = Toplevel(self.root)
        self.exp.geometry("300x250")
        self.exp.resizable(False, False)
        self.exp.iconbitmap("2742085.ico")
        self.exp.transient(self.root)
        self.exp.focus_force()
        self.exp.grab_set()
        self.labelcar = Label(self.exp , text="SELECIONE O FORMATO A\n SER EXPORTADO", font=('Helvetica 11 bold'))
        self.labelcar.pack(anchor=CENTER, ipady=20)

        combobox = Combobox(self.exp, state= "readonly")
        combobox['values'] = ("xlsx","csv")
        combobox.current(0)
        combobox.pack(padx=20)

        botaoexp = Button(self.exp, text="EXPORTAR", height=2, width=13, command=lambda: [exporta.exp.toxlsx() if combobox.get() == "xlsx" else exporta.exp.tocsv(), self.exp.destroy()])
        botaoexp.pack(anchor=CENTER, pady=30)






    def dropdown(self):
        OPTIONS = [
            "maior valor",
            "menor valor",
        ]


        self.variable = StringVar(self.frame1)
        self.variable.set(OPTIONS[0])  # default value

        self.dropmenu = Combobox(self.frame1, textvariable=self.variable, values=OPTIONS)
        self.dropmenu.pack(side= RIGHT, padx=20)
        self.dropmenu.bind('<<ComboboxSelected>>', lambda x: self.listaCli.delete(*self.listaCli.get_children()) if len(self.selected_users) == 0 else self.select_list(self.bda.listafiltro(tuple(self.selected_users), self.ordem())))

    def ordem(self):
        if self.variable.get() == "maior valor":
            return "DESC"
        else:
            return "ASC"


    def checkbox(self):
        for x in range(len(self.users)):
            self.users_l[x] = IntVar()
            l = Checkbutton(self.frame1, text=self.users[x], variable=self.users_l[x], offvalue=0, bg="#b0afa9", onvalue=1,
                            command=lambda x=self.users[x], y=self.users_l[x]: self.add_remove(x, y))
            l.pack(side= RIGHT)
