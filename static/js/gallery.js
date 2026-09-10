const imageBoxes = document.querySelectorAll('.image-box')
const galleryModal = document.querySelector('.gallery-modal')
const imageModal = document.querySelector('.image-modal')
const primaryImage = document.querySelector('.image-block img')
const leftArrow = document.querySelector('.arrow:nth-child(2)')
const rightArrow = document.querySelector('.arrow:first-child')

galleryModal.addEventListener('click', e => {
    galleryModal.classList.add('hidden')
})

imageBoxes.forEach(image => {
    image.addEventListener('click', e => {
        primaryImage.setAttribute('src', `${e.target.src}`)
        galleryModal.classList.remove('hidden')
    })
})


imageModal.addEventListener('click', e => {
    e.stopPropagation();
});

leftArrow.addEventListener('click', e => {
    primaryImage.setAttribute('src', '')
})

rightArrow.addEventListener('click', e => {
    primaryImage.setAttribute('src', '')
})
