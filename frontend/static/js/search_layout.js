    // Get the move div and its content
    var moveDiv = document.querySelector('.move');
    // Get the search span
    var searchSpan = document.querySelector('.search');
    // Get the search bar div
    var searchForm = document.getElementById('search-form');
    var searchField = document.getElementById('product-search');
    var middleLinks = document.getElementById('middle-links');
    var rightLinks = document.getElementById('right-links');
    var cancelLink = document.getElementById('cancel-link');
    // Add input event listener to the search input
    searchField.addEventListener('input', function() {
        // Move the content to the search span only if it's not already there
        if (searchForm.parentNode !== searchSpan) {
            searchSpan.innerHTML = ''; // Clear previous content
            searchSpan.appendChild(searchForm);
            searchField.focus();
            if (searchField.value.trim() !== '') {
                    // If there is input, switch to the search layout
                    cancelLink.style.display = 'inline-block';
                    middleLinks.style.display = 'none';
                    rightLinks.style.display = 'none';
                } else {
                    // If no input, switch back to the default layout
                    cancelLink.style.display = 'none';
                    middleLinks.style.display = 'inline-block';
                    rightLinks.style.display = 'inline-block';
                }
        }
    });
    // Add click event listener to the cancel link
    cancelLink.addEventListener('click', function() {
        // Move the content back to its initial spot
        if (searchbarDiv.parentNode !== moveDiv) {
            moveDiv.innerHTML = ''; // Clear previous content
            moveDiv.appendChild(searchbarDiv);
            searchInput.value = ''; // Clear the input value
            searchInput.blur(); // Remove focus from the input field
            middleLinks.style.display = 'inline-block';
            cancelLink.style.display = 'none';
        }
    });
