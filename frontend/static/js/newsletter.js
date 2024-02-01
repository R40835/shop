const newsletterLink = document.getElementById('subscribe-link')
const newsletterForm = document.getElementById('newsletter-popup');
const closeNewsletter = document.getElementById('close-newsletter');
const successMessage = document.getElementById("success-message");
const failureMessage = document.getElementById("failure-message");
const closeMessages = document.querySelectorAll('.close-message-button');

document.addEventListener("DOMContentLoaded", () => {
    const emailInput = document.getElementById('email');
    const confirmEmailInput = document.getElementById('confirm-email');
    const choiceField = document.getElementById('choice-field');
    const submitButton = document.querySelector('.submit-button');

    function hideNewsletterForm() {
        newsletterForm.style.display = 'none';
    };

    function clearNewsletterFormErrors() {
        document.getElementById('invalid-email').style.display = 'none';
        document.getElementById('unmatching-email').style.display = 'none';
        document.getElementById('existing-email').style.display = 'none';
        document.getElementById('email-field-required').style.display = 'none';
        document.getElementById('confirm-email-field-required').style.display = 'none';
        emailInput.classList.remove('newsletter-field-error');
        confirmEmailInput.classList.remove('newsletter-field-error');    
    }

    function reinitialiseNewsletterForm() {
        emailInput.value = "";
        confirmEmailInput.value = "";
        choiceField.value = choiceField.options[0].value;
    }
    
    newsletterLink.addEventListener('click', (event) => {
        event.preventDefault(); 
        newsletterForm.style.display = 'block';
    });
    
    document.addEventListener('click', (event) => {
        if (!newsletterForm.contains(event.target) && event.target !== newsletterLink) {
            reinitialiseNewsletterForm();
            clearNewsletterFormErrors();
            hideNewsletterForm();
        }
    });
    
    closeNewsletter.addEventListener('click', () => {
        reinitialiseNewsletterForm();
        clearNewsletterFormErrors();
        hideNewsletterForm();
    });
    
    closeMessages.forEach(closeMessage => {
        closeMessage.addEventListener('click', () => {
            switch (closeMessage.getAttribute('close')) {
                case 'success-close':
                    successMessage.style.display = 'none';
                    break;
                case 'failure-close':
                    failureMessage.style.display = 'none';
                    break;
            }
        })
    })

    submitButton.addEventListener('click', (event) => {
        event.preventDefault(); 
        
        const emailValue = emailInput.value;
        const confirmEmailValue = confirmEmailInput.value;
        const choiceValue = choiceField.value;
                
        clearNewsletterFormErrors();

        const response = SubmitNewsletter(emailValue, confirmEmailValue, choiceValue)

        switch (response) {
            case 'success':
                hideNewsletterForm();
                successMessage.style.display = "block";
                reinitialiseNewsletterForm();
                break;
            case 'failure':
                document.getElementById('existing-email').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                confirmEmailInput.value = "";
                choiceField.value = choiceField.options[0].value;
                break;
            case 'invalid-email':
                document.getElementById('invalid-email').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                break;
            case 'unmatching-email':
                document.getElementById('unmatching-email').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                confirmEmailInput.classList.add('newsletter-field-error');
                break;
        }

        function SubmitNewsletter(email, confirm_email, choice) {
            let fieldsFilledOut = true;
            if (email.trim() === '') {
                document.getElementById('email-field-required').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                fieldsFilledOut = false;
            } 
            if (confirm_email.trim() === '') {
                document.getElementById('confirm-email-field-required').style.display = 'block';
                confirmEmailInput.classList.add('newsletter-field-error');
                fieldsFilledOut = false;
            }
            
            if (fieldsFilledOut) {
                let xhr = new XMLHttpRequest();
                xhr.open('GET', `/products/newsletter/?email=${email}&confirm_email=${confirm_email}&choice=${choice}`, false); // Make the request synchronous
                xhr.send();
                
                if (xhr.status === 200) {
                    let data = JSON.parse(xhr.responseText);
                    console.log(data)
                    return data.response;
                } else {
                    throw new Error('Failed to fetch data');
                }    
            }
        }        
        
    });
});
