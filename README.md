## Cenário – Criptografia

  A **criptografia** refere-se a conversão de dados de um **formato legível em um formato
codificado (criptografado) não legível**. O objetivo de codificar os dados é que, na comunicação entre
usuários e sistemas autorizados, o conteúdo não seja interceptado por terceiros não autorizados
que podem, por exemplo, fazer uso das informações sensíveis as empresas.

  Uma das formas de criptografia é realizar o *deslocamento das posições das letras e,
posteriormente, as suas substituições*. Abaixo um exemplo de deslocamento do alfabeto em 5
posições:

![Cifra de César](https://github.com/user-attachments/assets/3648d43e-f53b-4c37-97bc-ad55939702b0)

A quantidade de posições que o alfabeto é deslocado nessa criptografia é denominada
chave, informação necessária para realizar a conversão do texto para sua compreensão.
A ação de converter o texto codificado em texto legível (decodificado) recebe o nome de decodificação.

Portanto, o texto **“jz frt udymts”** sabendo que a chave é 5, tem-se o texto **“eu amo python”**.

Considerando o funcionamento dessa criptografia, deseja-se implementar um programa em
Python que realize as conversões de um texto legível em um texto criptografado, considerando uma
chave a escolha do usuário (1).

O programa deve ser capaz, também, de decodificar um texto criptografado sabendo a chave
de criptografia informada também pelo usuário (2).
Além disso, o programa deve, ao receber uma mensagem, ser capaz de codificar um texto legível com uma chave aleatória (3) ou decodificar um
texto criptografado descobrindo a sua chave (4).
