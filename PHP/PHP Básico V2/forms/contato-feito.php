<?php
    $status = $_GET['status'];
?>
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Confirmação de Contato</title>
<!-- Inclua o CSS do Bootstrap -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>

<div class="container mt-5">
  <h2 class="mb-4">Confirmação de Contato</h2>
  <?php
    if ($status == "sucesso"){ 
        echo "<div class='alert alert-success' role='alert'>";
        echo "Seu contato foi feito com sucesso!";
        echo "</div>";
    } else {
        echo "<div class='alert alert-danger' role='alert'>";
        echo "Seu contato não foi efetuado, tente novamente... <a href='index.html'>Voltar ao formulário.</a>";
        echo "</div>";
    }
  ?>
</div>

<!-- Inclua o JS do Bootstrap -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

</body>
</html>
