const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').text();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
};
