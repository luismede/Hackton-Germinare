alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm','n', 
            'o','p','q','r','s','t','u','v','w','x','y','z']

def decodificar_Mensagem(mensagem, chave):
  for letra in mensagem.lower():
    if letra in alfabeto:
      letra_criptografada = alfabeto.index(letra)
      letra_original = (letra_criptografada - chave) % 26
      decodificar = alfabeto[letra_original]
      print(decodificar, end="")
    else:
      print(letra, end="")
      
def decodificar_Letra(letra, chave):
  global alfabeto
  
  letra_criptografada = alfabeto.index(letra.lower())
  letra_original = (letra_criptografada - chave) % 26
  decodificar = alfabeto[letra_original]
  print("Letra criptografada: " + letra)
  print("Letra descriptografada: " + decodificar)
  
if __name__ == "__main__":
  decodificar_Letra("A", 5)