$((function(context) {
    return function() {

        $("#studentForm").submit(function(event){
            event.preventDefault(); //prevent default action 

            var post_url = $(this).attr("action"); //get form action url
            var form_data = new FormData($(this)[0]);
            
            $.ajax({
                url: post_url,
                type: 'POST',
                data: form_data,
                async: false,
                cache: false,
                contentType: false,
                processData: false,
                success: function (content) {
                    $("#interface").fadeOut('slow', function() {
                        $(this).html(content).fadeIn('slow');
                    });
                },
                error: function (content) {
                    alert('Invalid student ID. Please use a valid student ID')
                }
              });
        });
    }   

})(DMP_CONTEXT.get()));
