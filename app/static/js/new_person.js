/*
JavaScript to send new person data to backend
@author nano-bytes and signare
*/

//Function that sends a message to backend
$(function(){$('#maintenance-form').on('submit', function(event){
    event.preventDefault();
    $.ajax({
        url: '/hominem/new_person/',
        type: 'POST',
        data: dataOfNewPerson(),
        dataType: 'json',
        error: function(){
            $('#dni-number').val('');
        },
        success: function(){
            alert('Datos Grabados Correctamente!');
        }
    });
});});

function dataOfNewPerson(){
return {dniType: $('#dni-type').val(), dni: $('#dni-number').val(), nationality: $('#nationality').val(),
personType: $('#person-type').val(), name: $('#name').val(), lastName: $('#last-name').val(), addressType: $
('#address-type').val(), address: $('#address').val(), principalAddress: $('#principal-address').val(), phoneType: $
('#phone-type').val(), phoneNumber: $('phone-number').val(), principalPhone: $('#principal-phone').val(), emailAddress:
$('#email-address').val(), principalEmail: $('#principal-email').val()};
}

//var csrftoken = getCookie('csrftoken');
var csrftoken = $.cookie('visit');
function tokenSafe(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings){
        if(!tokenSafe(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});