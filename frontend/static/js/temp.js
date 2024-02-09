const collectionDropdownButton = document.getElementById('collection-dropdown');
const closeCollectionButton = document.getElementById('close-collection-button')
const collectionContent = document.querySelector('.collection-content');

const linensTextilesDropdownButton = document.getElementById('linens-textiles-dropdown');
const closeLinensTextilesButton = document.getElementById('close-linens-textiles-button');
const linensAndTextilesContent = document.querySelector('.linens-textiles-content');

const collectionGridContainer = document.getElementById('collection-grid');
const houseGridContainer = document.getElementById('house-grid');
const housegGridContainer2 = document.getElementById('house-grid-two');

let collectionOpened = false;
let houseOpened = false;

function sleep(miliseconds) {
    var currentTime = new Date().getTime();
 
    while (currentTime + miliseconds >= new Date().getTime()) {
    }
 }

 if (event.target !== collectionDropdownButton && houseOpened) {
    // If linens/textiles is opened, wait for its transition to finish before opening collection
    linensAndTextilesContent.addEventListener('transitionend', () => {
        updateDropdown('open', 'collection');
        // Remove the event listener after it's used to prevent multiple event registrations
        linensAndTextilesContent.removeEventListener('transitionend', arguments.callee);
    });
    console.log(houseOpened, collectionOpened)
}
if (event.target !== linensTextilesDropdownButton && collectionOpened) {
     // If collection is opened, wait for its transition to finish before opening linens/textiles
     collectionContent.addEventListener('transitionend', () => {
        updateDropdown('open', 'linens&textiles');
        // Remove the event listener after it's used to prevent multiple event registrations
        collectionContent.removeEventListener('transitionend', arguments.callee);
    });
}

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
    } else if (option === 'linens&textiles') {
        switch(action) {
            case 'open':
                linensTextilesDropdownButton.classList.add('hovered');
                linensAndTextilesContent.classList.toggle('collapsed');
                houseGridContainer.style.display = 'flex';
                housegGridContainer2.style.display = 'flex';
                closeLinensTextilesButton.style.display = 'block';
                houseOpened = true;
                break;
            case 'close': 
                linensTextilesDropdownButton.classList.remove('hovered'); 
                linensAndTextilesContent.classList.remove('collapsed');
                houseGridContainer.style.display = 'none';
                housegGridContainer2.style.display = 'none';
                closeLinensTextilesButton.style.display = 'none';
                houseOpened = false;
                break;
        }    
    }
}

collectionDropdownButton.addEventListener('click', function(event) {
    event.preventDefault();
    if (!collectionOpened) {
        updateDropdown('open', 'collection');
    } else {
        updateDropdown('close', 'collection');
    }
});


linensTextilesDropdownButton.addEventListener('click', function(event) {
    event.preventDefault();
    if (!houseOpened) {
        updateDropdown('open', 'linens&textiles');
    } else {
        updateDropdown('close', 'linens&textiles');
    }
});


window.addEventListener('click', function(event) {
    if (event.target !== collectionDropdownButton && !collectionContent.contains(event.target) || event.target === closeCollectionButton) {
        updateDropdown('close', 'collection');
    }
    if (event.target !== linensTextilesDropdownButton && !linensAndTextilesContent.contains(event.target) || event.target === closeLinensTextilesButton) {
        updateDropdown('close', 'linens&textiles');
    }
})