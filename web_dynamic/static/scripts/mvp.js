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
  $.get(url, function (data, txtStatus) {
    console.log("hola mundo");
    //$('.products').empty();
    // console.log(data);
  });
}