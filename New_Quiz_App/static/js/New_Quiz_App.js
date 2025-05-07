$(function () {
    const bigChoiceBtn = $('.big-choice');
    const fillFormBtn = $('.fill-form');
    const largeView = $('.large-selection-view');
    const formView = $('.fill-form-view');
    const modal = $('#modalOverlay');
    const body = $('body');


    bigChoiceBtn.click(function () {
        bigChoiceBtn.addClass('active');
        fillFormBtn.removeClass('active');
        largeView.show();
        formView.hide();
    });

    fillFormBtn.click(function () {
        fillFormBtn.addClass('active');
        bigChoiceBtn.removeClass('active');
        formView.show();
        largeView.hide();
    });


    $('.ai-icon, .ia-label').click(function (e) {
        e.preventDefault();
        modal.addClass('active');
        body.css('overflow', 'hidden');
    });

    modal.click(function (e) {
        if (e.target === modal[0]) {
            modal.removeClass('active');
            body.css('overflow', '');
        }
    });


    $(document).keydown(function (e) {
        if (e.key === 'Escape' && modal.hasClass('active')) {
            modal.removeClass('active');
            body.css('overflow', '');
        }
    });


    $('.submit-ai-promt-btn').click(function () {
        modal.removeClass('active');
        body.css('overflow', '');
    });

    bigChoiceBtn.addClass('active');
    formView.hide();


    $('.scroll-frame').click(function () {
        const questionInput = $('.large-selection-view input[type="text"]')[0];
        const question = questionInput ? questionInput.value : '';
        const answers = [];

        $('.answers-options-frame .answer-container').each(function () {
            const textInput = $(this).find('input[type="text"]')[0];
            const text = textInput ? textInput.value : '';
            const isCorrect = $(this).find('input[type="checkbox"]').is(':checked');
            if (text) {
                answers.push({ text: text, correct: isCorrect });
            }
        });

        $.ajax({
            url: '/save_quiz',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ question: question, answers: answers }),
        });
    });
});