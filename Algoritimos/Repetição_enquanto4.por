programa
{
	inclua biblioteca Matematica
	
	funcao inicio()
	{
		real saldoatual
		real deposito
		real valoratingir
		real taxa

		inteiro mes

		// Taxa média de rendimento da poupança (ao mês)
		taxa = 0.6

		// Declçarando os valores das váriaveis
		saldoatual = 0.0
		mes = 0

		escreva("Informe o valor do depósito a cada mês \n")
		leia (deposito)

		escreva ("Informe o valor que deseja atingir\n")
		leia (valoratingir)

		// Laço que se repete até que o valor desejado seja atingido
		enquanto (saldoatual <= valoratingir){
			//Incremento para contar os meses
			mes = mes + 1

			//Primeiro mês é um calculo 
			se (mes == 1){
				saldoatual = deposito
			}
			//Segundo mes é outro cálcúlo
			senao
			saldoatual = saldoatual + saldoatual * (taxa/100) + deposito
						}
		//Apresentação do resultado na tela
		escreva ("*** Para atingir o valor ", valoratingir, " você levará ", mes, " meses ***\n")
		escreva ("*** Valor atingido: ", Matematica.arredondar(saldoatual,2), " ***\n")
		}
	}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 212; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {saldoatual, 7, 7, 10}-{deposito, 8, 7, 8}-{valoratingir, 9, 7, 12}-{taxa, 10, 7, 4}-{mes, 12, 10, 3};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */