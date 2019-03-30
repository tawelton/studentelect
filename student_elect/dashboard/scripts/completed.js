$((function(context) {
    return function() {

        $(".pollDelete").click(function() {

            if (confirm("Are you sure you want to delete this poll?")) {

                var element = $(this);
                var pollID = element.attr('data-id')
                
                $.ajax({
                    url: "/dashboard/edit.deletepoll/" + pollID,
                    type: 'POST'
                  }).done(function(content) {
                    location.href = "/dashboard/completed/";
                  });
            }

            

        });     

    }   

})(DMP_CONTEXT.get()));
