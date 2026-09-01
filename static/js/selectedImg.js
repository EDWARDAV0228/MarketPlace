let fileInput = document.querySelector('#image')
  document.querySelector('.selected-file').textContent = 'пусто'

  fileInput.addEventListener('change', e => {
    const fileName = fileInput.value.split('//').pop()
    document.querySelector('.selected-file').textContent = fileName.slice(12,)
})