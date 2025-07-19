programa
{
	
	funcao inicio()
	{
		caracter aplicativo
		
		escreva(" Informe o programa que deseja: '1' para Netflix, '2' para Youtube, '3' para Instagram\n")
		leia(aplicativo)

		escolha (aplicativo)
		{
			caso '1':
			escreva( " Abrindo programa", aplicativo)
			pare

			caso '2':
			escreva("Abrindo programa", aplicativo)
			pare

			caso '3':
			escreva("Abrindo programa", aplicativo)
			pare

			caso contrario:
			escreva("Desculpe, não temos o programa ", aplicativo, " disponivel no momento")
		}
			
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 472; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */