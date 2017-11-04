


var init = function(){
    sendRequest("init","/init");
}

function sendRequest(request,requestPort){
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST",requestPort,true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.onreadystatechange = function(){
        if(this.readyState== 4 && this.status ==200){

            initPage(this);
        }
    }

    xhttp.send(request)
}
function initPage(xhttp){
    response = xhttp.responseText;
    occasion = JSON.parse(response);
    console.log(occasion);
}















window.onload = init();