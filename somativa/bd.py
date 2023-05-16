import mysql.connector
from webscrap import scrap

class bd:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="amazon"
            )
            self.cursor = self.cnx.cursor()
        except:
            self.cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            self.cursor = self.cnx.cursor()
            self.cursor.execute("CREATE DATABASE amazon")
            self.cnx.commit()

        self.cursor.execute("SHOW TABLES")

        if 'celulares' in self.cursor.fetchall():
            pass
        else:
            self.cursor.execute("""
            CREATE TABLE `celulares` (
            `idcelulares` int(11) NOT NULL AUTO_INCREMENT,
            `marca` varchar(45) DEFAULT NULL,
            `modelo` varchar(200) DEFAULT NULL,
            `valor` decimal(15,2) DEFAULT NULL,
             PRIMARY KEY (`idcelulares`)
             ) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
            """)
            self.cnx.commit()

        self.scraper = scrap()

    def listatudo(self):
        self.cursor.execute("SELECT marca, modelo, valor FROM amazon.celulares")
        return self.cursor.fetchall()

    def listafiltro(self, args, ordem):
        args = tuple(args)
        if len(args) == 1:
            formatado = "marca = " + str(args).replace(",", "").replace("(", "").replace(")", "")
        else:
            formatado = "marca = " + str(args).replace(",", " OR marca = ").replace("(", "").replace(")", "")

        sql = f"SELECT marca, modelo, valor FROM amazon.celulares WHERE {formatado} ORDER BY valor {ordem}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def atualiza(self):
        a = self.scraper.nomesevalores()

        self.cursor.execute("TRUNCATE amazon.celulares")

        self.cnx.commit()

        sql = "INSERT INTO amazon.celulares (marca, modelo, valor) VALUES (%s, %s, %s)"

        vals = []
        for i in a:
            for j in a[i]:
                vals.append(tuple([i, j, a[i][j]]))

        self.cursor.executemany(sql, vals)

        self.cnx.commit()
