<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Séries de Streaming</title>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f8f9fa;
    }

    .serie-card {
        margin-bottom: 20px;
    }

    .serie-image {
        width: 100%;
        max-height: 200px;
        object-fit: cover;
    }
</style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">Séries de Streaming</h1>
        <div class="row">
            <?php
            function filtrar_series($lista_series, $plataforma) {
                $series_filtradas = array();
                foreach ($lista_series as $serie) {
                    if ($serie['plataforma'] == $plataforma) {
                        $series_filtradas[] = $serie;
                    }
                }
                return $series_filtradas;
            }


            $series = array(
                array(
                    "titulo" => "Stranger Things",
                    "plataforma" => "Netflix",
                    "ano_lancamento" => 2016,
                    "genero" => "Ficção científica, Terror",
                    "imagem" => "img/stranger.jpg"
                ),
                array(
                    "titulo" => "The Mandalorian",
                    "plataforma" => "Disney+",
                    "ano_lancamento" => 2019,
                    "genero" => "Ficção científica, Ação",
                    "imagem" => "img/mandalorian.jpg"
                ),
                array(
                    "titulo" => "The Witcher",
                    "plataforma" => "Netflix",
                    "ano_lancamento" => 2019,
                    "genero" => "Fantasia, Ação",
                    "imagem" => "img/witcher.jpg"
                )
            );

            $plataforma_desejada = "Netflix";
            $series_filtradas = filtrar_series($series, $plataforma_desejada);

            foreach ($series_filtradas as $serie) {
                echo "<div class='col-md-4 serie-card'>";
                echo "<div class='card'>";
                echo "<div class='card-header'>" . $serie['titulo'] . "</div>";
                echo "<div class='card-body'>";
                echo "<img src='" . $serie['imagem'] . "' alt='" . $serie['titulo'] . "' class='img-fluid serie-image mb-3'>";
                echo "<p class='font-weight-bold'>" . $serie['titulo'] . "</p>";
                echo "<p>Plataforma: " . $serie['plataforma'] . "</p>";
                echo "<p>Ano de Lançamento: " . $serie['ano_lancamento'] . "</p>";
                echo "<p>Gênero: " . $serie['genero'] . "</p>";
                echo "</div>";
                echo "</div>";
                echo "</div>";
            }
            ?>
        </div>
    </div>
</body>
</html>
