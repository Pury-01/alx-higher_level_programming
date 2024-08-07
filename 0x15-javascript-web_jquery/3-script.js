// adds the class red to the <header> elemennt when the user clicks on the tag DIV#red_header
(function (callback) {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = callback;
  document.head.appendChild(script);
})(function () {
  $(document).ready(function () {
    $('#red_header').on('click', function () {
      $('header').addClass('red');
    });
  });
});
