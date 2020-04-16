$(function () {
    $('#id_konten').summernote();
    $('.switch-input').click(function () {
        var id = $(this).attr('id').replace('id-switch-', '')
            .replace('{', '').replace('}', '');
        var url = '/artikel/comment/' + id;
        $(location).attr('href', url);
    });
});