$(document).ready(function () {
    



        // Display Speak Message
        eel.expose(DisplayMessage)
        function DisplayMessage(message) {
            if ($('siri-message').length) {
                $(this).text(message).fadeOut('fast', function() {
                    $(this).text(message).fadeIn('fast');
                });
            } else {
                console.error("Element '.siri-message' not found.") 
            }
    
        }

            // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        if ($("#Oval").length && $("#SiriWave").length) {
            $("#Oval").attr("hidden", false);
            $("#SiriWave").attr("hidden", true);
        } else {
            console.error("Elements '#Oval' or '#SiriWave' not found. ")
        }
    }

});