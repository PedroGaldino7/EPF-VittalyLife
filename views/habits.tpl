<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/stylePages.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
    <title>Hábitos</title>
</head>
<body>

    <div class="container-page">
        <h1>Hábitos</h1>
        

        <div class="cards">

        % for h in habits:
        <div class="card" id="card">
            <div class="card-body">
                <h5 class="card-title">{{h["name"]}}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary">{{h["frequency"]}}</h6>
                <p class="card-text">{{h["description"]}}</p>

                % if h["done"]:
                    <p><span style="color: green; font-weight: bold;">Concluído ✓</span></p>
                % else:
                    <p><span style="color: red; font-weight: bold;">Pendente ✗</span></p>
                % end

                <a href="/habits/edit/{{h['id']}}" id="editHabit">Editar</a>

                <form action="/habits/delete/{{h['id']}}" method="post" style="display:inline;">
                    <button type="submit" id="btnExc">Excluir</button>
                </form>
                % if not h["done"]:
                    <form action="/habits/checkin/{{h['id']}}" method="post" style="display:inline;">
                        <button type="submit" id="btnCheckin">Check-in</button>
                    </form>
                % else:
                    <span style="color: #888; font-size: 14px;">✔ Já concluído hoje</span>
                % end
            </div>
        </div>
        % end 
    
        </div>
        
        <a href="/dashboard" id="voltarDash">Voltar para o dashboard</a>
    </div>
<script src="../static/js/main.js"></script>
    
</body>
</html>