const dropdownButton = document.getElementById('dropdown-button');
const dropDownContent = document.querySelector('.dropdown-content');

function updateButtonStyle(action) {
    switch(action) {
        case 'mouseover':
            dropdownButton.classList.add('hovered');
            dropDownContent.style.display = 'block';
            break;
        case 'mouseout':
            dropdownButton.classList.remove('hovered'); 
            dropDownContent.style.display = 'none';
            break;
    }
}

dropDownContent.addEventListener('mouseover', function() {
    updateButtonStyle('mouseover');
});

dropdownButton.addEventListener('mouseover', function() {
    updateButtonStyle('mouseover');
})

window.addEventListener('mouseout', function(event) {
    if (event.target !== dropdownButton) {
        updateButtonStyle('mouseout');
    }
})
