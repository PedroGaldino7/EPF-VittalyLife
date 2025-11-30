<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Ops! Algo deu errado</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding: 50px;
            background: #f0f2f5;
            color: #333;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: 0 auto;
        }
        h1 {
            font-size: 80px;
            margin: 0;
            color: #e74c3c;
        }
        h2 {
            margin-top: 10px;
            color: #555;
        }
        p {
            color: #777;
            font-size: 18px;
        }
        .btn {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            background: #3498db;
            color: white;
            padding: 12px 25px;
            border-radius: 25px;
            font-weight: bold;
            transition: 0.3s;
        }
        .btn:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{error.status_code}}</h1>
        <h2>Ops! Parece que tivemos um problema.</h2>
        <p>{{error.body}}</p>
        
        <a href="/dashboard" class="btn">Voltar para o Dashboard</a>
    </div>
</body>
</html>