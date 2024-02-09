const paginator = document.getElementById("items-paginator");
const loadingArea = document.getElementById('loading-area');

let currentPage;
let totalPages;
let viewMoreButton;
let loadingSpinner;


if (paginator) {
    viewMoreButton = document.getElementById('view-more');
    loadingSpinner = document.getElementById('product-spinner-container');

    currentPage = parseInt(paginator.getAttribute("current-page"));
    totalPages = parseInt(paginator.getAttribute("total-pages"));
}

function loadProducts(pageNumber) {
    loadingSpinner.style.display = 'block';

    if (pageNumber <= totalPages) {
        const nextPageUrl = `?page=${pageNumber}`;
        fetch(nextPageUrl)
            .then(response => response.text())
            .then(content => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(content, 'text/html');
                const products = doc.querySelector('.products-grid');

                loadingArea.appendChild(products);
                
                if (pageNumber == totalPages) {
                    viewMoreButton.remove();
                }
    
                loadingSpinner.style.display = 'none';
            })
            .catch(error => {
                console.error('Error:', error);
            });    
    } 
}
viewMoreButton.addEventListener('click', () => {
    currentPage++;
    loadProducts(currentPage);
});