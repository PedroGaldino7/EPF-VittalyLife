<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/stylePages.css">
    <title>Editar Hábito</title>
</head>
<body>
    
<div class="container-page">

    <h1>Editar Hábito</h1>

    <form action="/habits/edit/{{habit.id}}" method="post">

        <label>Nome:</label>
        <input type="text" name="name" value="{{habit.name}}" required>

        <label>Descrição:</label>
        <textarea name="description" required>{{habit.description}}</textarea>

        <label>Frequência:</label>
        <select name="frequency" required>
            % for f in ['Diario', 'Semanal', 'Quinzenal', 'Mensal', 'Bimestral', 'Trimestral', 'Semestral', 'Anual']:
                <option value="{{f}}" {{ 'selected' if habit.frequency == f else '' }}>
                    {{
                        'Diário' if f == 'Diario' else
                        'Semanal' if f == 'Semanal' else
                        'Quinzenal' if f == 'Quinzenal' else
                        'Mensal' if f == 'Mensal' else
                        'Bimestral' if f == 'Bimestral' else
                        'Trimestral' if f == 'Trimestral' else
                        'Semestral' if f == 'Semestral' else
                        'Anual'
                    }}
                </option>
            % end
        </select>

        <button class="btn btn-success" type="submit">Salvar Alterações</button>
    </form>

    <br>
    <a class="btn" href="/dashboard">Voltar</a>

</div>

</body>
</html>