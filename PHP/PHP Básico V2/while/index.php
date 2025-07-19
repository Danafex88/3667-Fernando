<?php
$saldoInicial = 800;
$meta = 2000;
$rendimentoReal = 0.01; // 1% de rendimento real
$mes = 0;
?>
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Investimento</title>
    <!-- Adicione o link do Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <div class="card">
                    <div class="card-body">
                        <h2 class="text-center">Calculadora de Investimento</h2>
                        <p class="text-center">Foram necessários <?php echo $mes; ?> meses para atingir a meta de R$ <?php echo $meta; ?><br> com rendimento real de <?php echo $rendimentoReal * 100; ?>% ao mês.</p>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>

</html>