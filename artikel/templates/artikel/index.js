$(function () {
    $('.btn.btn-danger.btn-sm').click(function () {
        var idStr = $(this).attr('id');
        id = idStr.replace('btn-delete-', '');
        $('#btn-ok').click(function () {
            var url = '/artikel/delete/' + id;
            $(location).attr('href', url);
        });
    });

});