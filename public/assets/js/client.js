// const hostName = "https://rdhaliwa97-services.000webhostapp.com";
// const hostName = "http://localhost:8080";
document.querySelector('.menu_toggle').addEventListener('click',()=>{
  document.querySelector('.page').classList.toggle("shazam");
});

document.querySelector('.content').addEventListener('click',()=>{
  document.querySelector('.page').classList.remove("shazam");
});

document.querySelector('span.cross-button').addEventListener('click', ()=>{
  document.documentElement.style.setProperty('--modal-visibility', 'hidden');
});

document.querySelector('.menu_items a').addEventListener('click', ()=>{
  document.documentElement.style.setProperty('--modal-visibility', 'visible');
});

(function() {
  let methodArray = ['GET', 'POST', 'PUT', 'DELETE'];
  let reqBody = { req: 'xyz' };
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function(){
    if(this.readyState == 4 && this.status ==200){
      // console.log(xhr.getAllResponseHeaders());
      console.log(JSON.parse(xhr.response));
    }
  }
  xhr.open(methodArray[Math.floor(Math.random() * methodArray.length)], `/api/xyz`, "true");
  // xhr.open("DELETE", `http://localhost:8080/api/xyz`, "true");
  xhr.setRequestHeader('Access-Control-Allow-Origin', '*')
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send(JSON.stringify(reqBody));
}());
