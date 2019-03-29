$((function(context) {
    return function() {

        function getcandidates(){
            var container = $("#candidate-container");
            $.ajax({
                url: "/dashboard/edit.getactivecandidates/" + context.poll,
            }).done(function(content) {
                $(container).html(content);
            })
        }
        
        $(document).ready(getcandidates);

        $("#candidateform").submit(function(event){
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
                success: function (returndata) {
                    getcandidates();
                    $("#candidateModal").modal('hide');
                }
              });
        });        

    }   

})(DMP_CONTEXT.get()));
