$(function () {
    $('#id_konten').summernote();
    $('.switch-input').click(function () {
        var id = $(this).attr('id').replace('id-switch-', '')
            .replace('{', '').replace('}', '');
        var url = '/artikel/comment/' + id;
        $(location).attr('href', url);
    });
    $('.btn.btn-danger.btn-sm').click(function () {
        var idStr = $(this).attr('id');
        idAll = idStr.replace('btn-delete-', '');
        var idArray = idAll.split('-');
        $('#btn-ok').click(function () {
            var url = '/artikel/delete_komentar/' + idArray[1];
            console.log(url)
            $(location).attr('href', url);
        });
    });
});