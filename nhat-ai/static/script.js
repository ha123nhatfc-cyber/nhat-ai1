async function send(){

let input = document.getElementById("message")
let message = input.value

if(message === "") return

addMessage("Bạn: " + message, "user")

input.value=""

let response = await fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:message})
})

let data = await response.json()

addMessage("AI: " + data.reply, "ai")

}

function addMessage(text, type){

let chatbox=document.getElementById("chatbox")

let div=document.createElement("div")
div.className="message "+type
div.innerText=text

chatbox.appendChild(div)

chatbox.scrollTop = chatbox.scrollHeight

}
