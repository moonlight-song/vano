$(document).ready(function() {

$('clicker').click (getAll());

function getAll() {

    $.ajax ({
        type : 'GET',
        url : 'http://127.0.0.1:8000/humen/humen/'
    }).done (function (response) {
        alert (JSON.stringify (response));
    }).fail(function() {
        alert( "error" );
    });

}

});