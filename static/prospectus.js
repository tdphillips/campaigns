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
