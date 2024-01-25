// script.js
document.addEventListener('DOMContentLoaded', function() {
    var messageBar = document.getElementById('message-bar');
    var messageText = document.getElementById('message-text');
    var closeButton = document.getElementById('close-button');
    var messagetext = messageText.textContent;

    // Display the message bar
    showMessage(messagetext, 3000); // 5000 milliseconds (5 seconds)
  
    // Close the message bar when the close button is clicked
    closeButton.addEventListener('click', function() {
      hideMessage();
      setTimeout(function() {
        // Redirect to the home page after the delay (adjust the time as needed)
        window.location.href = '/';
    }, 1000);
    });
  });
  
  function showMessage(message, duration) {
    var messageBar = document.getElementById('message-bar');
    var messageText = document.getElementById('message-text');
  
    messageText.innerText = message;
    messageBar.classList.remove('hidden');
  
    // Close the message bar after the specified duration
    setTimeout(function() {
      hideMessage();
    }, duration);
  }
  
  function hideMessage() {
    var messageBar = document.getElementById('message-bar');
    messageBar.classList.add('hidden');
  }
  