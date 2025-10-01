// Salin dan tempel SELURUH kode ini ke static/js/main.js

console.log("File main.js berhasil dimuat.");

function loadCollection(type) {
  console.log(`---> Fungsi loadCollection() dipanggil dengan tipe: ${type}`);

  let url = '';
  if (type === 'all') {
    url = '/products/partial/all/';
  } else if (type === 'mine') {
    url = '/products/partial/mine/';
  } else {
    return;
  }

  const productContainer = document.getElementById('product-container');
  if (!productContainer) {
    console.error("KRITIS: Elemen dengan id='product-container' TIDAK DITEMUKAN!");
    return;
  }

  console.log(`Mengambil data dari URL: ${url}`);

  fetch(url)
    .then(response => response.text())
    .then(html => {
      console.log("Fetch berhasil. Mengganti isi #product-container.");
      productContainer.innerHTML = html;
    })
    .catch(error => {
      console.error('Terjadi error saat fetch:', error);
    });
}

console.log("Menambahkan event listener untuk DOMContentLoaded.");
document.addEventListener('DOMContentLoaded', () => {
  console.log("Event DOMContentLoaded terpicu! Memanggil loadCollection('all')...");
  loadCollection('all');
});