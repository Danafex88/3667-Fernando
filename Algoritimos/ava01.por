programa
{
	
	funcao inicio()
	{
	real velocidademax
	real velocidadereal
	real diferenca
	real multa
	
	diferenca = 0.0
	multa = 0.0

	escreva("---------------- \n")
	escreva("SISTEMA DE MULTAS \n")
	escreva("---------------- \n")
	escreva("\n")

	escreva("Qual a velocicidade maxima permetida na avenida? \n")
	leia(velocidademax)

	escreva("Qual a velocidade que o usuaruo trafega na via? \n")
	leia(velocidadereal)
	escreva("\n")

	se (velocidadereal > velocidademax)
	{
		diferenca = (velocidadereal - velocidademax)

		se (diferenca <=10)
		{
			multa = 50.0
		}
		se (diferenca >10 e diferenca <=30)
		{
			multa = 100.0
		}
		se (diferenca >30)
		{
			multa =200.0
		}

		escreva ("\n")
		escreva ("--------------------------------------------------------- \n")
		escreva ("Você foi multado!!! \n")
		escreva ("\n")
		escreva ("Por andar a  ", diferenca, "km/h acima do permitido! \n")
		escreva ("O valor da multa será de ", multa, "\n")
		escreva ("--------------------------------------------------------- \n")
		escreva ("\n")
	}
	
	senao
	{
	escreva ("--------------------------------------------------------- \n")
	escreva (" Parabéns!!! \n")
	escreva ("\n")
	escreva ("\n")
	escreva ("Quem anda dentro dos limites respeita a vida \n")
	escreva ("--------------------------------------------------------- \n")
	escreva ("\n")	
	}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1354; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */