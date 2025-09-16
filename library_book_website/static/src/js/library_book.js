console.log("Library Website JS loaded!");

document.addEventListener("DOMContentLoaded", () => {
    console.log("func run")
    const header = document.querySelector(".o_main_nav")
    header.style.setProperty("background-color", "#FF0000", "important")

    setTimeout(() => {
    const cards = document.querySelectorAll(".card-body");
    cards.forEach((card) => {
        let card_texts = document.querySelectorAll(".card-text")
        card_texts.forEach( (text) =>{
            text.style.setProperty("font-size", "20px", "important");
            console.log(text.textContent);
        });
    });
    }, 5000);

});
