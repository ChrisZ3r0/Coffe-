// app.js
const express = require('express');
const app = express();
const port = 3000;
const ip = '172.20.10.8'

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(port, ip, () => {
  console.log(`Server is running on port ${port}`);
});

