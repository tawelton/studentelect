$((function(context) {
    return function() {

        $(".pollSelect").click(function() {

            var pollElement = $(this);
            var pollID = pollElement.attr('data-id');

            $.ajax({
                url: "/poll/"+ context.username + "/current.getlogin/" + pollID,
                type: 'POST'
              }).done(function(content) {
                $("#interface").fadeOut('slow', function() {
                    $(this).html(content).fadeIn('slow');
                })
              });

        });  

    }   

})(DMP_CONTEXT.get()));
