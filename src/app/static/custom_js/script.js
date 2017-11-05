


var init = function(){
    sendRequest("init","/request");
}

function sendRequest(request,requestPort){
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST",requestPort,true);
    // xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.onreadystatechange = function(){
        if(this.readyState== 4 && this.status ==200){
            parseResponse(this);
        }
    }

    xhttp.send(request)
}
function parseResponse(xhttp){
    response = xhttp.responseText;
    parsedData = JSON.parse(response);
    if(parsedData.keys()[0]=="init"){
        initPage(parsedData["init"]);
    }
}
function initPage(ocassions){
    for(ocassion in ocassions){
        alert(ocassion);
    }

    // occasion = JSON.parse(response);

}















window.onload = init();
