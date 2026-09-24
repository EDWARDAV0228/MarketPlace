let openBtn = document.querySelectorAll('.open-btn');

openBtn.forEach(btn => {
    btn.addEventListener('click', e => {
        const angle = btn.querySelector('.angle')
        if (angle.innerHTML == '<i class="fa-solid fa-angle-right"></i>') {
            angle.innerHTML = '<i class="fa-solid fa-angle-down"></i>'
            angle.parentElement.parentElement.querySelector('.filter-list').classList.remove('hidden')
        } else if (angle.innerHTML == '<i class="fa-solid fa-angle-down"></i>') {
            angle.innerHTML = '<i class="fa-solid fa-angle-right"></i>'
            angle.parentElement.parentElement.querySelector('.filter-list').classList.add('hidden')
        }




    })
});
