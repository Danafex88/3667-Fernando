programa
{
	
	funcao inicio()
	{
		cadeia cupom1
		cadeia cupom2

		real preco_produto
		real desconto

		preco_produto = 200.00

		escreva("Informe o primeiro cupom\n")
		leia(cupom1)

		escreva ("Informe o segundo cupom\n")
		leia(cupom2)

		se (cupom1 == "CP10" e cupom2 == "CP20" ou cupom1 == "CP10" e cupom2 == "CP20" ) {
			desconto = 0.20
			desconto = preco_produto * desconto
			escreva("Produto com desconto maximo:\n", preco_produto - desconto)
		}
		senao se (cupom1 == "CP10" ou cupom1 == "CP20" ou cupom2 == "CP10" ou cupom2 == "CP20"){
			desconto = 0.10
			desconto = preco_produto * desconto
			escreva("Produto com desconto médio:\n", preco_produto - desconto)
					}
		senao
			escreva("Produtos sem desconto:\n", preco_produto)
	}
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 298; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */