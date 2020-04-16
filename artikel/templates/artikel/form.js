$(function () {
    $('#id_konten').summernote({
        placeholder: 'Deskripsi isi artikel.',
        tabsize: 2,
        height: 350
    });
    $('#ikon').change(function (evt) {
        console.clear();
        var filename = evt.target.files[0];
        var output = $('#img-ikon');
        output.width(150);
        output.height(150);
        var logo_src = $('#id_ikon_src');
        var reader = new FileReader();
        reader.addEventListener('load', function (e) {
            output.attr('src', e.target.result);
            logo_src.val(e.target.result);
        });
        var res = reader.readAsDataURL(filename);
    });
});