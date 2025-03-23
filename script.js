// script.js
document.addEventListener("DOMContentLoaded", function () {
    const startButton = document.querySelector("h2"); // Selects the 'Start >' text

    startButton.addEventListener("click", function () {
        window.location.href = "nextpage.html"; // Change 'nextpage.html' to your desired page
    });
});
