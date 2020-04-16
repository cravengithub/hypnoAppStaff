$(function () {
    $('#id_tanggal_bayar').datepicker({
        dateFormat: "yy-mm-dd"
    });
    $('#btn-browse').change(function (evt) {
        console.clear();
        var filename = evt.target.files[0];
        var output = $('#img-bukti');
        output.width(300);
        output.height(150);
        var bukti_path = $('#id_bukti_path');
        var reader = new FileReader();
        reader.addEventListener('load', function (e) {
            output.attr('src', e.target.result);
            bukti_path.val(e.target.result);
        });
        var res = reader.readAsDataURL(filename);
    });
});