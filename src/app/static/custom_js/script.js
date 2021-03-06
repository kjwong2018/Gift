
var arr = [];
var taglist = [];
var init = function(){
    sendRequest("question","/request");
}

function sendRequest(request,requestPort){
    var xhttp = new XMLHttpRequest();
    var s= "";
    if(request=="gift_please"){
        for(sr in taglist){
            s=s+","+taglist[sr];
        }
        request = s;
    }
    xhttp.open("POST",requestPort,true);
    xhttp.setRequestHeader("Content-type", "text/plain");
    xhttp.onreadystatechange = function(){
        if(this.readyState== 4 && this.status ==200){
            parseResponse(this);
        }
    }

    xhttp.send(request);
}
function parseResponse(xhttp){
    response = xhttp.responseText;
    parsedData = JSON.parse(response);
    if("question" in parsedData){
        generateQuestion(parsedData["question"]);
    }else if("request" in parsedData){
        generateGift(parsedData["request"]);
    }
}
function generateGift(gift){
    var con = document.getElementById("gift");
    con.className = "flex-display text-center";
    con.style.marginBottom = "50px";
    con.style.paddingBottom = "25px";
    for(x in gift){
        var wraper = document.createElement("div");
        wraper.className = "flex-items";
        var name = document.createElement("h3");
        var price = document.createElement("p");
        var image = document.createElement("img");
        image.style.width = "150px";
        var webLink = document.createElement("a");

        name.innerHTML = gift[x]["name"];
        price.innerHTML = "$"+gift[x]["price"]
        image.src = gift[x]["image"];
        webLink.innerHTML = "Check me out =>"+gift[x]["name"];
        webLink.href = gift[x]["link"];
        webLink.target = "_blank";
        wraper.style.padding = "50px";
        wraper.style.border = "5px solid white";

        wraper.appendChild(name);
        wraper.appendChild(price);
        wraper.appendChild(image);
        wraper.appendChild(webLink);
        con.appendChild(wraper);
    }
}
function initPage(ocassions){
    var answer = document.getElementById("answer-container");
    var questionContainer = document.getElementById("question-container");
    var question = createQuestion();
    var list = document.createElement("div");
    list.className = "flex-display";
    for(ocassion in ocassions){
        createOp(list,ocassions[ocassion]);
    }
    questionContainer.appendChild(question)
    answer.appendChild(list);
}
function createOp(answer,ocassion){
    var op = document.createElement("div");
    op.className = "flex-items";
    op.innerHTML = "<h3>"+ocassion+"</h3>";
    op.addEventListener("click",nextQuestion(arr,ocassion));
    answer.appendChild(op);
}
function nextQuestion(arr,ocassion){
    return function(){

        var question = document.getElementById("question");
        taglist.push(ocassion);
        clear(question);
        if(arr.length!=0){
            var elem = arr.pop(0);
            question.appendChild(elem);
        }else{
            var complete = createComplete(arr);
            question.appendChild(complete);
        }
    }
}
function createComplete(arr){
    var wraper = document.createElement("div");
    var text = document.createElement("h2");
    var check = document.createElement("button");
    var con = document.createElement("div");
    con.id = "gift";
    check.className = "btn btn-info";
    check.innerHTML = "Check Gifts!!!";
    text.innerHTML = "Status Completed";
    wraper.appendChild(text);
    wraper.appendChild(check);
    wraper.appendChild(con);
    sendRequest("gift_please","/complete");
    return wraper;
}
function clear(containner){
    while(containner.hasChildNodes()){
        containner.removeChild(containner.lastChild);
    }
}
function generateQuestion(questions){

    for(question in questions){
        var item = document.createElement("div");
        item.id = "questionC";
        var answer = document.createElement("div");
        answer.className = "answer-container";
        var questionContainer = document.createElement("div");
        questionContainer.className = "question-container";
        var question1 = createQuestion(questions[question]["Question"]);
        var list = document.createElement("div");
        list.className = "flex-display";
        for(ans in questions[question]["Answer"]){
            createOp(list,questions[question]["Answer"][ans]);
        }
        questionContainer.appendChild(question1);
        answer.appendChild(list);
        item.appendChild(questionContainer);
        item.appendChild(answer);
        item.style.position = "relative";
        item.style.opacity = "0.6";
        item.style.marginBottom = "20px";
        if (question==1){
            document.getElementById("question").appendChild(item);
        }else{
            arr.push(item);
        }
    }

}
function createQuestion(question){
    question = question || "What is this gift for?";
    if(question!=0){
        var ques = document.createElement("h2");
        ques.innerHTML = question+'<hr>';
        return ques;
    }

}















window.onload = init();
