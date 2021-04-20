import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = 'https://absolutasaude.com.br/landingpage.php'
# getting the options importeds from firefox(selenium)
# pegando as opções importadas do firefox (selenium) e atribuindo a uma variavel
configOptions = Options()
# esconde o navegador | hidden browser
configOptions.headless = False
# instance of browser, and adding configs created upside this comment.
# instanciando um navegador, adicionando suas configurações, criadas acima...
Browser = webdriver.Firefox(options=configOptions)
# abre o navegador | open browser (mozilla)
Browser.get(url)
time.sleep(10)

elemento = Browser.find_element_by_xpath("//section[@class='second-section']//div")

html_content = elemento.get_attribute('outerHTML')

ParseHTML = BeautifulSoup(html_content, 'html.parser')

structuredData = ParseHTML.find(name="h4")
# dataframer structure
                              # pd learn one string of html, then pass var to string again
dataframe_full = pd.read_html( str(structuredData) )[0] # to limit add : .head(10) <- that's function delimit to 10 objects

dataframe = dataframe_full[['src','text']]
dataframe.columns = ['src','h4']


# Fecha o Navegador
Browser.quit()