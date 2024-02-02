const paginator = document.getElementById("items-paginator");
const loadingArea = document.getElementById('loading-area');
let currentPage;
let totalPages;

if (paginator) {
    currentPage = parseInt(paginator.getAttribute("current-page"));
    totalPages = parseInt(paginator.getAttribute("total-pages"));
    console.log(`the current page is ${currentPage}`);
    console.log(`the total no of pages is ${totalPages}`);

}

function appendMessagesToChatLog(pageNumber) {

    if (pageNumber <= totalPages) {
        const nextPageUrl = `?page=${pageNumber}`;
        console.log(`next page url ${nextPageUrl}`)
        fetch(nextPageUrl)
            .then(response => response.text())
            .then(content => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(content, 'text/html');
                // console.log(doc);
                const products = doc.querySelectorAll('.products-grid');
                // console.log(products)
                products.forEach(product => {
                    loadingArea.appendChild(product);
                    // console.log(product.childNodes)
                });

                if (pageNumber == totalPages) {
                    viewMoreButton.remove();
                }
    
            })
            .catch(error => {
                console.error('Error:', error);
            });    
    } 
}
const viewMoreButton = document.getElementById('view-more');
viewMoreButton.addEventListener('click', () => {
    currentPage++;
    console.log(`next page is: ${currentPage}`)
    appendMessagesToChatLog(currentPage);
});