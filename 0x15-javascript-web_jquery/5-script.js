// adds a <li> element to a list when the user clicks on the tag DIV#add_item
(function (callback) {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = callback;
  document.head.appendChild(script);
})(function () {
  $(document).ready(function () {
    $('#add_item').on('click', function () {
      $('UL.my_list').append('<li>Item<li>');
    });
  });
});
