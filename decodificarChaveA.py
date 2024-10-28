alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm','n', 
            'o','p','q','r','s','t','u','v','w','x','y','z']

def decifrar_chave(mensagem):
    global alfabeto
        
    for chave in range(1, 26):
        decifrado = ''
        for letra in mensagem:
            if letra in alfabeto:
                posicao = alfabeto.index(letra)
                nova_posicao = (posicao - chave) % 26
                decifrado += alfabeto[nova_posicao]
            else:
                decifrado += letra
        
        print(f'Chave {chave}: {decifrado}')


if __name__ == "__main__":
    decifrar_chave("v")