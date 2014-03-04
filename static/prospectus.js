$(function() {
        $('#add-another').click(function(e) {
                console.log('clicked');
                e.preventDefault();
                console.log('clicked; current count: ' + form_count);
                form_count++;
                console.log('new count: ' + form_count);
                var new_form = form.replace(/__prefix__/g, form_count);
                $('#prospectus-table').append(new_form)
                $('#id_form-TOTAL_FORMS').val(form_count);
            }
        )
    }
)