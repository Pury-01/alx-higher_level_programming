// fetches and lists the title for all movies by using the url "https://swapi-api.alx-tools.com/api/films/?format=json"
(function (callback) {
  const script = document.createElement('script');
  script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
  script.onload = callback;
  document.head.appendChild(script);
})(function () {
  $(document).ready(function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
      data.results.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    });
  });
});
