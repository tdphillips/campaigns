$(function() {
    $('#add-another').click(function(e) {
        e.preventDefault();
        form_count++;
        var new_form = form.replace(/__prefix__/g, form_count);
        $('#prospectus-table').append(new_form)
        $('#id_form-TOTAL_FORMS').val(form_count);
    });

    $('#vote').click(function(e) {
        e.preventDefault();
        /* TODO: Do save voting logic */
    })
});

function enableSpinners() {
    var limit = parseInt($('#vote-points-total').text());
    var spinners = $('.spinner');
    spinners.spinner({
        min: 0,
        max: limit,
        spin: function(event, ui) {
            var current_max = 0;
            spinners.each(function() {
                current_max += parseInt(this.value);
            });
            if (limit - current_max >= 0) {
                spinners.each(function() {
                    $(this).spinner('option', 'max', limit - current_max + this.value)
                    $(this).attr('max', (limit - current_max - this.value));
                });
            } else {
                $(this).val(ui.value);
            }
        },
    });
    spinners.click(function(event) {
        event.stopPropagation();
    });
    $('.ui-spinner-button').click(function(event) {
        event.stopPropagation();
    });
}