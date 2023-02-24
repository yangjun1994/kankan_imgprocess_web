const express=require('express');
const path=require('path');
const fs=require('fs');
const multer=require('multer');



const app = express();
let upload = multer({
    storage: multer.diskStorage({
        destination: function (req, file, cb) {
            let date = new Date();
            let year = date.getFullYear();
            let month = (date.getMonth() + 1).toString().padStart(2, '0');
            let day = date.getDate();
            let dir = "./files/" + year + month + day;

            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, {recursive: true});
            }

            cb(null, dir);
        },

        filename: function (req, file, cb) {
            let fileName = 'original-' + Date.now() + path.extname(file.originalname);

            cb(null, fileName);
        }
    })
});

app.use('/', express.static('static'));
app.use('/files', express.static('files'));



const child_process = require('child_process');
app.post('/upload_img',upload.single('kankan_img_file'),(req,res,next)=>{
    let file = req.file;
    if (!file) {
        res.send('您没选择文件╮(╯▽╰)╭');
    }
    else {

        console.log(file);

        infilepath = file.destination + '/' + file.filename;
        outfilepath = file.destination + '/' + file.filename.replace('original-', 'output-');
        console.log(infilepath);
        console.log(outfilepath);


        let workerProcess = child_process.exec('python pydemo.py ' + infilepath + ' ' + outfilepath, function (error, stdout, stderr) {
            if (error) {
                console.log(error.stack);
                console.log('Error code: ' + error.code);
                console.log('Signal received: ' + error.signal);
                res.send('算法程序出错了！');
            } else {
                console.log('stdout: ' + stdout);
                console.log('stderr: ' + stderr);
                res.send("点击<a href=" + infilepath + ">这里</a>下载您上传的文件。" + "<br />" + "点击<a href=" + outfilepath + ">这里</a>下载您上传的文件处理后的结果。" + "<br />" + "点击<a href=/>这里</a>返回。");

            }
        });
    }
})







app.listen(3000, () => {
    console.log('侃侃图片远程程序正在监听3000端口。');
});
