<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/stylePages.css">
    <title>Criar Usuário</title>
</head>
<body>

    <div class="container-page">

    <h1>Criar Novo Usuário</h1>

    <form action="/users/add" method="post">

        <label>Nome:</label>
        <input type="text" name="username" required>

        <label>Email:</label>
        <input type="email" name="email" required>

        <label>Senha:</label>
        <input type="password" name="password" required>

        <label>Tipo de Usuário:</label>
        <select name="is_admin">
            <option value="false">Usuário Comum</option>
            <option value="true">Administrador</option>
        </select>

        <button class="btn btn-success" type="submit">Criar</button>
    </form>

    <a class="btn" href="/users">Voltar</a>

</div>
    
</body>
</html>