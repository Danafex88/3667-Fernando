programa
{
	
	funcao inicio()
	{
		real peso

		real pesado
		inteiro pesado_codigo

		real leve
		inteiro leve_codigo
		
	
		peso = 0.0
		pesado = 0.0
		leve= 10000.0

		pesado_codigo = 0
		leve_codigo = 0

	para (inteiro contador=1; contador<=3; contador++)
	{
		escreva( "Entre com o pesa da pessoa #", contador, "\n")
		leia(peso) 

		se (peso < leve)
		{
			leve = peso
			leve_codigo = contador
		}

		se (peso > pesado)
		{
			pesado = peso
			pesado_codigo = contador
		}
	}
	escreva(" A pessoa mais pesada é a  ", pesado_codigo, " com ", pesado, " kg\n")
	escreva(" A pessoa mais leve é a  ", leve_codigo, " com ", leve, " kg\n")
 }
}


	
	
	
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 164; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */