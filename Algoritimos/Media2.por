programa
{
	
	funcao inicio()
	{
		real n1,n2, n3, n4

		real soma, media

		escreva("Digite a primeira nota: ")
		leia(n1)

		escreva("Digite a segunda nota: ")
		leia(n2)

		escreva("Digite a terceira nota: ")
		leia(n3)

		escreva("Digite a quarta nota: ")
		leia(n4)

		soma = (n1+n2+n3+n4)
		media = (soma/4)
		escreva("A média final do aluno é = ", media, "\n")

		se (media >= 5) {
			escreva ( " O aluno esta aprovado")
				}
				senao 
				escreva( "O aluno esta reprovado")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 483; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {n1, 6, 7, 2}-{n2, 6, 10, 2}-{n3, 6, 14, 2}-{n4, 6, 18, 2}-{soma, 8, 7, 4}-{media, 8, 13, 5};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */