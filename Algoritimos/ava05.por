programa
{
	
	funcao inicio()
	{
		real peso
		real altura
		real imc

		escreva("------------------------------------------------ \n")
		escreva(" CALCULO DO IMC \n")
		escreva("------------------------------------------------ \n")
		escreva("\n")
		

		escreva("Informe o seu peso em Kg: \n")
		leia (peso)
		
		escreva (" Informe a sua altura em metros \n")
		leia(altura)

		imc= peso / (altura*altura)

		escreva("\n")
		escreva("------------------------------------------------ \n")
		escreva(" Resultado \n")
		escreva("------------------------------------------------ \n")
		escreva("\n")

		escreva(" Seu IMC é de: \n", imc)

		se(imc < 18.5)
		
		{
			escreva("\n")
			escreva( "Classificação: Abaixo do peso")
		}

		se (imc >= 18.5 e imc <= 24.9)
		
		{
			escreva("\n")
			escreva("Classificação: Sobrepeso")
			
		}
		
		se (imc >= 30 e imc <=34.9)
		
		{
			escreva("\n")
			escreva(" Classificação: Obesidade grau I")
		}

		se (imc >= 35 e imc <= 39.9)
		
		{
			escreva("\n")
			escreva(" Classificação: Obesidade grau II")
		}

		se (imc >= 40)
		
		{
			escreva("\n")
			escreva(" Classificação: Obesidade grau III")
		}

		
		escreva("\n")
		escreva("------------------------------------------------ \n")
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 70; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */