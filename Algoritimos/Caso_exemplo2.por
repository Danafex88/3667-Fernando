programa
{
	
	funcao inicio()
	{
		caracter uf 
		
		escreva("Entre como o UF do cliente: Digite 'P' para PR - 'M' para MG - 'S' para SP \n")
		leia(uf)

		escolha (uf)
		{
			caso 'P':
			escreva(" Cliente Paranaense")
			pare

			caso 'M':
			escreva ("Cliente Mineiro")
			pare

			caso 'S':
			escreva("Cliente Paulista")
			pare

			caso contrario:
			escreva("UF inválida")
			pare
						
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 49; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */