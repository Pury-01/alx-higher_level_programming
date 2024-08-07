// updates the text color of the <header> element to red when user clicks on the tag DIV#red_header using JQuery API

$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
