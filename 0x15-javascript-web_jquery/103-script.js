$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`,
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function () {
        $('#hello').text('Translation not found');
      }
    });
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      $('#btn_translate').click();
    }
  });
});
