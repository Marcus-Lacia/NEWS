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
const fileName = '/root/github/NEWS/agaim.txt';
// 輸出的資料夾名稱
const exportDirName = 'beta';


const html = fs.readFileSync(fileName, 'utf8');
const document = new JSDOM(html).window.document;
const targetQuery = '#mainScroll>.scroller>.contents-main>.weighty-list>[id^="important-text-"]';
const nodes = document.body.querySelectorAll(targetQuery);

if (!fs.existsSync(exportDirName)) {
    fs.mkdirSync(exportDirName);
}

function nodeToFile(n) {
    const saveName = n.id + '.txt';
    let text = n.children[0].textContent + '';
    let texts = text.split('\n').map(t => t.trim()).filter(t => t);
    text = texts.join('\n');
    fs.writeFileSync(`./${exportDirName}/${saveName}`, text);
}

const handleNodes = [];

// 只取最後的節點
// {
//     let lastIndex = nodes.length - 1;
//     if (lastIndex < 0) { lastIndex = 0; }
//     const lastNode = nodes.item(lastIndex);
//     handleNodes.push(lastNode);
// }

// 只取第一個節點
{
    const firstNode = nodes.item(0);
    handleNodes.push(firstNode);
}

// 加入處理所有節點
// {
//     handleNodes.push(...nodes);
// }

handleNodes.forEach(n => {
    nodeToFile(n);
});