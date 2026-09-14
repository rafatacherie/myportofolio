let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

document.querySelectorAll('.skill-bar').forEach(bar => {
    const percentage = bar.dataset.percentage;
    bar.style.width = percentage + '%';
});