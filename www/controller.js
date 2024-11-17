$(document).ready(function () {
    



        // Display Speak Message
        eel.expose(DisplayMessage)
        function DisplayMessage(message) {

            $('.siri-message').text('message').fadeIn();
    
        }

            // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

});