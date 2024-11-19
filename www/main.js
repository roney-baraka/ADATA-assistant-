$(document).ready(function () {


if ($('.text').length) {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut"
        },
    });
}

if ($('.siri-message').legth) {
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
    });
}


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
    } else {
        console.error("#siri-container not found.");
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
        console.log("DisplayMessage called with message", message);

        if ($('.siri-message').length) {
            $('.siri-message li:first').text(message);
            $('.siri-message').textillate(start);
        } else {
            console.error("Element '.siri-message' not found.");
        }

    }

    //Microphone button click event 
    $("#MicBtn").click(function (e) {
        const micButton =$(this);
        micButton.prop("disabled", true);
        eel.playAssistantSound();

        if($("#Oval").length && $("#Siriwave").length) {
            $("#Oval").attr("hidden",true);
            $("#SiriWave").attr("hidden", false);
        } else{
            console.error("#Oval or #SiriWave not found.");
        }

       eel.allCommands()
          .then(() => {
            micButton.prop("disabled" false);
          })
          .catch((err) =>{
            console.error("Error during command execution:", err);
            micButton.prop("disabled", false);
          })
    });
});