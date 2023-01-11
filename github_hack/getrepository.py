import requests
import json

class GetRepository():

    def __init__(self, usuario):
        self._usuario = usuario

    def request(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        dados_api = self.request()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)

user = input('Digite o seu usuário!:\n')
repositorios = GetRepository(user)
repositorios.imprime_repositorios()