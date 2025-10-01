function loadCollection(type) {
  let url = '';
  if (type === 'all') url = '/products/partial/all/';
  if (type === 'mine') url = '/products/partial/mine/';

  fetch(url)
    .then(response => response.text())
    .then(html => {
      document.getElementById('product-container').innerHTML = html;
      document.getElementById('collection-section').scrollIntoView({ behavior: "smooth" });
    });
}
