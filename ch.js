/**
 * 腳本需要用到jsdom執行腳本前先安裝
 * 在腳本所在位置開命令工具執行下面命令安裝
 * npm i jsdom
 * 
 * 之後執行腳本
 * node html_to_text.js
 */
const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

// 要讀取的html檔案名稱
const fileName = 'agaim.txt';
// 輸出的資料夾名稱
const exportDirName = '更新公告';


const html = fs.readFileSync(fileName, 'utf8');
const document = new JSDOM(html).window.document;
const targetQuery = '#mainScroll>.scroller>.contents-main>.weighty-list>[id^="important-text-"]';
const nodes = document.body.querySelectorAll(targetQuery);

if (!fs.existsSync(exportDirName)) {
    fs.mkdirSync(exportDirName);
}

nodes.forEach(n => {
    const saveName = n.id + '.txt';
    const text = n.children[0].textContent;
    fs.writeFileSync(`./${exportDirName}/${saveName}`, text);
})