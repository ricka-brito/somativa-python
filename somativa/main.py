from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.amazon.com.br/s?bbn=16243890011&rh=n%3A16243890011%2Cp_89%3AXiaomi&dc&qid=1683649219&rnid=18120432011&ref=lp_16243890011_nr_p_89_0")

