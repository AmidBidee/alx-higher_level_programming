$('#hello').on(function () {
    $.ajax({
        type:'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        dataType:'json',
        success: function (data) {
            $hello.append('<p>' + data + '</p>');
        }
    });
});
