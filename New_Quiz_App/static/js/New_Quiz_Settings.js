document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('image')
    const fileNameElement = document.getElementById('file-name')
    const previewImage = document.querySelector('.quiz-image-preview')

    if (fileInput && fileNameElement && previewImage) {
        fileInput.addEventListener('change', function () {
            if (fileInput.files.length > 0) {
                const file = fileInput.files[0];
                fileNameElement.textContent = file.name

                const reader = new FileReader();
                reader.onload = function (e) {
                    previewImage.src = e.target.result
                }
                reader.readAsDataURL(file)
            } else {
                fileNameElement.textContent = 'Drop files or click here'
                previewImage.src = "{{ url_for('New_Quiz.static', filename='img/quiz-image-preview.png') }}"
            }
        })
    }
    const quizNameInput = document.getElementById('quiz-name')
    const quizTitle = document.getElementById('quiz-title')

    if (quizNameInput && quizTitle) {
        quizNameInput.addEventListener('input', function () {
            quizTitle.textContent = quizNameInput.value || 'Вікторина з програмування'
        })
    }
})