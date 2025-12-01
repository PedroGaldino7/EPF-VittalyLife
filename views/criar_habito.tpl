<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/stylePages.css">
    <title>Criar Hábito</title>
</head>
<body>
    
    <div class="container-page">

    <h1>Criar Novo Hábito</h1>

    <form action="/habits/add" method="post">

        <label>Nome:</label>
        <input type="text" name="name" required>

        <label>Descrição:</label>
        <textarea name="description" required></textarea>

        <label>Frequência:</label>
        <select name="frequency" required>
            <option value="Diario">Diário</option>
            <option value="Semanal">Semanal</option>
            <option value="Quinzenal">Quinzenal</option>
            <option value="Mensal">Mensal</option>
            <option value="Bimestral">Bimestral</option>
            <option value="Trimestral">Trimestral</option>
            <option value="Semestral">Semestral</option>
            <option value="Anual">Anual</option>
        </select>

        <button class="btn btn-success" type="submit">Criar Hábito</button>
    </form>

    <br>
    <a class="btn" href="/dashboard">Voltar</a>

</div>

</body>
</html>