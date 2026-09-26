let imageInput = document.querySelector('#image_inp');
let galleryInput = document.querySelector('#gallery');

document.querySelectorAll('.selected-file').forEach(file => {
  file.textContent = 'пусто';
})

imageInput.addEventListener('change', () => {
  const fileName = imageInput.value.split('//').pop().slice(12,);
  document.querySelector('.selected-file').textContent = fileName
})

galleryInput.addEventListener('change', () => {
  let filesName = '';
  document.querySelectorAll('.selected-file')[1].innerHTML = '';
  for (const file of galleryInput.files) {
    filesName += file.name + ', '
  }
  document.querySelectorAll('.selected-file')[1].innerHTML += filesName.slice(0, -2);
})
