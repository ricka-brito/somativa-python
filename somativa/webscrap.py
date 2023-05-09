from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class scrap:

    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")

        self.marcas = {
            "Xiaomi": "https://www.amazon.com.br/s?i=electronics&bbn=16243890011&rh=n%3A16243890011%2Cp_72%3A17833785011%2Cp_89%3AXiaomi&dc&qid=1683650416&rnid=18120432011&ref=sr_nr_p_89_1&ds=v1%3Aoh3Oyr8%2B0taJp6DxZI3qcGXy634kbIMbDh1RL4jP%2BIQ",
            "Apple": "https://www.amazon.com.br/s?i=electronics&bbn=16243890011&rh=n%3A16243890011%2Cp_72%3A17833785011%2Cp_89%3AApple&dc&ds=v1%3Ash3GBQXMVwPRhym9R460J1FSIYb%2F0bU2cmG3h7BkCZI&qid=1683650440&rnid=18120432011&ref=sr_nr_p_89_2",
            "motorola": "https://www.amazon.com.br/s?i=electronics&bbn=16243890011&rh=n%3A16243890011%2Cp_72%3A17833785011%2Cp_89%3AMotorola&dc&qid=1683650453&rnid=18120432011&ref=sr_nr_p_89_1&ds=v1%3AlHuCkAFvsyup7jeE%2FV4LyIKBdcmxQtlXwet37u%2BtDSc",
            "samsung": "https://www.amazon.com.br/s?i=electronics&bbn=16243890011&rh=n%3A16243890011%2Cp_72%3A17833785011%2Cp_89%3ASAMSUNG&dc&qid=1683650518&rnid=18120432011&ref=sr_nr_p_89_4&ds=v1%3AK1210RQ43Pc2osOqwKyexxBTg26dUxJpknCp41NvwAw",
            "multilaser": "https://www.amazon.com.br/s?i=electronics&bbn=16243890011&rh=n%3A16243890011%2Cp_72%3A17833785011%2Cp_89%3AMultilaser&dc&qid=1683653077&rnid=18120432011&ref=sr_nr_p_89_5&ds=v1%3ASYXG80WDqr6n6edaWjfj%2F3YpHJo1Vb2AL7t7AueVFeE"
        }


    def nomesevalores(self):
        self.navegador = webdriver.Chrome(service=self.servico, options=self.options)

        listas = {
            "Xiaomi": {},
            "Apple": {},
            "motorola": {},
            "samsung": {},
            "multilaser": {},
                  }
        for i in self.marcas:
            self.navegador.get(self.marcas[i])

            for j in range(2, 100):
                try:
                    nome = self.navegador.find_element('xpath', f"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[2]/div[1]/h2/a/span")
                    preco = self.navegador.find_element('xpath', f"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[2]/div[3]/div/div[1]/a/span/span[2]/span[2]")
                except:
                    continue
                if len(listas[i]) == 10:
                    break
                else:
                    formatado = int(preco.text.replace(".", ""))
                    listas[i][nome.text] = formatado
        self.navegador.close()
        self.servico.stop()
        return listas

