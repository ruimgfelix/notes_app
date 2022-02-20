$(document).ready( () => {

  hideValidations();
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

  $('#modalConfirmButtonCreate').on('click', () => {
    $("#loading").show();
    validationsPassed = doValidations();
    if (validationsPassed) {
      $("#editCreateForm").submit();
    } else {
      $("#modalConfirmButtonCreateClose").click();
    }
    $("#loading").hide();
    
  });

  function doValidations() {
    validationsPassed = true;
    if ($("#inputNoteTitle").val() == "") {
      validationsPassed = false;
      $("#inputNoteTitleError").show();
      $("#inputNoteTitle").css("border", "red solid 1px");
    }
    if ($("#inputNoteDescription").val() == "") {
      validationsPassed = false;
      $("#inputNoteDescriptionError").show();
      $("#inputNoteDescription").css("border", "red solid 1px");
    }
    if ($("#noteTitle option:selected").val() == "") {
      validationsPassed = false;
      $("#noteTitleError").show();
      $("#noteTitle").css("border", "red solid 1px");
    }
    return validationsPassed
  }

  function hideValidations() {
    $("#inputNoteTitleError").hide();
    $("#inputNoteDescriptionError").hide();
    $("#noteTitleError").hide();
    $("#inputNoteTitle").css("border", "1px solid #ced4da");
    $("#inputNoteDescription").css("border", "1px solid #ced4da");
    $("#noteTitle").css("border", "1px solid #ced4da");
  }
  
});