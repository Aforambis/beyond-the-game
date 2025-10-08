// --- Fungsi Utama untuk Setup Halaman ---
document.addEventListener('DOMContentLoaded', () => {

    // ===================================================
    // BAGIAN 1: SETUP UNTUK INTERAKSI HEADER & NAVIGASI
    // ===================================================

    // --- Logika untuk Hamburger Menu (Dropdown di Kiri) ---
    const navbarToggle = document.getElementById('navbar-toggle');
    const navbarLinks = document.getElementById('navbar-links');

    if (navbarToggle && navbarLinks) {
        navbarToggle.addEventListener('click', function(event) {
            event.preventDefault();
            navbarLinks.classList.toggle('active');
        });
    }

    // --- Logika untuk User Icon Dropdown (di Kanan) ---
    const userIconTrigger = document.querySelector('.user-icon');
    const userDropdown = document.getElementById('user-dropdown');

    if (userIconTrigger && userDropdown) {
        userIconTrigger.addEventListener('click', function(event) {
            event.preventDefault();
            userDropdown.classList.toggle('active');
        });
    }

    // Menutup kedua dropdown jika user mengklik di luar area header
    document.addEventListener('click', function(event) {
        const header = document.querySelector('.main-header');
        if (header && !header.contains(event.target)) {
            if (navbarLinks) navbarLinks.classList.remove('active');
            if (userDropdown) userDropdown.classList.remove('active');
        }
    });


    // ===================================================
    // BAGIAN 2: EFEK VISUAL
    // ===================================================

    // --- Efek Header menjadi Solid saat di-scroll ---
    const mainHeader = document.querySelector('.main-header');
    if (mainHeader) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                mainHeader.classList.add('scrolled');
            } else {
                mainHeader.classList.remove('scrolled');
            }
        });
    }

    // --- Efek Smooth Scrolling untuk link anchor (#) ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetElement = document.querySelector(this.getAttribute('href'));
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });


    // ===================================================
    // BAGIAN 3: LOGIKA FILTER PRODUK
    // ===================================================
    const productNav = document.querySelector('.product-filter-nav');
    if (productNav) {
        const filterButtons = productNav.querySelectorAll('a[data-filter]');
        filterButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const filterType = this.getAttribute('data-filter');
                loadCollection(filterType, this);
            });
        });

        const allProductsButton = productNav.querySelector('a[data-filter="all"]');
        if (allProductsButton) {
            loadCollection('all', allProductsButton);
        }
    }

    // ===================================================
    // BAGIAN 4: LOGIKA UNTUK FORM DINAMIS (KODE BARU)
    // ===================================================
    const categorySelect = document.getElementById('id_category');
    const clubLabel = document.querySelector('label[for="id_club"]');
    const playerLabel = document.querySelector('label[for="id_player"]');

    const checkCategory = () => {
        if (!categorySelect || !clubLabel || !playerLabel) return;

        const selectedCategory = categorySelect.value;
        if (selectedCategory === 'jersey' || selectedCategory === 'shoes') {
            clubLabel.classList.add('is-required');
            playerLabel.classList.add('is-required');
        } else {
            clubLabel.classList.remove('is-required');
            playerLabel.classList.remove('is-required');
        }
    };

    if (categorySelect) {
        categorySelect.addEventListener('change', checkCategory);
        checkCategory();
    }
});

function showLoading(targetId) {
  const el = document.getElementById(targetId);
  if (el) el.innerHTML = "<p class='text-center text-gray-500'>Loading...</p>";
}

// --- FUNGSI UNTUK LOAD KOLEKSI PRODUK (KODE ASLI KAMU, TIDAK DIUBAH) ---
function loadCollection(type, element) {
    const productContainer = document.getElementById('product-container');
    if (!productContainer) { return; }

    const filterButtons = document.querySelectorAll('.product-filter-nav a[data-filter]');
    if (filterButtons) {
        filterButtons.forEach(btn => btn.classList.remove('active-filter'));
    }
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

    showLoading("product-container")
    fetch(url)
        .then(response => response.text())
        .then(html => {
            productContainer.innerHTML = html;
            if (html.includes("You haven't added any products")) {
                productContainer.classList.add('is-empty');
            } else {
                productContainer.classList.remove('is-empty');
            }
        })
        .catch(error => console.error('Error fetching the collection:', error));
}

function toggleModal(id) {
  document.getElementById(id).classList.toggle("hidden");
}

document.getElementById("loginBtn")?.addEventListener("click", async () => {
  const username = document.getElementById("login-username").value;
  const password = document.getElementById("login-password").value;

  const res = await fetch("/api/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
    },
    body: JSON.stringify({ username, password }),
  });

  const data = await res.json();
  showToast(data.message, data.success ? "success" : "error");
  if (data.success) location.reload();
});

document.getElementById("registerBtn")?.addEventListener("click", async () => {
  const username = document.getElementById("reg-username").value;
  const password = document.getElementById("reg-password").value;
  const password2 = document.getElementById("reg-password2").value;

  const res = await fetch("/api/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
    },
    body: JSON.stringify({ username, password, password2 }),
  });

  const data = await res.json();
  showToast(data.message, data.success ? "success" : "error");
  if (data.success) toggleModal("registerModal");
});

document.getElementById("refresh-products")?.addEventListener("click", (e) => {
  const url = e.target.dataset.refreshUrl;
  const container = document.getElementById("product-container");
  container.innerHTML = "<p class='text-gray-500 text-center'>Refreshing...</p>";
  htmx.ajax('GET', url, { target: "#product-container" });
});

function openEditModal(id) {
    // Get the modal elements you already have in main.html
    const modal = document.getElementById("form-modal");
    const modalTitle = document.getElementById("modal-title");
    const modalBody = document.getElementById("modal-body");

    // The new URL we just created
    const url = `/get-edit-form/${id}/`;

    // Set the title and show the modal
    modalTitle.textContent = "Edit Product";
    modal.classList.remove("hidden");
    modal.classList.add("flex");
    
    // Use HTMX to fetch the form and inject it into the modal's body
    htmx.ajax('GET', url, { target: modalBody });
}

async function submitEdit(id) {
    const name = document.getElementById("edit-name").value;
    const price = document.getElementById("edit-price").value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Make sure to get CSRF token

    // The edit URL from your urls.py is /products/<id>/edit/
    const res = await fetch(`/products/${id}/edit/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ name, price }),
    });

    const data = await res.json();
    showToast(data.message, data.status === "success" ? "success" : "error");
    document.getElementById("editModal").remove();

    // Refresh the product list
    const refreshBtn = document.getElementById("refresh-products");
    const url = refreshBtn?.dataset.refreshUrl;
    if (url) {
        htmx.ajax('GET', url, { target: "#product-container" });
    }
}