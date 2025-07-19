programa
{
	
	funcao inicio()
	{
	inteiro idade
	inteiro tempodeservico

	escreva("********************************************* \n")
	escreva(" SISTEMA - DEPARTAMENTO PESSOAL FACIL \n")
	escreva("********************************************* \n")
	escreva("\n")

	escreva(" Informe quantos anos possui o funcionario: \n")
	leia(idade)

	escreva("Informe quantos anos de serviço possui o funcionario: \n")
	leia(tempodeservico)

	se (idade >= 65 ou tempodeservico >= 30)
	{
		escreva ("")
		escreva (" Requer aposentadoria!")
	}
	senao 
	{
		se( idade >=60 e tempodeservico >=25)
		{
			escreva("\n")
			escreva("Requer aposentadoria \n")
		}
		senao
		escreva("\n")
		escreva("Ainda nao pode se aposentar! \n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 432; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */