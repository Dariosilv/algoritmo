def verificar_perticipacao_crime():
    pontuacao = 0
    print("Responda as perguntas com 'sim' ou 'Não'")
    if input("Telefou para a vitima ?") == 'sim':
        pontuacao += 1
    if input("Esteve no local do Crime?") == 'sim':
        pontuacao += 1
    if input("Mora perto da Vitima?") == 'sim':
        pontuacao += 1
    if input("Devia para a vitima?") == 'sim':
        pontuacao += 1
    if input("Já trabalhou com a vitima?") == 'sim':
        pontuacao += 1

    print('')
    if pontuacao == 2:
        print("Suspeita")
    elif 3 <= pontuacao <= 4:
        print("Cumplice")
    elif pontuacao == 5:
        print("Assassino")
    else:
        print("Inocente")

verificar_perticipacao_crime()

