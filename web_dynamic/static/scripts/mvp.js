$(document).ready(main);
const HOST = '0.0.0.0';
const checksCategories = {};

function main () {
  /* readCategories(); */
  dataUsers();
  /* $(':button').click(function () {
      dataUsers();
  }); */
}

function dataUsers () {
  const url = `http://${HOST}:5001/api/v1/products/category/5`;
  console.log("fin");
  $.get(url, function (data) {
    console.log("hola mundo");
    //$('.products').empty();
    for (const product of data) {
      $('section.products').append(`<article>
      <div class="title_box">
        <h2>${product.name}</h2>
        <h3>holaaaaa</h3>
      </div>
      </article>`);
    }
  });
}