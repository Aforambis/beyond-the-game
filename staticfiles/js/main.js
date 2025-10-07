// ===================================================
// GLOBAL HELPER FUNCTIONS
// ===================================================

/**
 * Fetches and displays a collection of products based on the type.
 * @param {string} type - The type of collection to load ('all' or 'mine').
 * @param {HTMLElement} element - The navigation element that was clicked.
 */
function loadCollection(type, element) {
    const productContainer = document.getElementById('product-container');
    if (!productContainer) return;

    // Set the active filter style
    document.querySelectorAll('.product-filter-nav a[data-filter]').forEach(btn => btn.classList.remove('active-filter'));
    if (element) {
        element.classList.add('active-filter');
    }

    let url = '';
    if (type === 'all') {
        url = '/products/partial/all/';
    } else if (type === 'mine') {
        url = '/products/partial/mine/';
    } else {
        return;
    }

    fetch(url)
        .then(response => response.text())
        .then(html => {
            productContainer.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching the collection:', error);
            productContainer.innerHTML = '<p>Error loading products. Please try again.</p>';
        });
}

/**
 * Gets a cookie value by name.
 * @param {string} name - The name of the cookie.
 * @returns {string|null} The cookie value or null if not found.
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

/**
 * Handles the submission of the "Add Product" form via AJAX.
 * @param {Event} event - The form submission event.
 */
function handleAddFormSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('form-modal').classList.add('hidden');
            loadCollection('all', document.querySelector('a[data-filter="all"]'));
            alert(data.message); // You can replace this with a toast notification
        } else {
            // Re-render the form with validation errors
            document.getElementById('modal-body').innerHTML = data.form_html;
            document.getElementById('product-form').addEventListener('submit', handleAddFormSubmit);
        }
    });
}

// ===================================================
// MAIN SCRIPT EXECUTION (waits for page to load)
// ===================================================
document.addEventListener('DOMContentLoaded', () => {

    // --- Header & Navigation Logic ---
    const navbarToggle = document.getElementById('navbar-toggle');
    const navbarLinks = document.getElementById('navbar-links');
    if (navbarToggle && navbarLinks) {
        navbarToggle.addEventListener('click', (event) => {
            event.stopPropagation();
            navbarLinks.classList.toggle('active');
        });
    }

    // --- Modal Management ---
    const modal = document.getElementById('form-modal');
    const closeModalBtn = document.getElementById('close-modal-btn');
    if (modal && closeModalBtn) {
        closeModalBtn.addEventListener('click', () => {
            modal.classList.add('hidden');
            document.getElementById('modal-body').innerHTML = ''; // Clear modal
        });
    }

    // --- Add Product Button ---
    const addProductBtn = document.getElementById('add-product-btn');
    if (addProductBtn) {
        addProductBtn.addEventListener('click', () => {
            const addUrl = addProductBtn.dataset.addUrl;
            fetch(addUrl)
                .then(response => response.text())
                .then(html => {
                    document.getElementById('modal-title').textContent = 'Add New Product';
                    document.getElementById('modal-body').innerHTML = html;
                    modal.classList.remove('hidden');
                    document.getElementById('product-form').addEventListener('submit', handleAddFormSubmit);
                });
        });
    }

    // --- Product Filtering and Deletion (Event Delegation) ---
    const productContainer = document.getElementById('product-container');
    const productNav = document.querySelector('.product-filter-nav');

    if (productNav) {
        productNav.addEventListener('click', (event) => {
            if (event.target.matches('a[data-filter]')) {
                event.preventDefault();
                const filterType = event.target.getAttribute('data-filter');
                loadCollection(filterType, event.target);
            }
        });
    }

    if (productContainer) {
        productContainer.addEventListener('click', (event) => {
            if (event.target.classList.contains('delete-btn')) {
                const deleteUrl = event.target.dataset.deleteUrl;
                if (confirm("Are you sure you want to delete this product?")) {
                    fetch(deleteUrl, {
                        method: 'POST',
                        headers: { 'X-CSRFToken': csrftoken },
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            loadCollection('all', document.querySelector('a[data-filter="all"]'));
                            alert(data.message); // Replace with a toast notification
                        } else {
                            alert("Error: " + data.message);
                        }
                    });
                }
            }
        });
    }

    // --- Initial Load ---
    const allProductsButton = document.querySelector('a[data-filter="all"]');
    if (allProductsButton) {
        loadCollection('all', allProductsButton);
    }
});