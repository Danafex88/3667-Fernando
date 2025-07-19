<?php
    // define os numeors que serao utilizados 
    $Numero1 = 30;
    $Numero2 = 7;

    //Atribui cada operação a uma variavel propria
    $soma = $Numero1 + $Numero2;
    $subtracao = $Numero1 - $Numero2;
    $mutiplicacao = $Numero1 * $Numero2;
    $divisao = $Numero1 / $Numero2;
    $resto = $Numero1 % $Numero2;
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exemplo de Operadores em PHP</title>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="estilo.css">
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="card-header">
                <h1 class="text-center">Exemplo de Operadores em PHP</h1>
            </div>
            <div class="card-body">
                <?php
                echo "<h3>Operadores Aritméticos:</h3>";
                echo "<p>Soma: $Numero1 + $Numero2 = <span class= 'resultado'>$Soma</span></p>";
                <p>Subtração: Conta = <span class='resultado'></span></p>
                <p>Multiplicação: Numero 01 * Numero 02 = <span class='resultado'>Resultado da multiplicação</span></p>
                <p>Divisão: Numero 01 / Numeoro 02 = <span class='resultado'>Resultado da divisão</span></p>
                <p>Resto da Divisão: Numero 01 % Nu,ero 02 = <span class='resultado'>Resto da divisão</span></p>
                ?>
                
            </div>
            <div class="card-footer text-muted text-center">
                Exemplo desenvolvido por: 
            </div>
        </div>
    </div>
</body>
</html>