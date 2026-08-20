let addBtn = document.querySelectorAll('.add-btn')

addBtn.forEach((btn) => {

    btn.addEventListener('click', (e) => {
        btn.style = 'background-color: transparent;color: #000;border: 1px solid #00e317;'
        btn.textContent = 'Успешно добавлено'
    })

})