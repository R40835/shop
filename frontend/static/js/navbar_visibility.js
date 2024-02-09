var lastScrollTop = 0;
var navbar = document.getElementById("navbar");
var navbarTop = document.getElementById("navbar-top");
var navbarHeight = navbar.offsetHeight;

window.addEventListener("scroll", function() {
  var currentScroll = document.documentElement.scrollTop;
  if (currentScroll > lastScrollTop && currentScroll > navbarHeight) {
    // Scrolling down, hide the navbar
    navbar.style.top = "80px";
    navbarTop.style.top = "0px";
  } 
  lastScrollTop = currentScroll;
});