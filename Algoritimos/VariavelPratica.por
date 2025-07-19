programa
{
	
	funcao inicio()
	{
		real salario
		real comissao
		real desconto
		real resultado

		

		escreva (" Informe o valor do salário: \n")
		leia(salario)

		escreva(" Informe o valor da comissão: \n")
		leia(comissao)

		escreva(" Informe o valor de desconto do salário: \n")
		leia(desconto)

		resultado = salario + comissao - desconto
		escreva("Salário Final: ", resultado, "\n")
		

		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 86; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */