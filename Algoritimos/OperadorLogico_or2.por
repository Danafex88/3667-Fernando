programa
{
	
	funcao inicio()
	{
		inteiro idade
		cadeia nome

		escreva("Informe o nome \n")
		leia(nome)

		escreva("Informe a idade \n")
		leia(idade)

		se (idade < 18 ou nome == "Bruno"){
			escreva("Acesso Autorizado")
		}
		senao
		escreva("Acesso Negado ao sistema")
	}
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 174; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {idade, 6, 10, 5}-{nome, 7, 9, 4};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */