/**
 * 使用:
 * 直接 node compare_file.js
 */
const fs = require('fs');
const spawn = require("child_process").spawn;

const filePath1 = 'C:/Users/Administrator/Desktop/githubc/NEWS/beta/new.txt';
const filePath2 = 'C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt';

const content1 = fs.readFileSync(filePath1, 'utf8');
const content2 = fs.readFileSync(filePath2, 'utf8');
if (content1 == content2) {
    console.log('Both file are same');
} else {
    python 6.py;
}
