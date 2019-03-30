$((function(context) {
    return function() {

        $(".close").click(function(){
            console.log('clicked');
            var candidateElement = $(this);
            var candidateID = candidateElement.attr('data-id');
            candidateElement.closest(".candidate").remove()


            $.ajax({
                url: '/dashboard/edit.deletecandidate/' + candidateID,
                type: 'POST',
                async: false,
                cache: false,
                contentType: false,
                processData: false,
                success: function (returndata) { }
              });
        });
    }   

})(DMP_CONTEXT.get()));
