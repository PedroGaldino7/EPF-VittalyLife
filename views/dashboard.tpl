<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
</head>
<body>

    <h1>Dados do login</h1>
    % if user:
        <p>Bem vindo: {{user.username}}</p>
        <p>O seu email é: {{user.email}}</p>
        <p>Sua senha é: {{user.password_hash}}</p>
        <a href="/">Home</a>
    % else:
        <p>Usuário não encontrado</p>
    % end

    
</body>
</html>
