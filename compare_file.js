/**
 * 使用:
 * 直接 node compare_file.js
 */
const fs = require('fs');
const { spawn } = require('child_process');

// 檔案路徑
const filePath1 = '/root/github/NEWS/beta/new.txt';
const filePath2 = '/root/github/NEWS/new/new.txt';

const content1 = fs.readFileSync(filePath1, 'utf8');
const content2 = fs.readFileSync(filePath2, 'utf8');
if (content1 == content2) {
    console.log('Both file are same');
} else {
    const python = spawn('python', ["6.py"]);
}
