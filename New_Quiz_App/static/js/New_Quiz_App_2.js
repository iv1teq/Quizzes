document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.big-choice').onclick = function() {
        location.href = '/new-quiz';
    };

    document.querySelector('.fill-form').onclick = function() {
        location.href = '/new-quiz-2';
    };
});