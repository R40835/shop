const searchInput = document.getElementById('product-search');
const searchResults = document.getElementById('search-results');

searchInput.addEventListener('input', debounce(search, 300));

document.addEventListener('click', closePopup);

    // Event delegation for handling clicks on the results
searchResults.addEventListener('click', handleResultClick);

function debounce(func, delay) {
    let timeoutId;
    return function () {
        const args = arguments;
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

async function search() {
    const query = searchInput.value;
    if (query.trim() === '') {
        searchResults.innerHTML = '';
        return;
    }

    try {
        const response = await fetch(`/products/search-autocomplete/?term=${encodeURIComponent(query)}`);
        const data = await response.json();
        console.log("data ->", data)

        if (data.items) {
            const products = data.items;
            // Clear previous results
            searchResults.innerHTML = '';
            // Display new results
            products.forEach(result => {
                const li = document.createElement('li');
                li.textContent = result[1];
                li.classList.add('result-found');
                searchResults.appendChild(li);
            });
        } else {
            searchResults.innerHTML = '';
            const li = document.createElement('li');
            li.textContent = 'No Results';
            li.classList.add('result-not-found');
            searchResults.appendChild(li);
        }
    } catch (error) {
        console.error('Error fetching autocomplete results:', error);
    }
}

function closePopup(event) {
    // Check if the click target is outside the search input and results
    if (
        event.target !== searchInput &&
        !searchInput.contains(event.target) &&
        event.target !== searchResults &&
        !searchResults.contains(event.target)
    ) {
        // Close the popup
        searchResults.innerHTML = '';
    }
}

function handleResultClick(event) {
    const clickedElement = event.target;
    const ResultFound = clickedElement.classList.contains('result-found');
    // Check if the clicked element is an <li> inside the searchResults
    if (clickedElement.tagName === 'LI' && searchResults.contains(clickedElement) && ResultFound) {
        // Set the input value to the clicked item's text
        searchInput.value = clickedElement.textContent;

        // Close the popup
        searchResults.innerHTML = '';
    }
}