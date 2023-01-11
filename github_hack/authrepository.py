import requests
import json

class AuthRepository():
    def __init__(self, usuario, token):
            self._usuario = usuario
            self._token = token

    def request(self):
        resposta = requests.get('https://api.github.com/search/repositories?q=github+api',
                                auth=(self._usuario, self._token))
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        dados_api = self.request()
        print(dados_api)



user = input('Digite o seu usuário!:\n')
print('Resgate seu token aqui: https://github.com/settings/apps')
token = input('Digite o seu token!:\n')


