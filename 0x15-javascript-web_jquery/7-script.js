$(function () {
  const $character = $('#character');

  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function (data) {
      $character.append('<p>' + data.name + '</p>');
    }
  });
});
