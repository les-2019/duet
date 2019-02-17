"use strict";
var Outcomes = { LOST:-1, CONTINUE:0, WON:1};
var turnsLeft = 9;
  var agentsLeft = 15;
  var board = [];
/*
 use $.getJSON(url, data, success);  success
 Type: Function( PlainObject data, String textStatus, jqXHR jqXHR )
 A callback function that is executed if the request succeeds.
see https://api.jquery.com/jquery.getjson/ for example.
data["words","role1","role2"]
*/
  var words = ['rock', 'fact', 'bite', 'clam', 'quiet', 'front', 'oven', 'attack', 'stage', 'umbrella', 'snail', 'apparatus', 
               'friends', 'stocking', 'rub', 'smoke', 'cloth', 'milk', 'zephyr', 'hydrant', 'group', 'believe', 'lunchroom', 'north', 'arm'];
  var role1 = ['bystander','agent','agent','bystander','bystander','bystander','agent','bystander','assassin','bystander','agent','bystander',
               'assassin','assassin','agent','agent','agent','bystander','agent','bystander','bystander','bystander','bystander','agent','bystander'];
  var role2 = ['agent','agent','bystander','bystander','bystander','agent','agent','bystander','assassin','bystander','agent','bystander',
               'bystander','agent','bystander','assassin','bystander','bystander','bystander','agent','assassin','agent','agent','bystander','bystander'];

  var role1D = {};
  var role2D = {};
  var roleD = role2D;  // for example
//------------------------------------------------------------------
function Square(word, role1, role2) {
  this.word = word;
  this.role1 = role1;
  this.role2 = role2;
  this.exposed = false;
}
/*-----------------------------------------------------------------
|  reurn won:boolean
\-----------------------------------------------------------------*/
function agentHit(item) {
  $(item).addClass("agent");
  agentsLeft--;
  return (agentsLeft == 0);
}
//------------------------------------------------------------------
function bystanderHit(item) {
  $(item).addClass("bystander");
}
//------------------------------------------------------------------
function assassinHit(item) {
  $(item).addClass("assassin");
  alert("Game is Lost");
}
/* /------------------------------------------------------------------
   |  return outcome:Outcomes (WON, LOST, CONTINUE) and endTurn:boolean
   \------------------------------------------------------------------*/
function squareHit(event) {
    var endTurn = true;
    var outcome = Outcomes.CONTINUE;
    var item = event.target;
    $(this).removeClass('unexposed');
    console.log($(this).classList);
    var word = $(this).text()
    console.log(word);
    
    switch(roleD[word]) {
        case 'agent':
           endTurn = false;
           if (agentHit(item)) {
             outcome = Outcomes.WON;
           }
           break;
        case 'assassin':
           assassinHit(item);
           outcome = Outcomes.LOST;
           break;
        case 'bystander':
           bystanderHit(item);
           break;
        default:
           console.log('invalid role');
           break;
    }        
   $(this).prop('disabled', true);
   return { endTurn:endTurn, outcome:outcome };
//  
}
/*------------------------------------------------------------------
    returns isSpymaster
*------------------------------------------------------------------*/
function makeBoard() {
  var i = 0;
  words.forEach(function(word,i) {
    board.push(new Square(word, role1[i], role2[i]));
    square = $('.item'+ (i+1)).first();
    square.addClass("unexposed");
    square.text(word);
    role1D[word] = role1[i];
    role2D[word] = role2[i];
  });
     
  $('.item').click(squareHit);
  return roleD == role1D;
}
//------------------------------------------------------------------
$(document).ready(function() {
  isSpymaster = makeBoard();
  while (roleD == role1D) {
       spymaster();
  } 
  while (roleD == role2D) {
        player();
  }
});
