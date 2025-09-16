
const start = () => {
    console.log("Library Website JS loaded and running");
    setTimeout(() => {
        // Website header (frontend) uses .o_header_affix .navbar or #top .navbar
        const header = document.querySelector("header#top .navbar, .o_header_affix .navbar, .o_main_navbar");
        if (header) {
            header.style.setProperty("background-color", "#FF0000", "important");
            console.log("Header color updated");
        } else {
            console.log("Header element not found");
        }
    }, 1000);

};

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
} else {
    start();
}
