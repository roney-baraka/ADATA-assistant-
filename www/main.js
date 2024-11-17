$(document).ready(function () {

    $('.text').textillate({
         loop: true,
         sync: true,
         in:{
            effect: "bounceIn",
         },
         out: {
            effect: "bounceOut",
         },
    });


    // SiriWave initialization
    const siriContainer = document.getElementById("siri-container");
    let siriWave;
    if (siriContainer) {
        siriWave = new SiriWave({
            container: siriContainer,
            width: 800,
            height: 200,
            style: "ios9",
            amplitude: "1", 
            speed: "0.30",   
            autostart: true
        });
    }

    //Siri message animation 
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
    });

    //Display message to Python and update UI
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        console.log(message);
        $('.siri-message li:first').text(message);
        $('.siri-message li:first').textillate('start');
    }

    //Microphone button click event 
    $("MicBtn").click(function (e) {
        const micButton = $(this)
        micButton.prop("disabled", true);
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);

        eel.allCommands().then(() => {
            micButton.prop("disabled", false); 
        }).catch((err) => {
            console.error("Error during command execution:", err);
            micButton.prop("disabled", false);
        });
    });
});