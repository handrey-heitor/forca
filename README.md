# forca

Grupo: Handrey heitor, Izayner Siqueira, Andre cnopca 

Jogo: Jogo da forca

Objetivo: O jogo consiste em adivinhar uma palavra de um dicionário, o jogador tem 5 chances para acertar cada letra 
no campo de espaço determinado pelo tamanho da palavra, se a letra estiver contida na palavra, o campo é preenchido com tal letra. 
Se a letra não estiver contida na palavra, o campo é preenchido com um traço e a cada letra selecionada incorretamente, o jogador perde uma chance.
Quando totalizado 5 erros ou a vida ser igual a 0 o jogo é encerrado e o jogador perde. O mesmo acontece quando o jogador acertar a palavra, pórem conta como vitória.

Regras: O jogador tem 5 vidas, ele deve adivinhar a palavra que o comando selecionou, ao zerar as 5 vidas o jogo é encerrado, o jogador também deve digitar apenas letras,
para ganhar o jogador deve apenas acertar todas as letras da palavra.
 
Entradas/Saídas: O usuario deve fornecer uma letra como entrada, o programa ira verificar se está letra está contida em uma palavra do dicionário.
Caso contida ele preenchera o campo com a letra, caso não ele ira preencher com um traço e exbira a quantidade de vidas restantes.
Se o jogador acertar a palavra o jogo ira exibir uma mensagem de vitória, caso o jogador perca o jogo ira exibir uma mensagem de derrota.
Independe de perder ou ganhar a palavra será exibida no final.

Estrutura do codigo:
 O programa importara palavras de forma randomizada de um dicionário separado, para ser a palavra resposta da forca
 a ferramenta " while true " será utilizada para repetição do código enquanto o break não for ativado
 o " if e else " será utilizado para verificar se a letra digitada pelo usuário está contida na palavra assim como se o usuário acertou ou errou a palavra
 caso esteja, a letra será adicionada ao slot pertencente , caso não, a vida será decrementada e o processo de solicitação de letras irá se repetir até que o jogador acerte a palavra
 ou perca suas vidas
 o lower será utilizado para transformar a letra digitada em minuscula para evitar erros de digitação
 o break será ativado logo após acertar a palavra ou após o jogador perder todas as suas vidas
 O "for __ in __ " para letra contida na palavra":" (if) se a letra estiver na lista para letras aparecerá a letra no lugar do traço.

Exemplo de uso:
(a palavra que o programa escolheu foi "azul"")
_ _ _ _ 
"tente adivinhas uma letra!:"
usuario [a]
a _ _ _
"tente adivinhas uma letra!:"
usuario [e]
"você tem 4 tentativas!"
a _ _ _
"tente adivinhas uma letra!:"
usuario [z]
a z _ _
"tente adivinhas uma letra!:"
usuario [l]
a z _ l
"tente adivinhas uma letra!:"
usuario [u]
"parabéns você ganhou!"
"a palavra era azul"

--------------------------------------------------

caso perca

"você perdeu! a palavra era azul"

Conclusão:
O jogo já está em fase de testes
ele está implementada na IDE VsCode na linguagem python
o jogo ainda não tem interface e não existe uma previsão certa de que será implementada, mas já está em desenvolvimentos
