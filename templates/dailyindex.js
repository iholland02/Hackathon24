function paint(color,text) {
    const circle = document.getElementById('circleID');
    circle.style = `background-color:${color}`;
    circle.textContent = text;
  }