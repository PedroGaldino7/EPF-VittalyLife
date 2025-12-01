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