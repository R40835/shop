const collectionDropdownButton = document.getElementById('collection-dropdown');
const closeCollectionButton = document.getElementById('close-collection-button')
const collectionContent = document.querySelector('.collection-content');

const houseDropdownButton = document.getElementById('linens-textiles-dropdown');
const closeHouseButton = document.getElementById('close-linens-textiles-button');
const houseContent = document.querySelector('.linens-textiles-content');

const collectionGridContainer = document.getElementById('collection-grid');
const houseGridContainer = document.getElementById('house-grid');
const housegGridContainer2 = document.getElementById('house-grid-two');

let collectionOpened = false;
let houseOpened = false;

function updateDropdown(action, option) {
    if (option === 'collection') {
        switch(action) {
            case 'open':
                collectionDropdownButton.classList.add('hovered');
                collectionContent.classList.toggle('collapsed');

                collectionGridContainer.style.display = 'flex'
                closeCollectionButton.style.display = 'block';
                collectionOpened = true;
                break;
            case 'close': 
                collectionDropdownButton.classList.remove('hovered'); 
                collectionContent.classList.remove('collapsed');
                collectionGridContainer.style.display = 'none';
                closeCollectionButton.style.display = 'none';
                collectionOpened = false;
                break;
        }    
    } else if (option === 'house') {
        switch(action) {
            case 'open':
                houseDropdownButton.classList.add('hovered');
                houseContent.classList.toggle('collapsed');
                houseGridContainer.style.display = 'flex';
                housegGridContainer2.style.display = 'flex';
                closeHouseButton.style.display = 'block';
                houseOpened = true;
                break;
            case 'close': 
                houseDropdownButton.classList.remove('hovered'); 
                houseContent.classList.remove('collapsed');
                houseGridContainer.style.display = 'none';
                housegGridContainer2.style.display = 'none';
                closeHouseButton.style.display = 'none';
                houseOpened = false;
                break;
        }    
    }
}

collectionDropdownButton.addEventListener('click', function(event) {
    event.preventDefault();
    if (!houseOpened) {
        if (!collectionOpened) {
            updateDropdown('open', 'collection');
        } else {
            updateDropdown('close', 'house');
        }
    } else {
        updateDropdown('close', 'house');
        setTimeout(() => {
            updateDropdown('open', 'collection');
        }, 500); 
    }
});

houseDropdownButton.addEventListener('click', function(event) {
    event.preventDefault();
    if (!collectionOpened) {
        if (!houseOpened) {
            updateDropdown('open', 'house');
        } else {
            updateDropdown('close', 'collection');
        }
    } else {
        updateDropdown('close', 'collection');
        setTimeout(() => {
            updateDropdown('open', 'house');
        }, 500);
    }
});

window.addEventListener('click', function(event) {
    
    if (event.target !== collectionDropdownButton && !collectionContent.contains(event.target) || event.target === closeCollectionButton) {
        updateDropdown('close', 'collection');
    }
    if (event.target !== houseDropdownButton && !houseContent.contains(event.target) || event.target === closeHouseButton) {
        updateDropdown('close', 'house');
    }
});