// Function to change the background color of the circle
function paint(color) {
  const circle = document.getElementById('circleID');
  circle.style.backgroundColor = color; // Set the background color properly
}

// Function to shake the image
function shakeImage() {
  const image = document.getElementById('imageID'); // Updated to match the correct ID
  
  // Add the shake class to the image
  image.classList.add('shake');
  
  // Remove the shake class after the animation ends to allow future triggers
  setTimeout(() => {
      image.classList.remove('shake');
  }, 500); // Match the animation duration (0.5s)
}
