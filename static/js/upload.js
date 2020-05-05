function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    var imgEl = $('#preview');
    reader.onload = function(e) {
      imgEl.attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]); // convert to base64 string
    imgEl.css({
      display: "block",
      width: "300px",
      height: "100%",
      lineHeight: "170px",
      margin: "auto"
    })
    $("#helpText").css({display: "none"})
  }
}

$("#imageFile").change(function() {
  console.log('change')
  readURL(this);
});



console.log('file loaded');