# Giselle Aki
# Luis Henrique
# Lucas Lima
# Gustavo Kenzo

import random
from criptografiaChave import criptografia_Mensagem, criptografia_Letra
from criptografiaChaveA import criptografia_Letra_A, criptografia_Mensagem_A 
from decodificarChave import decodificar_Letra, decodificar_Mensagem
from decodificarChaveA import decifrar_chave


def continuar():
    continuar = input("\nVocê deseja continuar? (S/N): ").strip()[0].upper()
    if continuar not in ['S', 'N']:
      print("Opção inválidada!", end="")
      continuar = input("Você deseja continuar? (S/N): ").strip()[0].upper()
    elif continuar == 'S':
      return
    else:
      quit("Saindo do programa...")

while True:
    print(f'\nCriptografia Tech')
    print('''Opções: 
    [ 1 ] Criptografar Mensagem (com chave)
    [ 2 ] Decodificar Mensagem (com chave)
    [ 3 ] Criptografar Mensagem (sem chave)
    [ 4 ] Decodificar Mensagem (sem chave)
    [ 5 ] Sair''')

    opcao = int(input('Escolha a opção: '))
    if opcao not in range(1,6):
      print('Opçõa inválida, tente novamente')
      continue
    if opcao == 5:
        print("Saindo do programa...")
        break
    elif opcao == 1:
        tipo = str(input('Você quer codificar letra ou mansagem [L/M]? ')).strip()[0].upper()
        if tipo not in ['L', 'M']:
          print("Opção inválida, tente novamente: ")
          continue
        elif tipo == 'L':
          letra = str(input('Me fale qual vai ser a letra: '))
          chave = int(input('Digite a chave: '))
          criptografia_Letra(letra, chave)
          continuar()
        else:
          mensagem = str(input('Me fale sua mensagem: '))
          chave = int(input('Qual é sua chave: '))
          print("Mensagem Original: " + mensagem)
          print("Mensagem Criptografada: ", end="")
          criptografia_Mensagem(mensagem, chave)
          continuar()
          print("\n")
    elif opcao == 2:
        tipo = str(input('Você quer decodificar uma letra ou mansagem [L/M]? ')).strip()[0].upper()
        if tipo not in ['L', 'M']:
          print("Opção inválida, tente novamente: ")
          continue
        elif tipo == 'L':
          letra = str(input('Me fale qual vai ser a letra: '))
          chave = int(input('Digite a chave: '))
          decodificar_Letra(letra, chave)
          continuar()
        else:
          mensagem = str(input('Me fale sua mensagem: '))
          chave = int(input('Qual é sua chave: '))
          print("Mensagem Criptografada: " + mensagem)
          print("Mensagem Descriptografada: ", end="")
          decodificar_Mensagem(mensagem, chave)
          continuar()
          print("\n")
    elif opcao == 3:
        tipo = str(input('Você quer codificar uma letra ou mansagem [L/M]? ')).strip()[0].upper()
        if tipo.upper() not in ['L', 'M']:
            print("Opção inválida, tente novamente: ")
            continue
        elif tipo == 'L':
          letra = str(input('Me fale qual vai ser a letra: ')).strip().lower()
          chave = random.randint(0,25)
          print("Letra Original: " + letra)
          print("A chave é: ", chave)
          print("Letra Criptografada: ", end="")
          criptografia_Letra_A(letra,chave)
          continuar()
        elif tipo == 'M':
          mensagem = str(input('Me fale a mensagem: '))
          chave = random.randint(0,25)
          print("Mensagem Original: " + mensagem)
          print("A chave é: ", chave)
          print("Mensagem Criptografada: ", end="")
          criptografia_Mensagem_A(mensagem,chave)
          continuar()
          print("\n")
    elif opcao == 4:
      mensagem = str(input('Me fale a mensagem: '))
      decifrar_chave(mensagem.lower())
      print()
      continuar()
