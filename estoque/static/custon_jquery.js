$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-category").modal("show");
      },
      success: function (data) {
        $("#modal-category .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list);
          $("#modal-category").modal("hide");
        }
        else {
          $("#modal-category .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-category").click(loadForm);
  $("#modal-category").on("submit", ".js-book-create-form", saveForm);

  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
  $("#modal-category").on("submit", ".js-book-update-form", saveForm);

  // Delete book
  $("#book-table").on("click", ".js-delete-book", loadForm);
  $("#modal-category").on("submit", ".js-book-delete-form", saveForm);

});

$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-produto").modal("show");
      },
      success: function (data) {
        $("#modal-produto .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#produto-table tbody").html(data.html_book_list);
          $("#modal-produto").modal("hide");
        }
        else {
          $("#modal-produto .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create produto
  $(".js-create-produto").click(loadForm);
  $("#modal-produto").on("submit", ".js-produto-create-form", saveForm);
  // Update produto
  $("#produto-table").on("click", ".js-update-produto", loadForm);
  $("#modal-produto").on("submit", ".js-produto-update-form", saveForm);
  // Delete produto
  $("#produto-table").on("click", ".js-delete-produto", loadForm);
  $("#modal-produto").on("submit", ".js-produto-delete-form", saveForm);
  
});
