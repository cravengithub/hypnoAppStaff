$(function () {
    $('#id_deskripsi').summernote({
        placeholder: 'Deskripsi isi Paket Terapi.',
        tabsize: 2,
        height: 350
    });
    $('#id_mulai').datepicker({
        dateFormat: "yy-mm-dd"
    });
    $('#id_akhir').datepicker({
        dateFormat: "yy-mm-dd"
    });

});