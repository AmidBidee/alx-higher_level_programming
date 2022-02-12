$(function () {
  const $movieList = $('ul#list_movies');

  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    dataType: 'json',
    success: function (movies) {
      $.each(movies.results, function (i, movie) {
        $movieList.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
