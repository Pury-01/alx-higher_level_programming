// fetches from 'https://hellosalut.stefanbohacek.dev/?lang=fr' and displays the value of hello
(function (callback) {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = callback;
  document.head.appendChild(script);
})(function () {
  $(document).ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
      $('#hello').text(data.hello);
    });
  });
});
