
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


// Initial health bar width in pixels (starting at 150px)
let healthWidth = 150;

// Function to increase the width of the health bar
function increaseHealth() {
    const healthBar = document.getElementById('healthBar');
    const maxWidth = 300; // Maximum width of the health bar

    // Increase the width by 30px (or any increment you want)
    if (healthWidth < maxWidth) {
      healthWidth += 50;
      healthBar.style.width = healthWidth + 'px';
  } else {
      console.log('Health is already at maximum!');
  }
}
