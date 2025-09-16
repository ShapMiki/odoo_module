// OWL компонент счётчика, увеличивает значение каждую секунду
import { Component, useState, onMounted, onWillUnmount } from "@odoo/owl";

export class LibraryBookList extends Component {
    setup() {
        this.state = useState({ value: 0 });

        let intervalId = null;

        onMounted(() => {
            intervalId = setInterval(() => {
                this.state.value += 1;
            }, 1000);
        });

        onWillUnmount(() => {
            if (intervalId) {
                clearInterval(intervalId);
            }
        });
    }
}

LibraryBookList.template = "library_book_website.library_book_templates";
