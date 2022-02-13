$(document).ready(function () {
  $.get(
    "https://fourtonfish.com/hellosalut/?lang=fr",
    function (data) {
      $("#hello").append("<p>" + data.hello + "</p>");
    },
    "json"
  );
});
