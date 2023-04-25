# SVG Parrot Drawing.

#### You:
Draw a Parrot using SVG

#### ChatGPT:
As an AI language model, I cannot directly draw images. However, I can help you create a simple SVG representation of a parrot. You can copy and paste the code below into an HTML file and open it in a web browser to see the parrot.

Please note that this is a very basic representation, and you might want to modify it or search for more advanced examples to meet your specific requirements.

```html
<!DOCTYPE html>
<html>
<head>
<style>
    svg {
        width: 200px;
        height: 200px;
    }
</style>
</head>
<body>
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <!-- Body -->
    <ellipse cx="50" cy="50" rx="30" ry="40" fill="green" />
    
    <!-- Head -->
    <circle cx="50" cy="20" r="15" fill="green" />
    
    <!-- Eye -->
    <circle cx="45" cy="18" r="3" fill="white" />
    
    <!-- Beak -->
    <polygon points="50,25 60,25 50,30" fill="orange" />
    
    <!-- Wing -->
    <path d="M 30 50 Q 50 40 70 50 L 70 65 Q 50 60 30 65 Z" fill="darkgreen" />
    
    <!-- Tail -->
    <polygon points="50,90 40,70 60,70" fill="darkgreen" />
</svg>
</body>
</html>
```

This code creates a simple parrot shape using SVG elements such as circles, ellipses, polygons, and paths. You can further customize the colors and shapes to make it look more like the parrot you have in mind.


#### You:
Write a program that relies on this basic "template" and is capable of customizing the parot with different colors and shapes. Implement the program with 10 variables whose values can be changed. Generate 100 random variants by randomly setting values to the 10 variables.

#### ChatGPT:
I'll provide you with a simple JavaScript program that generates random parrot SVGs based on the provided template. The program uses 10 variables to customize the parrot's colors and shapes. The variables control the colors of the body, head, wing, tail, and beak, and the dimensions of the body, head, wing, and tail.

You can copy and paste the code below into an HTML file and open it in a web browser to see the random parrots generated:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random Parrots</title>
  <style>
    .parrot {
      display: inline-block;
      width: 100px;
      height: 100px;
    }
  </style>
</head>
<body>
  <script>
    function randomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }

    function randomParrot() {
      const bodyColor = randomColor();
      const headColor = randomColor();
      const wingColor = randomColor();
      const tailColor = randomColor();
      const beakColor = randomColor();

      const bodySizeX = 20 + Math.floor(Math.random() * 20);
      const bodySizeY = 30 + Math.floor(Math.random() * 20);
      const headSize = 10 + Math.floor(Math.random() * 10);
      const wingSize = 20 + Math.floor(Math.random() * 20);
      const tailSize = 10 + Math.floor(Math.random() * 20);

      return `
        <svg class="parrot" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <!-- Body -->
          <ellipse cx="50" cy="50" rx="${bodySizeX}" ry="${bodySizeY}" fill="${bodyColor}" />
          <!-- Head -->
          <circle cx="50" cy="20" r="${headSize}" fill="${headColor}" />
          <!-- Eye -->
          <circle cx="45" cy="18" r="3" fill="white" />
          <!-- Beak -->
          <polygon points="50,25 60,25 50,30" fill="${beakColor}" />
          <!-- Wing -->
          <path d="M 30 50 Q 50 40 70 50 L 70 ${50 + wingSize} Q 50 ${50 + wingSize / 2} 30 ${50 + wingSize} Z" fill="${wingColor}" />
          <!-- Tail -->
          <polygon points="50,90 40,${90 - tailSize} 60,${90 - tailSize}" fill="${tailColor}" />
        </svg>`;
    }

    for (let i = 0; i < 100; i++) {
      document.body.innerHTML += randomParrot();
    }
  </script>
</body>
</html>
```

This code defines a `randomColor` function that generates random colors and a `randomParrot` function that generates an SVG parrot with random colors and shapes based on the 10 variables. Finally, it generates 100 random parrots and appends them to the document body.


#### You:
can you animate the 100 SVG, giving the impression to fly with the different parots?

#### ChatGPT:
Sure! Here's a modified version of the previous code that animates the parrots, giving the impression of flying. This is achieved by adding a simple up and down animation to the parrots using CSS keyframes:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random Animated Parrots</title>
  <style>
    .parrot {
      display: inline-block;
      width: 100px;
      height: 100px;
      animation: fly 1s infinite alternate;
      transform-origin: center;
    }

    .parrot:nth-child(even) {
      animation-direction: alternate-reverse;
    }

    @keyframes fly {
      0% {
        transform: translateY(0);
      }
      100% {
        transform: translateY(-5px);
      }
    }
  </style>
</head>
<body>
  <script>
    function randomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }

    function randomParrot() {
      const bodyColor = randomColor();
      const headColor = randomColor();
      const wingColor = randomColor();
      const tailColor = randomColor();
      const beakColor = randomColor();

      const bodySizeX = 20 + Math.floor(Math.random() * 20);
      const bodySizeY = 30 + Math.floor(Math.random() * 20);
      const headSize = 10 + Math.floor(Math.random() * 10);
      const wingSize = 20 + Math.floor(Math.random() * 20);
      const tailSize = 10 + Math.floor(Math.random() * 20);

      return `
        <svg class="parrot" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <!-- Body -->
          <ellipse cx="50" cy="50" rx="${bodySizeX}" ry="${bodySizeY}" fill="${bodyColor}" />
          <!-- Head -->
          <circle cx="50" cy="20" r="${headSize}" fill="${headColor}" />
          <!-- Eye -->
          <circle cx="45" cy="18" r="3" fill="white" />
          <!-- Beak -->
          <polygon points="50,25 60,25 50,30" fill="${beakColor}" />
          <!-- Wing -->
          <path d="M 30 50 Q 50 40 70 50 L 70 ${50 + wingSize} Q 50 ${50 + wingSize / 2} 30 ${50 + wingSize} Z" fill="${wingColor}" />
          <!-- Tail -->
          <polygon points="50,90 40,${90 - tailSize} 60,${90 - tailSize}" fill="${tailColor}" />
        </svg>`;
    }

    for (let i = 0; i < 100; i++) {
      document.body.innerHTML += randomParrot();
    }
  </script>
</body>
</html>
```

In this code, I added a CSS animation called `fly` that moves the parrots up and down. The parrots are animated using the `animation` property with `1s` duration and `infinite` loop. The `alternate` value makes the animation reverse direction on every iteration, creating an up and down movement.
