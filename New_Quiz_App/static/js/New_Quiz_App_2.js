$(document).ready(function() {
    $('.big-choice').click(function() {
        window.location.href = '/new-quiz';
    });

    $('.fill-form').click(function() {
        window.location.href = '/new-quiz-2';
    });

    const $modalOverlay = $('#modalOverlay');
    const $body = $('body');

    function closeModalWindow() {
        $modalOverlay.removeClass('active');
        $body.css('overflow', '');
    }

    $('.ai-icon').click(function(e) {
        e.preventDefault();
        $modalOverlay.addClass('active');
        $body.css('overflow', 'hidden');
    });

    $modalOverlay.click(function(e) {
        if (e.target === this) {
            closeModalWindow();
        }
    });

    $(document).keydown(function(e) {
        if (e.key === 'Escape' && $modalOverlay.hasClass('active')) {
            closeModalWindow();
        }
    });

    $('.submit-ai-promt-btn').click(function() {
        closeModalWindow();
    });
});
