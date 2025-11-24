let number = document.getElementById("number");
let counter = 0;

setInterval(() => {
    if (counter == 70) {
        clearInterval();
    }else{
        counter += 1;
        number.innerHTML = counter + "%";
    }

}, 42);

const btnUser = document.getElementById("btnUser");
const userDropdown = document.getElementById("userDropdown");

btnUser.addEventListener("click", () => {
    userDropdown.style.display =
        userDropdown.style.display === "block" ? "none" : "block";
});

document.addEventListener("click", (e) => {
    if (!btnUser.contains(e.target) && !userDropdown.contains(e.target)) {
        userDropdown.style.display = "none";
    }
});
