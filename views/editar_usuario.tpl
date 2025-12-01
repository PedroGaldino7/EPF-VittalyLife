<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/stylePages.css">
    <title>Editar Usuário</title>
</head>
<body>

    <div class="container-page">

    <h1>Editar Usuário</h1>

    <form action="/users/edit/{{user.id}}" method="post">

        <label>Nome:</label>
        <input type="text" name="username" value="{{user.username}}" required>

        <label>Email:</label>
        <input type="email" name="email" value="{{user.email}}" required>

        <label>Senha (opcional):</label>
        <input type="password" name="password" placeholder="Deixe vazio para manter">

        % if logged_user.is_admin:
            <label>Tipo de Usuário:</label>
            <select name="is_admin">
                <option value="false" {{'selected' if not user.is_admin else ''}}>Usuário</option>
                <option value="true" {{'selected' if user.is_admin else ''}}>Administrador</option>
            </select>
        % end

        <button class="btn btn-success" type="submit">Salvar</button>
    </form>

    % if logged_user.id == user.id:
        <a class="btn" href="/dashboard">Voltar</a>
    % else:
        <a class="btn" href="/users">Voltar</a>
    % end

</div>
    
</body>
</html>