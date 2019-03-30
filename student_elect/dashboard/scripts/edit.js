$((function(context) {
    return function() {

        function getcandidates(){
            var container = $("#candidate-container");
            $.ajax({
                url: "/dashboard/edit.getactivecandidates/" + context.pollID,
            }).done(function(content) {
                $(container).html(content);
            })
        }
        
        $(document).ready(getcandidates);

        $("#pollStatus").click(function() {
            $.ajax({
                url: "/dashboard/edit.togglepollstatus/" + context.pollID,
                type: 'POST'
              }).done(function(content) {
                location.reload();
              });

        });

        $("#pollEnd").click(function() {
            $.ajax({
                url: "/dashboard/edit.endpoll/" + context.pollID,
                type: 'POST'
              }).done(function(content) {
                location.href = "/dashboard/active/";
              });

        });

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
