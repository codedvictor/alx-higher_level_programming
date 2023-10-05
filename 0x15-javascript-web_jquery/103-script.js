const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    sayHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      sayHello();
    }
  });
};

function sayHello () {
  const lan = $('INPUT#language_code').val();
  $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
}
