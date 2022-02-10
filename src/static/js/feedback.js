(function () {
    $(document).ready(function () {
        const form = $('#feedback_form');
        // const alert = $('#feedback_alert');

        const username_errors = $('#username_errors');
        const phone_number_errors = $('#phone_number_errors');
        const email_errors = $('#email_errors');
        const message_errors = $('#message_errors');
        const terms_accepted_errors = $('#terms_accepted_errors');
        form.submit(function (e) {
            e.preventDefault();

            $.ajax({
                method: 'POST',
                url: 'feedback/',
                data: form.serializeArray(),
                success: function (data) {
                    if (data.status === 'error') {
                        const errors = data.errors;

                        errors.username ? username_errors.html(errors.username) : username_errors.empty();
                        errors.phone_number ? phone_number_errors.html(errors.phone_number) : phone_number_errors.empty();
                        errors.email ? email_errors.html(errors.email) : email_errors.empty();
                        errors.message ? message_errors.html(errors.message) : message_errors.empty();
                        errors.terms_accepted ? terms_accepted_errors.html(errors.terms_accepted) : terms_accepted_errors.empty();
                    }
                    if (data.status === 'success') {
                        // Force hide bootstrap modal
                        username_errors.empty();
                        phone_number_errors.empty();
                        email_errors.empty();
                        message_errors.empty();
                        terms_accepted_errors.empty();

                        form[0].reset();
                        form.empty();
                        window.location.pathname.startsWith('/uk/') ? form.html("<h3 class='form-sent-text'>Дякуємо за ваше питання!</h3>") : null;
                        window.location.pathname.startsWith('/en/') ? form.html("<h3 class='form-sent-text'>Thank you for your question!</h3>") : null;
                        window.location.pathname.startsWith('/ru/') ? form.html("<h3 class='form-sent-text'>Благодарим за ваш вопрос!</h3>") : null;
                    }
                },
                error: function (error) {
                    // TODO: show error message
                }
            });
        });
    });
})();