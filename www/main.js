$(document).ready(function () {

    $('.text').textillate({
         loop: true,
         sync: true,
         in:{
            effect: "bounceIn",
         },
         out:{
            effect: "bounceOut",
         },
    });

    const siriContainer = document.getElementById("siri-container");
    if (siriContainer) {
        // Initialize SiriWave
        var siriWave = new SiriWave({
            container: siriContainer,
            width: 800,
            height: 200,
            style: "ios9",
            amplitude: 1, 
            speed: 0.3,   
            autostart: true
        });
    };

        // Siri message animation
        $('.siri-message').textillate({
            loop: true,
            sync: true,
            in: {
                effect: "fadeInUp",
                sync: true,
            },
            out: {
                effect: "fadeOutUp",
                sync: true,
            },
    
        });

});