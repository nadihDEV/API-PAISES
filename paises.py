import json
import sys

import requests

URL_ALL = "https://restcountries.com/v3.1/all?fields=name,capital,currencies"
URL_NAME = "https://restcountries.com/v3.1/name/"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requisicao em : ", url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print("Erro ao fazer parsing")

def contagem_de_paises(lista_de_paises):
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais[""])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao(URL_NAME + nome_do_pais)
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                print(f"{pais["name"]["common"]} : {pais["population"]} habitantes")
    else:
        print("Pais n encontradp")


def mostrar_moedas(nome_do_pais):
    resposta = requisicao(URL_NAME + nome_do_pais)

    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                nome = pais['name']['common']
                print(f"Moedas do {nome}:")

                moedas = pais.get("currencies", {})

                for codigo_moeda, dados_moeda in moedas.items():
                    nome_moeda = dados_moeda.get("name", "Desconhecido")
                    simbolo = dados_moeda.get("symbol", "")

                    print(f"- {nome_moeda} ({codigo_moeda}) {simbolo}")
        else:
            print("País não encontrado")

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        mostrar_populacao(nome_do_pais)
    except:
        print("E preciso passar o nome do pais")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Bem-Vindo ao Sistema de Paises")
        print("Uso: python paises.py <acao> <nome do pais>")
        print("Acoes disponiveis: contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            numero_de_paises = contagem_de_paises()
            print(f"Existem {numero_de_paises} paises no mundo todo")
        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Argumentos invalido")
