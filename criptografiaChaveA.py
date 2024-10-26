alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm','n', 
            'o','p','q','r','s','t','u','v','w','x','y','z']

def criptografia_Letra_A(letra, chave):
  global alfabeto
  
  letra_original = alfabeto.index(letra)
  letra_criptografada = (letra_original + chave) % 26
  criptografia = alfabeto[letra_criptografada]
  print(criptografia)

def criptografia_Mensagem_A(mensagem, chave):
  for letra in mensagem.lower():
    if letra in alfabeto:
      letra_original = alfabeto.index(letra)
      letra_criptografada = (letra_original + chave) % 26
      criptografia = alfabeto[letra_criptografada]
      print(criptografia, end="")
      
    else:
      print(letra, end="")