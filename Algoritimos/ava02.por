programa
{
	
	funcao inicio()
	{
		inteiro contador
		real somapeso
		real pesomaior
		real pesomenor
		real peso
		
		pesomenor = 99999.0
		pesomaior = 0.0
		somapeso = 0.0
		
		escreva ("---------------------------------------- \n")
		escreva (" COOPERATIVA NETUNO PESCAS \n")
		escreva ("---------------------------------------- \n")
		escreva ("\n")
		
		para ( contador = 1; contador <=3; contador  ++)
		{
			escreva (" Informe o peso do ", contador  , " º peixe : \n")
			leia (peso)
			
			se (peso > pesomaior)
			{
				pesomaior = peso 
			}
			
			se (peso < pesomenor)
			{
				pesomenor = peso
			}
				somapeso = somapeso + peso
			}
			escreva ("\n") 
			escreva ("---------------------------------------- \n")
			escreva ("RESUMO DA PESCARIA \n")
			escreva ("---------------------------------------- \n")
			escreva ("\n")
			escreva ( " Ótima pescaria João! \n")
			escreva (" A média de peso dos peixes foi de: ", somapeso / 3, "kg \n")
			escreva (" O menor peixe pesou: ", pesomenor, "kg \n")
			escreva (" O maior peixe pesou: ", pesomaior, "kg \n")
			escreva ("\n")
			escreva ("---------------------------------------- \n")
		}
	}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 633; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */