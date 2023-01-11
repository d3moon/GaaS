from art import text2art

Art = text2art("Github as a Service")
print(Art)

print('Buscas de repositórios [1]')
print('Buscas de pull requests [2]')
print('Autenticação (SÓ PARA CONTAS PRIVADAS) [3]\n')

question = int(input('Escolha uma opção:'))

if question == 1:
    import getrepository
    getrepository()
elif question == 2:
    import getpulls
    getpulls()
elif question == 3:
    import authrepository
    authrepository()
