document.addEventListener("DOMContentLoaded", () => {
    console.log('event added');
    const label = document.querySelector('#check-label');

    label.addEventListener('click',()=>{
        const input = document.querySelector('#check');
        const closeButton = document.querySelector('.menu-close');
        const openButton = document.querySelector('.menu-open');

        if(input.checked){
            openButton.style.display = "block";
            closeButton.style.display = "none";
        }else {
            openButton.style.display = "none";
            closeButton.style.display = "block";
        }
    })
})
