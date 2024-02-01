const newsletterLink = document.getElementById('subscribe-link')
const newsletterForm = document.getElementById('newsletter-popup');
const closeNewsletter = document.getElementById('close-newsletter');

newsletterLink.addEventListener('click', (event) => {
    event.preventDefault(); 
    
    console.log(newsletterForm)
    newsletterForm.style.display = 'block';
});

document.addEventListener('click', (event) => {
    if (!newsletterForm.contains(event.target) && event.target !== newsletterLink) {
        newsletterForm.style.display = 'none';
    }
});

closeNewsletter.addEventListener('click', () => {
    newsletterForm.style.display = 'none';
});

document.addEventListener("DOMContentLoaded", () => {
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const choiceField = document.getElementById('choice-field');
    const submitButton = document.querySelector('.submit-button');

    submitButton.addEventListener('click', (event) => {
        event.preventDefault(); 
        
        const emailValue = emailInput.value;
        const phoneValue = phoneInput.value;
        const choiceValue = choiceField.value;
                
        const response = SubmitNewsletter(emailValue, phoneValue, choiceValue)

        switch (response) {
            case 'success':
                console.log("new follower!")
                break;
            case 'failure':
                console.log('existing follower')
                break;
        }


        function SubmitNewsletter(email, phone, choice) {
            let xhr = new XMLHttpRequest();
            xhr.open('GET', `/products/newsletter/?email=${email}&phone=${phone}&choice=${choice}`, false); // Make the request synchronous
            xhr.send();
            
            if (xhr.status === 200) {
                let data = JSON.parse(xhr.responseText);
                console.log(data)
                return data.response;
            } else {
                throw new Error('Failed to fetch data');
            }
        }
        
    });
});
