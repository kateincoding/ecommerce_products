$(document).ready(loadCategories);
$(document).ready(main);
const HOST = 'test.katein.tech';
const checksCategories = {};
let categoryId = "0";

function main () {
  readCategories();
  allData();
  $(':button').click(function () {
    readCategories();
    dataUsers();
  });
}

function allData () {
  const url = `http://${HOST}/api/v1/products`;
  $.get(url, function (data) {
    $('.products').empty();
    for (const product of data) {
      $('section.products').append(`<article>
      <div class="title_box">
        <h2>${product.name}</h2>
        <div class="price_by_night">$${product.price}</div>
      </div>
      <div class="information">
        <img src="${product.url}" alt="${product.name}" width="100" height="70" >
      </div>
      </article>`);
    }
  });
}

function dataUsers () {
  const url = `http://${HOST}/api/v1/products/category/${categoryId}`;
  $.get(url, function (data) {
    $('.products').empty();
    for (const product of data) {
      $('section.products').append(`<article>
      <div class="title_box">
        <h2>${product.name}</h2>
        <div class="price_by_night">$${product.price}</div>
      </div>
      <div class="information">
        <img src=${product.url} alt="${product.name}" width="100" height="70" >
      </div>
      </article>`);
    }
  });
}

function readCategories () {
  $('.category_box').change(function () {
    console.log("estoy aqui")
    if ($(this).is(':checked')) {
      checksCategories[$(this).attr('data-name')] = $(this).attr('data-id');
      categoryId = $(this).attr('data-id');
    } else {
      delete checksCategories[$(this).attr('data-name')];
    }
     const namesh4 = Object.keys(checksCategories);
     $('.h4_categories').text(namesh4.sort().join(', '));
  });
}

function loadCategories () {
  const url = `http://${HOST}/api/v1/categories`;
  $.get(url, function (data) {
    for (const category of data) {
      $('section.categoriesfilters').append(`
        <li><input type="checkbox" style="margin-right: 10px" data-id="${category.id}" data-name="${category.name}" class="category_box">${category.name}</li>
      `);
    }
  });
}
