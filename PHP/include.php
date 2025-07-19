<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Inclusão de Arquivos</title>
</head>
<body>
  <?php
    include 'parametros.php';
    include 'funcoes.php';
    
    echo calcularMedia($alunos, "João Paulo")
  ?>
</body>
</html>