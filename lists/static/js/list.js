window.Superlists = {};
window.Superlists.initialize = function () {
    $('value').hide();
    $('input[name="text"]').on('keypress', function() {
        $('.has-error').hide();
    });
};
