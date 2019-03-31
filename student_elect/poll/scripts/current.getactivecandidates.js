

$((function(context) {
    return function() {

        var votes = {
            'candidates': []
        }

        $('.candidateCard').click(function() {
            
            var element = $(this);
            var candidateID = element.attr('data-id');

            console.log('initial value')
            console.log(element.attr('data-checked'));

            

                if (element.attr('data-checked') == 'unchecked') {
                    if (votes['candidates'].length < context.votelimit) {
                        element.attr('data-checked','checked');
                        votes['candidates'].push(candidateID);
                        
                        if (!element.hasClass('checked-candidate')) {
                            // fade class transition
                            element.fadeIn('slow', function() {
                                $(this).addClass('checked-candidate');
                            });
                        }
                    }
                    else {
                        alert('You may only pick ' + context.votelimit + ' ' + (parseInt(context.votelimit) == 1 ? 'candidate' : 'candidates'));
                    }
                }
                else {
                    element.attr('data-checked','unchecked');
                    // remove value from candidates array
                    votes['candidates'].splice($.inArray(candidateID, votes['candidates']), 1);

                    if (element.hasClass('checked-candidate')) {
                        element.fadeIn('slow', function() {
                            $(this).removeClass('checked-candidate');
                        });
                    }
                }
            console.log(votes['candidates']);
        });


        $("#voteButton").click(function(){
            var data = JSON.stringify(votes)
            
            $.ajax({
                url: '/poll/' + context.username + '/current.submitvotes/' + context.pollID + '/' + context.studentID + '/',
                type: 'POST',
                data: data,
                async: false,
                cache: false,
                contentType: false,
                processData: false,
                success: function (content) {
                    $("#interface").fadeOut('slow', function() {
                        $(this).html(content).fadeIn('slow');
                    });
                    setTimeout(function(){location.href = '/poll/' + context.username + '/current/'}, 8000);
                },
                error: function (content) {
                    alert('Error submitting votes. Make sure you are only selecting ' + context.votelimit + ' candidates');
                }
              });
        });

    }   

})(DMP_CONTEXT.get()));
