$(document).ready(function(){
    $(".list-notes").show();
    $(".notes-form").hide();

    $(".toggle-show-notes").click(function(){
      $(".notes-form").hide();
      $(".list-notes").show();
    });

    $(".toggle-create-notes").click(function(){
      $(".notes-form").show();
      $(".list-notes").hide();
    });


});