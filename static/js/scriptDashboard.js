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
            e.stopPropagation(); // evita fechar ao clicar no botão
            menu.style.display = menu.style.display === "block" ? "none" : "block";
        });

        // Clicar fora → fecha
        document.addEventListener("click", function () {
            menu.style.display = "none";
        });

        // Evita que clique dentro feche o menu
        menu.addEventListener("click", function (e) {
            e.stopPropagation();
        });
    }

});

