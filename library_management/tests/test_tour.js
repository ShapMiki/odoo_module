odoo.define('library_management.tour_library_book', function (require) {
    "use strict";

    const Tour = require('web_tour.tour');

    Tour.register('library_book_tour', {
        test: true,
        url: '/web',
    }, [
        {
            content: "Ожидаем главный экран",
            trigger: '.o_app[data-menu-xmlid="library_management.menu_root"]',
        },
        {
            content: "Открываем приложение Библиотека",
            trigger: '.o_app[data-menu-xmlid="library_management.menu_root"]',
            run: 'click',
        },
        {
            content: "Открываем меню Книги",
            trigger: '.o_menu_item[data-menu-xmlid="library_management.menu_library_book"]',
            run: 'click',
        },
        {
            content: "Ожидаем список книг",
            trigger: '.o_list_button_add',  // кнопка "Создать" в списке
        },
        {
            content: "Нажимаем Создать",
            trigger: '.o_list_button_add',
            run: 'click',
        },
        {
            content: "Ожидаем форму создания книги",
            trigger: 'input[name="title"]',  // поле Название книги
        },
    ]);
});