// update the text color of the <header> element to red using JQuery API
if (typeof jQuery !== 'undefined') {
  $('header').css('color', '#FF0000');
} else {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = function () {
    $('header').css('color', '#FF0000');
  };
  document.head.appendChild(script);
}
