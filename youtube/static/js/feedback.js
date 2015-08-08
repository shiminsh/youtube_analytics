
initializeRatings();

function initializeRatings() {
    $('#rate1').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate2').shieldRating({
        max: 7,
        step: 0.1,
        value: 6,
        markPreset: false
    });
    $('#rate3').shieldRating({
        max: 7,
        step: 0.1,
        value: 4.5,
        markPreset: false
    });
    $('#rate4').shieldRating({
        max: 7,
        step: 0.1,
        value: 5,
        markPreset: false
    });
    $('#rate5').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate6').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate7').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate8').shieldRating({
        max: 7,
        step: 0.1,
        value: 5,
        markPreset: false
    });
    $('#rate9').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate10').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate11').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate12').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate13').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate14').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate15').shieldRating({
        max: 7,
        step: 0.1,
        value: 5,
        markPreset: false
    });
    $('#rate16').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate17').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate18').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate19').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate20').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
    $('#rate21').shieldRating({
        max: 7,
        step: 0.1,
        value: 6.3,
        markPreset: false
    });
}
function resetActive(event, percent) {
    $(".progress-bar").css("width", percent + "%").attr("aria-valuenow", percent);
    $(".progress-completed").text(percent + "%");

    $("div").each(function () {
        if ($(this).hasClass("activestep")) {
            $(this).removeClass("activestep");
        }
    });

    if (event.target.className == "col-md-2") {
        $(event.target).addClass("activestep");
    }
    else {
        $(event.target.parentNode).addClass("activestep");
    }
}