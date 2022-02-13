$(document).ready( () => {
  $("#loading").hide();

  $('#orderBySelect').on('change', () => {
    $("#loading").show();
    const method = $('#orderBySelect').val();
    $.ajax({ type: "POST", url: "/order/"+method,
      success: function (msg) {
        
        $("#orderBySelect").val(method);
        $("body").html(msg);
        $("#loading").hide();
      },
    });
  });
});