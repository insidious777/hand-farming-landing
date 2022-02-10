document.addEventListener("DOMContentLoaded", () => {
    new Glider(document.querySelector('.feedback-cards'), {
        slidesToShow: 1,
        dots: '#dots',
        arrows: {
            prev: '.glider-prev',
            next: '.glider-next'
        },
        responsive: [
            {
                breakpoint: 1000,
                settings: {
                    // Set to `auto` and provide item width to adjust to viewport
                    slidesToShow: 3,
                }
            }
            ]
    });
});