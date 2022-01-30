# importar bibliotecas
from bs4 import BeautifulSoup
import requests

# entrar na API de moedas
site = requests.get("https://hgbrasil.com/status/finance")
soup = BeautifulSoup(site.content, "html.parser")

# função para pegar o valor atual do dolar
def pegar_dolar():
    cotacoes = soup.find_all("h3", {"class": "font-weight-normal text-white mb-2"})
    for cotacao in cotacoes:
        dolar = cotacoes[0].get_text()[3:7]
    return f"A cotação atual do dolar é de {dolar} reais!"

# função para pegar o valor atual do euro
def pegar_euro():
    cotacoes = soup.find_all("h3", {"class": "font-weight-normal text-white mb-2"})
    for cotacao in cotacoes:
        euro = cotacoes[1].get_text()[3:7]
    return f"A cotação atual do euro é de {euro} reais!"

# função para pegar o valor atual da libra
def pegar_libra():
    cotacoes = soup.find_all("h3", {"class": "font-weight-normal text-white mb-2"})
    for cotacao in cotacoes:
        libra = cotacoes[2].get_text()[3:7]
    return f"A cotação atual da libra é de {libra} reais!"

# função para pegar o valor atual do iene
def pegar_iene():
    cotacoes = soup.find_all("h3", {"class": "font-weight-normal text-white mb-2"})
    for cotacao in cotacoes:
        iene = cotacoes[6].get_text()[3:7]
    return f"A cotação atual do iene é de {iene} reais!"

# função para pegar o valor atual do bitcoin
def pegar_bitcoin():
    cotacoes = soup.find_all("h3", {"class": "font-weight-normal text-white mb-2"})
    for cotacao in cotacoes:
        bitcoin = cotacoes[11].get_text()
    bitcoin = bitcoin.replace("R$ ", "").replace(" ", "")
    return f"A cotação atual do bitcoin é de {bitcoin} reais!"