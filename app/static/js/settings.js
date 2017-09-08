function addNewInputs(typeOfBox, typeOfInput){
    var newInput = document.createElement('input');
    var newLine = document.createElement('br');
    var inputBox = document.getElementById(typeOfBox);
    newInput.type = 'text';
    newInput.className = typeOfInput;
    inputBox.appendChild(newLine);
    inputBox.appendChild(newInput);
}

var savingTypes = {
    startSavingTypes: function(){
        this.startButton();
    },
    startButton: function(){
        var saveButton = document.getElementById('save-button');
        saveButton.addEventListener('click', savingTypes.saveData);
    },
    saveData: function(){
//        event.preventDefault();
        var newTypes = $('.type');
        var jsonArray = null;
        var arrayOfTypes = [];
        for (var i = 0; i < newTypes.length; i++){
            if(newTypes[i].value != ''){
                var jsonObject = '{"type":"' + newTypes[i].value+'"}';
                arrayOfTypes.push(jsonObject);
            }
        }
        jsonArray = JSON.stringify(arrayOfTypes);
        if(jsonArray.valueOf() != ''){
            $.ajax  ({
                type: 'POST',
                dataType : "json",
                contentType: "application/json",
                data: JSON.stringify(arrayOfTypes),
                error: function(){
                   alert('An error has occurred!')
                },
                success: function(){
                    newTypes.val('');
                }
            });
        }else{
            alert('Need to write something');
        }
    },
}

if('addEventListener' in document){
  document.addEventListener('deviceready', function(){
    savingTypes.startButton();
  }, false);
}