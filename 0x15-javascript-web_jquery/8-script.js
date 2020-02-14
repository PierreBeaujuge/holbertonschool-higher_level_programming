//
$.ajax(
  {
    url: 'https://swapi.co/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (response) { response.results.forEach(dict => $('#list_movies').append('<li>' + dict.title + '</li>')); }
  }
);
