programa
{
	
	funcao inicio()
	{
		inteiro tijolos
		inteiro metros

		metros = 0

		escreva(" Informe o numero total de tijolos \n")
		leia(tijolos)

		se (tijolos <32)
		{
			escreva( "Tijolos insufcientes! \n")
		}
		enquanto (tijolos >= 32)
		{
			metros = metros  + 1
			tijolos = tijolos - 32

			escreva("*** Já construimos ", metros, "m² de muro e ainda restam: ", tijolos, " tijolos*** \n")  
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 404; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */