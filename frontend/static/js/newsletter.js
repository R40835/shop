const newsletterLink = document.getElementById('subscribe-link')
const newsletterForm = document.getElementById('newsletter-popup');

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

document.addEventListener("DOMContentLoaded", function() {
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const choiceField = document.getElementById('choice_field');
    const submitButton = document.querySelector('.submit-button');

    submitButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission
        
        const emailValue = emailInput.value;
        const phoneValue = phoneInput.value;
        const choiceValue = choiceField.value;
        
        // Do something with the values, such as sending them to the server
        console.log("Email:", emailValue);
        console.log("Phone:", phoneValue);
        console.log("Clothing category of interest:", choiceValue);
        
        SubmitNewsletter(emailValue, phoneValue, choiceValue)

        function SubmitNewsletter(email, phone, choice) {
            let xhr = new XMLHttpRequest();
            xhr.open('GET', `/products/newsletter/?email=${email}&phone=${phone}&choice=${choice}`, false); // Make the request synchronous
            xhr.send();
            
            if (xhr.status === 200) {
                let data = JSON.parse(xhr.responseText);
                console.log(data)
                return data;
            } else {
                throw new Error('Failed to fetch data');
            }
        }
        
    });
});
