function toggleMenu(event) {
    const menu = event.target.closest('.file-row').querySelector('.dropdown-menu');
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block';
}

document.addEventListener('click', function(event) {
    if (!event.target.closest('.file-row')) {
        const menus = document.querySelectorAll('.dropdown-menu');
        menus.forEach(menu => menu.style.display = 'none');
    }
});