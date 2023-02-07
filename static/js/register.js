var step = 1;

const buttonSubmit = $('#register-page form button[type="submit"]');

$('#register-page form button:not(button[type="submit"])').click((e) => {
  e.preventDefault();

  $("#register-page form").css("transform", `translate(-${step * 25}%)`);
  $("#register-page .progress-bar").css(
    "box-shadow",
    `inset ${step * 25}vw 0px #1c1c1c`
  );
  step++;
  $("#register-page").removeClass("dark");
});

buttonSubmit.click((e) => {
  e.preventDefault();
  $("#register-page .progress-bar").css(
    "box-shadow",
    `inset ${step * 25}vw 0px #1c1c1c`
  );

  buttonSubmit.submit();
});

const birthday = $("#birthday");
birthday.change();
birthday.change((e) => {
  console.log(birthday);
  if (!birthday.val()) {
    $("button.with-date").hide();
    $("button.empty-date").show();
  } else {
    $("button.empty-date").hide();
    $("button.with-date").show();
  }
});


$("form").submit(function (event) {
    
  });