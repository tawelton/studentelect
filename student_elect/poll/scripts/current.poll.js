$((function(context) {
    return function() {

        function getcandidates(){
            var container = $("#interface");
            $.ajax({
                url: "/dashboard/current.getactivecandidates/" + context.pollID,
            }).done(function(content) {
                $(container).html(content);
            })
        }
        
        $(document).ready(getcandidates);

    }   

})(DMP_CONTEXT.get()));
