document.addEventListener("DOMContentLoaded", function() {
    let number = document.getElementById("number");
    let circle = document.querySelector("circle");
    
    let valorFinal = document.getElementById("progressoReal").value;
    valorFinal = parseInt(valorFinal); 
    let counter = 0;
    
    const circumference = 691; 
    
    circle.style.strokeDashoffset = circumference;

    if (valorFinal === 0) {
        number.innerHTML = "0%";
        return;
    }

    let interval = setInterval(() => {
        if (counter >= valorFinal) {
            clearInterval(interval);
        } else {
            counter += 1;
            number.innerHTML = counter + "%";
            
            const offset = circumference - (valorFinal * circumference) / 100;
            
            circle.style.transition = "stroke-dashoffset 2s ease-in-out";
            circle.style.strokeDashoffset = offset;
        }
    }, 20);
});

document.addEventListener("DOMContentLoaded", function () {

    const trigger = document.getElementById("btnUser");
    const menu = document.getElementById("userDropdown");

    if (trigger && menu) {

        trigger.addEventListener("click", function (e) {
            e.stopPropagation();
            menu.style.display = menu.style.display === "block" ? "none" : "block";
        });

        document.addEventListener("click", function () {
            menu.style.display = "none";
        });

        menu.addEventListener("click", function (e) {
            e.stopPropagation();
        });
    }

});

document.addEventListener("DOMContentLoaded", function () {

    let progresso = parseInt(document.getElementById("progressoReal").value);
    let mensagem = document.getElementById("mensagemMotivacional");

    function gerarMensagem(p) {
        if (p === 0) {
            return "Comece sua jornada! O primeiro passo é o mais importante.";
        }
        if (p > 0 && p < 30) {
            return "Ótimo início! Continue avançando!";
        }
        if (p >= 30 && p < 50) {
            return "Boa! Você está indo muito bem!";
        }
        if (p >= 50 && p < 80) {
            return "Parabéns! Você chegou na metade dos desafios de hoje, não é hora de parar ❤️";
        }
        if (p >= 80 && p < 100) {
            return "Quase lá! Só mais um pouco, você consegue!";
        }
        if (p === 100) {
            return "INCRÍVEL! 🔥 Você completou tudo hoje, muito orgulho!";
        }
    }

    mensagem.textContent = gerarMensagem(progresso);

});
