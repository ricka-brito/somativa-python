import mysql.connector
from webscrap import scrap

class bd:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="amazon"
        )
        self.cursor = self.cnx.cursor()
        self.scraper = scrap()

    def listatudo(self):
        self.cursor.execute("SELECT * FROM celulares")
        return self.cursor.fetchall()

    def listafiltro(self, *args):
        if len(args) == 1:
            formatado = "marca = " + str(args).replace(",", "").replace("(", "").replace(")", "")
        else:
            formatado = "marca = " + str(args).replace(",", " OR marca = ").replace("(", "").replace(")", "")

        sql = f"SELECT * FROM celulares WHERE {formatado}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def atualiza(self):
        a = self.scraper.nomesevalores()

        self.cursor.execute("TRUNCATE celulares")

        self.cnx.commit()

        sql = "INSERT INTO celulares (marca, modelo, valor) VALUES (%s, %s, %s)"

        vals = []
        for i in a:
            for j in a[i]:
                vals.append(tuple([i, j, a[i][j]]))

        self.cursor.executemany(sql, vals)

        self.cnx.commit()






