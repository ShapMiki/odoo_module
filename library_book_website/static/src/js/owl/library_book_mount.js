import { mount, whenReady } from "@odoo/owl";
import { LibraryBookList } from "./library_book_owl";

const mountOwl = async () => {
    const el = document.querySelector("#library-book-owl");
    if (el) {
        await mount(LibraryBookList, { target: el });
        console.log("OWL mounted on #library-book-owl");
    } else {
        console.log("OWL mount target #library-book-owl not found on page");
    }
};

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountOwl);
} else {
    // In Odoo assets scripts may be deferred; run immediately if DOM is already ready
    whenReady(mountOwl);
}