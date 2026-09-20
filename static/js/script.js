let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

document.addEventListener('click', (event) => {
    const isNavbarOpen = navbar.classList.contains('active');
    const clickedInsideNavbar = navbar.contains(event.target);
    const clickedMenuIcon = menuIcon.contains(event.target);

    if (isNavbarOpen && !clickedInsideNavbar && !clickedMenuIcon) {
        navbar.classList.remove('active');
        menuIcon.classList.remove('bx-x');
    }
});

document.querySelectorAll('.skill-bar').forEach(bar => {
    const percentage = bar.dataset.percentage;
    bar.style.width = percentage + '%';
});