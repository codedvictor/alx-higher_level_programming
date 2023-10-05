const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  const res = data.results;
  for (let x = 0; x < res.length; x++) {
    $('UL#list_movies').append('<li>' + res[x].title + '</li>');
  }
});
