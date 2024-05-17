$(function() {
    //scroll 事件适用于所有可滚动的元素和 window 对象（浏览器窗口）。
    $('.content').scroll(function() {
        var scroHei = $('.content').scrollTop();//滚动的高度
        if (scroHei > 500) {
            $('.back-to-top').css('top','-20%');//上吊猫离页面底部的距离

        } else {
            $('.back-to-top').css('top','-100%');
        }
    })
    /*点击返回顶部*/
    $('.back-to-top').click(function() {
        $('.content').animate({
            scrollTop: 0
        }, 600);
    })
})