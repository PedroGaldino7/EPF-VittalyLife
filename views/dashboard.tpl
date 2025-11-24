<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/styleDashboard.css">
    
    <title>Dashboard</title>
</head>
<body>

    <header>
        <div class="logoDiv">
            <p class="logo"><a href="">VittalyLife</a></p>
        </div>
        <div class="loginDiv">
        % if user:

            <button class="botaoLogin" id="btnUser">
                Bem vindo: {{user.username}}
            </button>

            <div class="dropdownMenu" id="userDropdown">
                <a href="/users/edit/{{user.id}}">Alterar dados</a>
                <a href="/logout">Sair</a>
            </div>
            
        % else:
            <button class="botaoLogin"><a href="/login">Login</a></button>
        % end
        </div>
    </header>

    <section>
        <div class="leftDiv">
            <div class="streakDiv">
                <div class="imgStreak">
                    <div class="skill">
                        <div class="outer">
                            <div class="inner">
                                <div id="number">
                    
                                </div>
                            </div>
                        </div>

                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="240px" height="240px">
                    <defs>
                        <linearGradient id="GradientColor">
                            <stop offset="0%" stop-color="#FFD93D" />
                            <stop offset="100%" stop-color="#FF6B00" />
                            </linearGradient>
                    </defs>
                <circle cx="120" cy="120" r="110" stroke-linecap="round" />
                </svg>
                    </div>


                </div>
                <div class="fraseStreak">
                    <p>Vamos lá, você está quase completando a ofensiva, força !!</p>
                </div>
            </div>
            <div class="taskPendenteDiv">
                <div class="cardTaskPendente">Tomar 2L de água</div>
                <div class="cardTaskPendente">Meditar 30min</div>
                <div class="cardTaskPendente">Ler 10 capítulos da Biblia</div>
                <div class="cardTaskPendente">Ler 10 capítulos da Biblia</div>
            </div>
        </div>
        <div class="rightDiv">
            <div class="menuDivRight">
                <div class="opcDivRight"><a href="habits">Listar todas as tarefas</a></div>
                <div class="opcDivRight"><a href="habits/add">Criar tarefas</a></div>
                <div class="opcDivRight"><a href="desempenho.html">Gráficos de desempenho</a></div>
                <div class="opcDivRight">Configurações da conta</div>
            </div>
        </div>
    </section>

    <footer>

    </footer>

    <script src="../static/js/scriptDashboard.js"></script>
</body>
</html>