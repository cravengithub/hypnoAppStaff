$(function () {
    $('#id_tanggal_lahir').datepicker({
        dateFormat: "yy-mm-dd"
    });
    $('#foto').change(function (evt) {
        console.clear();
        var filename = evt.target.files[0];
        var output = $('#img-foto');
        output.width(150);
        output.height(150);
        var foto_src = $('#id_foto_src');
        var reader = new FileReader();
        reader.addEventListener('load', function (e) {
            output.attr('src', e.target.result);
            foto_src.val(e.target.result);
        });
        var res = reader.readAsDataURL(filename);

        // var message = "sekarang saya sedang makan roti";
        // var out = btoa(res);
        // console.log('file size: ' + filename.size)
        // alert(out);
    });
});