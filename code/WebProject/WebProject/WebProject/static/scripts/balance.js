function Balance() {
    var url = 'http://' + document.domain + ':' + location.port + '/balance/current';

    $.getJSON(url, function (data) {
        var value = `${data.balance}`

        $(".mypanel").html(value);
    });

}