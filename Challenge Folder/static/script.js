'use static'
toastr.options = {
  "closeButton": true,
  "progressBar": true,
  "positionClass": "toast-bottom-center",
  "timeOut": "10000",
  "extendedTimeOut": "1000",
}

function indexGo() {
  location.assign('/test/' + document.getElementById('items').value +'?person=james');
  $('#coding-time').show();
}

function keyDown() {
  if(event.keyCode == 13){document.getElementById('go').click()}
}
