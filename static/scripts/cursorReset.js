// 光标 URL 数组
var cursorUrls = [
    "/static/cursor/1.png",
    "/static/cursor/2.png",
    "/static/cursor/3.png",
    "/static/cursor/4.png",
    "/static/cursor/5.png",
    "/static/cursor/6.png",
    "/static/cursor/7.png",
    "/static/cursor/8.png",
    "/static/cursor/9.png"
];
var currentIndex = 0;

// 点击事件处理函数
function changeCursor() {
    // 获取下一个光标 URL
    var nextCursorUrl = cursorUrls[currentIndex];
    // 更新 CSS
    document.body.style.cursor = 'url(' + nextCursorUrl + '), auto';
    // 更新当前索引
    currentIndex = (currentIndex + 1) % cursorUrls.length;
}

// 为 body 添加点击事件监听器
document.body.addEventListener('click', changeCursor);