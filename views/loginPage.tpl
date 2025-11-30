<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/loginPage.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <title>Login</title>
</head>
<body>

    <div class="wrapper animar">
        <form action="/login" method="post">
            <h1>Login</h1>

            % if defined('error') and error:
            <div class="alert-error">
                {{error}}
            </div>
            % end

            <div class="input-box">
                <input type="email" name="email" placeholder="Email" required>
                <i class='bx bxs-envelope'></i>
            </div>

            <div class="input-box">
                <input type="password" name="password" placeholder="Password" required>
                <i class='bx bxs-lock-alt' ></i>
            </div>

            <div class="remember-forgot">
                <label><input type="checkbox"> Lembre-me</label>
                <a href="">Esqueceu a senha?</a>
            </div>

            <button type="submit" class="btn">Login</button>

            <div class="register-link">
                <p>Não possui uma conta? <a href="/cadPage">Registre-se</a></p>
                <p><a href="/">Voltar</a></p>
            </div>
        </form>
    </div>
    
    <script src="../static/js/scriptLoginPage.js"></script>
</body>
</html>