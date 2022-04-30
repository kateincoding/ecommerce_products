$(document).ready(main);
const HOST = '0.0.0.0';
const checksCategories = {};
let categoryId = "0";

function main () {
  readCategories();
  dataUsers();
  $(':button').click(function () {
      dataUsers();
  });
}

function dataUsers () {
  const url = `http://${HOST}:5001/api/v1/products/category/${categoryId}`;
  console.log("fin");
  $.get(url, function (data) {
    console.log("hola mundo");
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

function readCategories () {
  $('.categories .popover INPUT[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) {
      console.log("heheheheheh")
      checksCategories[$(this).attr('data-name')] = $(this).attr('data-id');
      categoryId = $(this).attr('data-id');
    } else {
      delete checksCategories[$(this).attr('data-name')];
    }
    const namesh4 = Object.keys(checksCategories);
    $('.h4_categories').text(namesh4.sort().join(', '));
  });
}
