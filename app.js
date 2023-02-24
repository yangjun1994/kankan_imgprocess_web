const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('It works2333');
});

app.listen(3000, () => {
    console.log('侃侃图片远程程序正在监听3000端口。');
});
