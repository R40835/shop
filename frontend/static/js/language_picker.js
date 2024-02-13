const dashboard = document.querySelector('.dashboard');
const language = document.querySelector('.language');

const dashboardIndicator = document.querySelector('.dashboard-indicator');
const languagePicker = document.querySelector('.language-picker');
const languagePickerContainer = document.querySelector('.language-picker-container');

if (dashboard) {
    dashboard.addEventListener('click', () => {
        window.location.href = '/products/dashboard/';
    })

    dashboard.addEventListener('mouseover', () => {
        dashboardIndicator.style.display = 'inline';
    })

    dashboard.addEventListener('mouseout', () => {
        dashboardIndicator.style.display = 'none';
    })
}

language.addEventListener('click', (event) => {
    event.preventDefault();
    languagePicker.style.display = 'inline';
})

languagePicker.addEventListener('click', (event) => {
    event.preventDefault();
})

window.addEventListener('click', (event) => {
    if (!languagePickerContainer.contains(event.target) && !language.contains(event.target)) { 
        languagePicker.style.display = 'none';
    }
})