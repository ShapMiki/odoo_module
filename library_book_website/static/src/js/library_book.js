
// Lazy Loading для изображений
const lazyLoadImages = () => {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy-image');
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => {
            img.classList.add('lazy-image');
            imageObserver.observe(img);
        });
    } else {
        // Fallback для старых браузеров
        images.forEach(img => {
            img.src = img.dataset.src;
            img.classList.add('loaded');
        });
    }
};

// Оптимизация производительности
const optimizePerformance = () => {
    // Debounce для scroll событий
    let scrollTimeout;
    const handleScroll = () => {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(() => {
            // Логика для scroll событий
        }, 100);
    };

    // Throttle для resize событий
    let resizeTimeout;
    const handleResize = () => {
        if (resizeTimeout) {
            clearTimeout(resizeTimeout);
        }
        resizeTimeout = setTimeout(() => {
            // Логика для resize событий
        }, 250);
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    window.addEventListener('resize', handleResize, { passive: true });
};

// SEO оптимизации
const seoOptimizations = () => {
    // Добавляем structured data для книг
    const books = document.querySelectorAll('.card');
    books.forEach((book, index) => {
        const title = book.querySelector('.card-title a')?.textContent;
        const author = book.querySelector('strong:contains("Автор")')?.nextSibling?.textContent?.trim();
        
        if (title && author) {
            const structuredData = {
                "@context": "https://schema.org",
                "@type": "Book",
                "name": title,
                "author": {
                    "@type": "Person",
                    "name": author
                }
            };
            
            // Добавляем microdata атрибуты
            book.setAttribute('itemscope', '');
            book.setAttribute('itemtype', 'https://schema.org/Book');
            
            const titleElement = book.querySelector('.card-title a');
            if (titleElement) {
                titleElement.setAttribute('itemprop', 'name');
            }
        }
    });
};

// Preload критических ресурсов
const preloadCriticalResources = () => {
    const criticalCSS = document.createElement('link');
    criticalCSS.rel = 'preload';
    criticalCSS.as = 'style';
    criticalCSS.href = '/library_book_website/static/src/css/library_book.scss';
    document.head.appendChild(criticalCSS);
};

// Основная функция инициализации
const start = () => {
    console.log("Library Website JS loaded and running");
    
    // Инициализируем все оптимизации
    lazyLoadImages();
    optimizePerformance();
    seoOptimizations();
    preloadCriticalResources();
    
    setTimeout(() => {
        // Website header (frontend) uses .o_header_affix .navbar or #top .navbar
        const header = document.querySelector("header#top .navbar, .o_header_affix .navbar, .o_main_navbar");
        if (header) {
            header.style.setProperty("background", "linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "important");
            console.log("Header color updated with gradient");
        } else {
            console.log("Header element not found");
        }
    }, 1000);
};

// Инициализация
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
} else {
    start();
}
