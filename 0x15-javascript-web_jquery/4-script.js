// toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
(function (callback) {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = callback;
  document.head.appendChild(script);
})(function () {
  $(document).ready(function () {
    $('#toggle_header').on('click', function () {
      if ($('header').hasClass('red')) {
        $('header').removeClass('red').addClass('green');
      } else {
        $('header').removeClass('green').addClass('red');
      }
    });
  });
});
