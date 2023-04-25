# Unleash JS Feature Toggles.

#### You:
Write a configurable Javascript program that implements four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc. The four features should be implemented as feature toggles. I'd like to use  Unleash, a feature toggle service, integrated with Gitlab

#### ChatGPT:
To implement a configurable JavaScript program using feature toggles with Unleash integrated with GitLab, you'll need to follow these steps:

1. Set up Unleash
2. Create feature toggles for the four features
3. Integrate Unleash with GitLab
4. Write a JavaScript program to utilize the feature toggles

First, let's assume you have set up Unleash and integrated it with GitLab. You can follow the official guide here: <https://docs.gitlab.com/ee/integration/unleash.html>

Next, create the four feature toggles in Unleash: `hello`, `beautiful`, `wonderful`, and `world`.

Now, let's write the JavaScript program. You'll need to install the `unleash-client` package:

```bash
npm install unleash-client
```

Now, create a file named `index.js` and add the following code:

```javascript
const { initialize } = require('unleash-client');

const unleash = initialize({
  appName: 'my-app-name',
  instanceId: 'my-instance-id',
  url: 'https://unleash.example.com/api/',
});

function printFeatures() {
  let output = '';

  if (unleash.isEnabled('hello')) {
    output += 'Hello';
  }

  if (unleash.isEnabled('beautiful')) {
    output += (output ? ' ' : '') + 'Beautiful';
  }

  if (unleash.isEnabled('wonderful')) {
    output += (output ? ' ' : '') + 'Wonderful';
  }

  if (unleash.isEnabled('world')) {
    output += (output ? ' ' : '') + 'World';
  }

  console.log(output);
}

unleash.on('ready', printFeatures);
unleash.on('update', printFeatures);
```

Replace `my-app-name`, `my-instance-id`, and `https://unleash.example.com/api/` with the appropriate values for your setup.

The code above initializes the Unleash client and listens for the `ready` and `update` events to print the enabled features. The `printFeatures` function checks if the feature toggles are enabled and prints the corresponding words.

Run the program with:

```bash
node index.js
```

This will print the enabled features according to the feature toggle configuration in Unleash. When you update the feature toggle configuration, the output will change accordingly.


#### You:
would it be possible to adapt the program as a Web application... and provide a server-side that returns the output while the client side prints it

#### ChatGPT:
Sure, we can adapt the program as a web application using Node.js and Express for the server-side, and plain HTML and JavaScript for the client-side.

First, install the required packages:

```bash
npm init -y
npm install express unleash-client cors
```

Now, create a file named `server.js` and add the following code:

```javascript
const express = require('express');
const { initialize } = require('unleash-client');
const cors = require('cors');

const app = express();
const unleash = initialize({
  appName: 'my-app-name',
  instanceId: 'my-instance-id',
  url: 'https://unleash.example.com/api/',
});

app.use(cors());

app.get('/features', (req, res) => {
  let output = '';

  if (unleash.isEnabled('hello')) {
    output += 'Hello';
  }

  if (unleash.isEnabled('beautiful')) {
    output += (output ? ' ' : '') + 'Beautiful';
  }

  if (unleash.isEnabled('wonderful')) {
    output += (output ? ' ' : '') + 'Wonderful';
  }

  if (unleash.isEnabled('world')) {
    output += (output ? ' ' : '') + 'World';
  }

  res.json({ output });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Replace `my-app-name`, `my-instance-id`, and `https://unleash.example.com/api/` with the appropriate values for your setup.

Now, create a file named `index.html` and add the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Feature Toggles Web App</title>
</head>
<body>
  <h1>Enabled Features:</h1>
  <div id="output"></div>

  <script>
    async function fetchFeatures() {
      const response = await fetch('http://localhost:3000/features');
      const data = await response.json();
      document.getElementById('output').innerText = data.output;
    }

    fetchFeatures();
  </script>
</body>
</html>
```

To run the server, execute:

```bash
node server.js
```

Open `index.html` in a browser to see the enabled features. Note that the server runs on `http://localhost:3000` by default. Make sure to adjust the URL in `index.html` if needed.

This setup provides a server-side API for fetching the enabled features, while the client-side JavaScript fetches the data and displays it on the page.


#### You:
can you adapt the client code in such a way all features come with a clicked (or not) box as well as the overall output message

#### ChatGPT:
Certainly! To achieve this, we'll update the client-side code to include checkboxes for each feature and a button to update the output message based on the selected checkboxes.

Update the `index.html` file with the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Feature Toggles Web App</title>
</head>
<body>
  <h1>Select Features:</h1>
  <div>
    <input type="checkbox" id="hello" name="hello">
    <label for="hello">Hello</label>
  </div>
  <div>
    <input type="checkbox" id="beautiful" name="beautiful">
    <label for="beautiful">Beautiful</label>
  </div>
  <div>
    <input type="checkbox" id="wonderful" name="wonderful">
    <label for="wonderful">Wonderful</label>
  </div>
  <div>
    <input type="checkbox" id="world" name="world">
    <label for="world">World</label>
  </div>

  <button onclick="updateOutput()">Update Output</button>

  <h2>Output:</h2>
  <div id="output"></div>

  <script>
    function updateOutput() {
      const hello = document.getElementById('hello').checked;
      const beautiful = document.getElementById('beautiful').checked;
      const wonderful = document.getElementById('wonderful').checked;
      const world = document.getElementById('world').checked;

      let output = '';

      if (hello) {
        output += 'Hello';
      }

      if (beautiful) {
        output += (output ? ' ' : '') + 'Beautiful';
      }

      if (wonderful) {
        output += (output ? ' ' : '') + 'Wonderful';
      }

      if (world) {
        output += (output ? ' ' : '') + 'World';
      }

      document.getElementById('output').innerText = output;
    }
  </script>
</body>
</html>
```

In this updated version, we've added checkboxes for each feature and a button to update the output message based on the selected checkboxes. The `updateOutput` function now checks the state of the checkboxes and updates the output message accordingly.

Please note that this version of the client-side code no longer communicates with the server-side code. The feature selections are handled entirely by the user via the checkboxes.


#### You:
please make a version that does communicate with the server side 

#### ChatGPT:
To create a version that communicates with the server-side, we'll update the server-side code to accept an array of selected features and return the output based on that. Then, we'll update the client-side code to send the selected features to the server.

Update the `server.js` file with the following code:

```javascript
const express = require('express');
const { initialize } = require('unleash-client');
const cors = require('cors');

const app = express();
const unleash = initialize({
  appName: 'my-app-name',
  instanceId: 'my-instance-id',
  url: 'https://unleash.example.com/api/',
});

app.use(cors());
app.use(express.json());

app.post('/features', (req, res) => {
  const selectedFeatures = req.body.features || [];

  let output = '';

  if (selectedFeatures.includes('hello') && unleash.isEnabled('hello')) {
    output += 'Hello';
  }

  if (selectedFeatures.includes('beautiful') && unleash.isEnabled('beautiful')) {
    output += (output ? ' ' : '') + 'Beautiful';
  }

  if (selectedFeatures.includes('wonderful') && unleash.isEnabled('wonderful')) {
    output += (output ? ' ' : '') + 'Wonderful';
  }

  if (selectedFeatures.includes('world') && unleash.isEnabled('world')) {
    output += (output ? ' ' : '') + 'World';
  }

  res.json({ output });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Update the `index.html` file with the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Feature Toggles Web App</title>
</head>
<body>
  <h1>Select Features:</h1>
  <div>
    <input type="checkbox" id="hello" name="hello">
    <label for="hello">Hello</label>
  </div>
  <div>
    <input type="checkbox" id="beautiful" name="beautiful">
    <label for="beautiful">Beautiful</label>
  </div>
  <div>
    <input type="checkbox" id="wonderful" name="wonderful">
    <label for="wonderful">Wonderful</label>
  </div>
  <div>
    <input type="checkbox" id="world" name="world">
    <label for="world">World</label>
  </div>

  <button onclick="updateOutput()">Update Output</button>

  <h2>Output:</h2>
  <div id="output"></div>

  <script>
    async function updateOutput() {
      const hello = document.getElementById('hello').checked;
      const beautiful = document.getElementById('beautiful').checked;
      const wonderful = document.getElementById('wonderful').checked;
      const world = document.getElementById('world').checked;

      const selectedFeatures = [];

      if (hello) {
        selectedFeatures.push('hello');
      }

      if (beautiful) {
        selectedFeatures.push('beautiful');
      }

      if (wonderful) {
        selectedFeatures.push('wonderful');
      }

      if (world) {
        selectedFeatures.push('world');
      }

      const response = await fetch('http://localhost:3000/features', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ features: selectedFeatures })
      });

```
