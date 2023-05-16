import pandas as pd
import openpyxl
import bd




class exp:

    @staticmethod
    def toxlsx():
        bda = bd.bd()
        d = bda.listatudo()
        df = pd.DataFrame(d, columns=["marca", "modelo", "valor"])
        df.to_excel('celulares.xlsx', index=False, header=True)

    @staticmethod
    def tocsv():
        bda = bd.bd()
        d = bda.listatudo()
        df = pd.DataFrame(d, columns=["marca", "modelo", "valor"])
        df.to_csv('celulares.csv', sep=';', encoding='utf-8', index=False)

