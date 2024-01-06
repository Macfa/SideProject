var buttonsLength = document.querySelectorAll('button').length;

for (let index = 0; index < buttonsLength; index++) {
  document.querySelectorAll(".drum")[index].addEventListener("click", function(e) {
    var htmlStatement = this.innerHTML;
    
    handleclick(htmlStatement);
  })
}

document.addEventListener('keydown', (e) => {
  let key = e.key;
  console.log(key);
  handleclick(key);
});

function handleclick(element) {
  var audio = '';

  switch(element) {
    case 'w': 
      audio = new Audio("./sounds/crash.mp3");
      break;
    case 'a': 
      audio = new Audio("./sounds/kick-bass.mp3");
      break;
    case 's': 
      audio = new Audio("./sounds/snare.mp3");
      break;
    case 'd': 
      audio = new Audio("./sounds/tom-1.mp3");
      break;
    case 'j': 
      audio = new Audio("./sounds/tom-2.mp3");
      break;
    case 'k': 
      audio = new Audio("./sounds/tom-3.mp3");
      break;
    case 'l': 
      audio = new Audio("./sounds/tom-4.mp3");
      break;
  }

  audio.play(); // sound1.mp3 재생
  // return audio;
}