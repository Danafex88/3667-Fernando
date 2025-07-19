<?php
    // Variavel do tipo string. Ela aceita uma seri de caracteres, seu valor deve ser informado entre aspas.
    $nome = "Diogo Tavares";
    $curso = "PHP Básico";

    //Variavel tipo float, ela aceita numero decimais, recomendada para ser trabalhada como moeda.
    $mensalidade = 124.90;

    // Variavel do tipo inteiro, nao aceita numeros decimais
    $aulas = 10;
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Variáveis</title>
</head>
<body>
    <h1>Olá, <?php echo $nome; ?></h1>
    <h2>você esta matriculado no curso de <?php echo $curso; ?>, sua mensalidade é de: R$ <?php echo $mensalidade ?> e você ainda tem <?php echo $aulas; ?> aulas restantes.</h2>
</body>
</html>