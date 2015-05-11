'use strict';

var clickHandlers = {
  'button1': function() {
    var request = window.navigator.mozApps.getSelf();
    var result = {};
    var result_status = true;
    var error_msg = "";

    request.onsuccess = function() {
      result['manifest'] = request.result['manifest'];
      result['origin'] = request.result['origin'];
      console.log("[mcts] app name: " + result['manifest']['name']);
      console.log("[mcts] app description: " + result['manifest']['description']);
      
      if (result['manifest']['name'] != "MCTS prototype") {
        error_msg += "Wrong name: " + result['manifest']['name'];
        result_status = false;
      }
      if (result['manifest']['description'] != "MCTS app") {
        error_msg += "Wrong description: " + result['manifest']['description'];
        result_status = false;
      }
      if (result_status) {
        alert("PASS");
      }
      else {
        alert("FAIL\n" + error_msg);
      }
    };
    request.onerror = function() {
        alert(prompt("Error", request.error.name));
    };
  },
  'button21': function() {
    alert('Hello world!');
  },
  'button22': function() {
    alert(confirm('Hello world?'));
  },
  'button23': function() {
    alert(prompt('Hello world:', 'initial value'));
  },
  'button31': function() {
    var msg = 'Hello world!1\n2\n3\n4\n5\n6\n7\n8\n9';
    msg += '\n10\n11\n12\n13\n14\n15\n16\n17\n18\n';
    alert(msg);
  },
  'button32': function() {
    var msg = 'Hello world!1\n2\n3\n4\n5\n6\n7\n8\n9';
    msg += '\n10\n11\n12\n13\n14\n15\n16\n17\n18\n';
    alert(confirm(msg));
  },
  'button33': function() {
    var msg = 'Hello world!1\n2\n3\n4\n5\n6\n7\n8\n9';
    msg += '\n10\n11\n12\n13\n14\n15\n16\n17\n18\n';
    alert(prompt(msg));
  }
};

document.body.addEventListener('click', function(evt) {
  if (clickHandlers[evt.target.id])
    clickHandlers[evt.target.id].call(this, evt);
});
