$(function() {
    $('.big-choice, .fill-form').click(function() {
        let isBig = $(this).hasClass('big-choice');
        $('.big-choice').toggleClass('active', isBig);
        $('.fill-form').toggleClass('active', !isBig);
        $('.large-selection-view').toggle(isBig);
        $('.fill-form-view').toggle(!isBig);
    });

    $('.ai-icon, .ia-label').click(e => {
        e.preventDefault();
        $('#modalOverlay').addClass('active');
        $('body').css('overflow', 'hidden');
    });

    $('#modalOverlay').click(e => {
        if (e.target !== this) return;
        $('#modalOverlay').removeClass('active');
        $('body').css('overflow', '');
    });

    $(document).keydown(e => {
        if (e.key === 'Escape' && $('#modalOverlay').hasClass('active')) {
            $('#modalOverlay').removeClass('active');
            $('body').css('overflow', '');
        }
    });

    $('.submit-ai-promt-btn').click(() => {
        $('#modalOverlay').removeClass('active');
        $('body').css('overflow', '');
    });

    $('.big-choice').addClass('active');
    $('.fill-form-view').hide();
});