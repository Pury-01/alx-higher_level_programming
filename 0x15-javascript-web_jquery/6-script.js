// updates the text on the <header> element to 'New Header!!!' when the user clicks on DIV#update_header
(function (callback) {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = callback;
  document.head.appendChild(script);
})(function () {
  $(document).ready(function () {
    $('#update_header').on('click', function () {
      $('header').text('New Header!!!');
    });
  });
});
