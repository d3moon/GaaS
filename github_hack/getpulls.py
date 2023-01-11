import requests
import json

class GetPulls():
    def __init__(self, owner, repo):
            self._owner = owner
            self._repo = repo

    def request_pull(self):
        resposta = requests.get(
            f'https://api.github.com/repos/{self._owner}/{self._repo}/pulls')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def request_changes(self):
        resposta = requests.get(
            f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code


    def code_review(self):
        resposta = requests.post(
            f'https://api.github.com/repos/repos/{owner}/{repo}/pulls/{pull_number}/{review_id}/events',
                data = review
            )
        if resposta.status_code == 200:
            return resposta.status_code
        else:
            return print('APROVADO!')

    def print_pull(self):
        pull = self.request_pull()
        if type(pull) is not int:
            for i in range(len(pull)):
                print('name: {}'.format(pull[i]['title']))
                print('url: {}'.format(pull[i]['url']))
        else:
            print('PR não aberta')

    def print_request_review(self):
        reviewers = self.request_changes()
        print('Copie esse ID para fazer code-review: {}'.format(reviewers['users']))

owner = input('Digite o dono do repositório!:\n')
repo = input('Digite o repositório!:\n')
pull_number = int(input('Digite o número da PR!:\n'))

pulls = GetPulls(owner, repo)
pulls.print_pull()
pulls.print_request_review()

review_id = input('Digite o ID do code review!:\n')
review = input('Faça o seu review! [APPROVE, REQUEST_CHANGES, COMMENT]:\n')

pulls.code_review()

