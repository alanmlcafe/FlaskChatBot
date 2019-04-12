function checkInput() {
    var event = window.event || event.which;
	
	// Enter key 
    if (event.keyCode == 13) {
		var textInput = document.getElementById("textinput").value
        addUserLine(textInput);
        document.getElementById("textinput").value = "";
		$.ajax({
            url: '/process',
            data: {textinput: textInput},
            type: 'POST',
            success: function(response) {
                console.log(response);
				addBotLine(response)
            },
            error: function(error) {
                console.log(error);
				addBotLine("Hmm, something bad happened on my side, brb")
            }
        });
		
    }
}

// Add User Input
function addUserLine(line) {
    var textNode = document.createTextNode("USER: " + line);
	var elementConsoleText = document.getElementById("consoletext")
	
	// Line Break
	var br = document.createElement("br"); 
	elementConsoleText.appendChild(br);
	
    elementConsoleText.appendChild(textNode);
}

function addBotLine(line){
	var textNode = document.createTextNode("BOT: " + line);
	var elementConsoleText = document.getElementById("consoletext")
	
	// Line Break
	var br = document.createElement("br"); 
	elementConsoleText.appendChild(br);
	
    elementConsoleText.appendChild(textNode);
}