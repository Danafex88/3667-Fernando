programa
{
	
	funcao inicio()
	{
		inteiro idade
		inteiro temposervico
		cadeia cargo

		escreva("Quantos anos possui o funcionário? \n")
		leia(idade)

		escreva("Há quantos anos o funcionário trabalha na empresa?\n")
		leia(temposervico)

		escreva("Qual o cargo do funcionário? \n")
		leia(cargo)

		escreva("\n")
		escreva("\n")
		escreva("*** *** *** *** *** *** *** *** *** ***\n")
		escreva("\n")
		escreva("Demonstrativo de Beneficios\n")
		escreva("\n")
		escreva("*** *** *** *** *** *** *** *** *** ***\n")
		escreva("\n")

		se (idade > 30 ou temposervico >= 5){
			escreva("1- O funcionário terá direito à cesta básica\n")
		}
		senao
			escreva("1- O funcionário não terá direito à cesta básica\n")

		se (nao(cargo == "Gerente")){
			escreva("2- O Funcionário terá direito ao convênio médico\n")
					}
		senao
			escreva("2- O funcionário não terá direito ao convênio médico\n")

		se (cargo == "Gerente" e temposervico > 10){
			escreva("3- O funcionário terá direito ao cartão corporativo\n")
		}
		senao
			escreva("3- O funcionário não terá direito ao cartão corporativo\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1096; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */