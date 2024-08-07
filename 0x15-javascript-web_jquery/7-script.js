// fetches the character name from thie url "https://swapi-api.alx-tools.com/api/people/5/?format=json"
(function (callback) {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = callback;
  document.head.appendChild(script);
})(function () {
  $(document).ready(function () {
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
      $('#character').text(data.name);
    });
  });
});
