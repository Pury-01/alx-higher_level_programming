// updates the text color of the <header> element to red (#FF0000)
(function () {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = () => {
    $(document).ready(() => {
      $('header').css('color', '#FF0000');
    });
  };
  document.head.appendChild(script);
})();
