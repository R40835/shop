var filterbar = document.getElementById("filterbar");
if (filterbar) {
    var cloneCreated = false;
    var filterbarClone = filterbar.cloneNode(true); 
    var lastScrollTopCategoryPage = 0;
    var filterbarHeight = 450 //filterbar.offsetHeight; not very precise better find another way
    const filterbarInitialHeight = filterbar.top + window.scrollY;
    
    window.addEventListener("scroll", function() {
        filterbarCurrentPosition = filterbar.getBoundingClientRect();
        filterbarCurrentYPosition = filterbarCurrentPosition.y;
        filterbarCurrentPositionHeight = filterbarCurrentPosition.height;
        var currentScroll = document.documentElement.scrollTop;

        if (filterbarCurrentYPosition >= (0 + filterbarCurrentPositionHeight)) {
            if (cloneCreated) {
                this.document.body.removeChild(filterbarClone);
                cloneCreated = false;   
            }
        }
        if (currentScroll > lastScrollTopCategoryPage && currentScroll > filterbarCurrentYPosition) {
            // Scrolling down, hide the navbar
            if (cloneCreated) {
                this.document.body.removeChild(filterbarClone);
                cloneCreated = false;
            }
        } else {
            if (filterbarCurrentYPosition < 0) {
                // Scrolling up or at the top, show the navbar
                filterbarClone.style.top = "80px";
                filterbarClone.style.width = '100%';
                filterbarClone.style.padding = '0 10px';
                filterbarClone.style.position = 'fixed';
                filterbarClone.style.zIndex = '1';
                // console.log(filterbarClone)
                this.document.body.appendChild(filterbarClone);
                cloneCreated = true;
            }
        }
        lastScrollTopCategoryPage = currentScroll;
    });     
    
    const filter = document.querySelector('.filter-link');
    const sidebar = document.getElementById('sidebar');

    window.addEventListener('click', function(event) {
        if (event.target.classList.value === filter.classList.value) {
            sidebar.style.display = 'block';
        } else {
            sidebar.style.display = 'none';
        }
    });

} else {
    console.log('filter bar does not exist')
}