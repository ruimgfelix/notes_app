$(document).ready( () => {

  $("#loading").hide();

  $('#orderBySelect').on('change', () => {
    $("#loading").show();
    const method = $('#orderBySelect').val();
    $.ajax({ type: "POST", url: "/order/"+method,
      success: function (msg) {
        $("body").html(msg);
        $("#loading").hide();
        $("#orderBySelect").val(method);
      },
    });
  });

  $('#formSearch').on('submit', () => {
    $("#loading").hide();
  });
  
});