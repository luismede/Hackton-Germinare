alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm','n', 
            'o','p','q','r','s','t','u','v','w','x','y','z']

def criptografia_Mensagem(mensagem, chave):
  global alfabeto
  
  for letra in mensagem.lower():
    if letra in alfabeto:
      letra_original = alfabeto.index(letra)
      letra_criptografada = (letra_original + chave) % 26
      criptografia = alfabeto[letra_criptografada]
      print(criptografia, end="")
    else:
      print(letra, end="")
      

def criptografia_Letra(letra, chave):
  global alfabeto
  
  letra_original = alfabeto.index(letra)
  letra_criptografada = (letra_original + chave) % 26
  criptografia = alfabeto[letra_criptografada]
  print("Letra original: " + letra)
  print("Letra criptografada: " + criptografia)
  
if __name__ == "__main__":
  criptografia_Mensagem("Hello World", 5)