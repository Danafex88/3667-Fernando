programa
{
	inclua biblioteca Matematica
	
	funcao inicio()
	{
		cadeia produto
		real  preco
		cadeia continuar

		//Define o valor da variavel para rodar o laço
		continuar = "S"
		preco = 0.0

		//Enquanto a variavel estiver valendo "S" o calculo se repetirá
		enquanto (continuar == "S")
		{
			escreva("Informe o nome do produto \n")
			leia(produto)

			escreva("Informe o precço do produto \n")
			leia(preco)

			escreva("n")
			escreva("Tabela de preços para:" ,produto)
			escreva("\n")
			
		}
		para (inteiro ccontador=1; contador<=10; contador++)
		{
			escreva ( "Valor de ", contador, " unidade(s):", Matematica.arredondar(preco * contador, 2), "\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 566; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */