let buttonColors = ['red', 'blue', 'yellow', 'green'];
let gamePattern = [];
let userClickedPattern = []
let level = 0;
let started = false;

// QS = question

// make a rnadom number QS and Show it
function nextSequence() {
  let randomNumber = Math.floor(Math.random() * 4);
  let chosenRandomNumber = buttonColors[randomNumber];
  userClickedPattern = [];

  gamePattern.push(chosenRandomNumber);
  twingcle(chosenRandomNumber);
  playSound(chosenRandomNumber);

  level++;
  $("#level-title").text("Level " + level );
}

function twingcle(target) {
  $(`#${target}`).fadeTo(100, 0.3, function() { $(this).fadeTo(500, 1.0); });
}

function checkAnswer(index) {
  if(gamePattern[index] === userClickedPattern[index]) {
    if(gamePattern.length === userClickedPattern.length) {
      // Is last index ? 
      setTimeout(function () {
        nextSequence();
      }, 1000);
    }
  } else {
    $("body").addClass("game-over");
    $("#level-title").text("Game Over, Press Any Key to Restart");

    setTimeout(function () {
      $("body").removeClass("game-over");
    }, 200);
    playSound('wrong');
    startOver();
  }
} 

function startOver() {
  gamePattern = [];
  userClickedPattern = [];
  started = false;
  level = 0;
}

$("div.btn").on("click", function(evt) {
  let userChosenColor = $(this).attr("id");
  userClickedPattern.push(userChosenColor);
  playSound(userChosenColor);
  twingcle(userChosenColor);
  checkAnswer(userClickedPattern.length-1);
})

$(document).on("keydown", function(evt){
  let = target = '';
  
  // Check Game Start
  if(started == false) {
    started = true;
    nextSequence();
  }

  switch (evt.key) {
    case 'q':
      target = 'green';
      break;
    case 'w':
      target = 'red';
      break;
    case 'a':
      target = 'yellow';
      break;
    case 's':
      target = 'blue';
      break;
  }
  
  if(target) {
    userClickedPattern.push(target);
    playSound(target);
    twingcle(target);
    checkAnswer(userClickedPattern.length-1);
  }
})

function playSound(name) {
  var audio = new Audio(`/sounds/${name}.mp3`);
  audio.play();
}