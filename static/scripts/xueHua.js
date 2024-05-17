(function($){
    $.fn.snow = function(options){
        var $flake = $('<div id="snowbox" />').css({'position': 'absolute','z-index':'50', 'top': '-50px', 'user-select': 'none'}).html('❄'),
            documentHeight  = $(document).height(),
            documentWidth   = $(document).width(),
            defaults = {
                minSize     : 10,
                maxSize     : 20,
                newOn       : 1000,
                flakeColor  : "#e0c0ce" /* 此处可以定义雪花颜色，若要白色可以改为#FFFFFF */
            },
            options = $.extend({}, defaults, options);
        var interval= setInterval( function(){
            var startPositionLeft = Math.random() * documentWidth - 100,
                startOpacity = 0.5 + Math.random(),
                sizeFlake = options.minSize + Math.random() * options.maxSize,
                endPositionTop = documentHeight - 200,
                endPositionLeft = startPositionLeft - 500 + Math.random() * 500,
                durationFall = documentHeight * 10 + Math.random() * 5000;
            $flake.clone().appendTo('body').css({
                left: startPositionLeft,
                opacity: startOpacity,
                'font-size': sizeFlake,
                color: options.flakeColor
            }).animate({
                top: endPositionTop,
                left: endPositionLeft,
                opacity: 0.2
            },durationFall,'linear',function(){
                $(this).remove()
            });
        }, options.newOn);
    };
})(jQuery);
$(function(){
    $.fn.snow({
        minSize: 5, /* 定义雪花最小尺寸 */
        maxSize: 80,/* 定义雪花最大尺寸 */
        newOn: 200  /* 定义密集程度，数字越小越密集 */
    });
});
/* 鼠标特效 */
var a_idx = 0;
jQuery(document).ready(function($) {
    $("body").click(function(e) {
        var a = new Array("欲买桂花同载酒","轻盈的风","浮世景色百千年依旧","愿你今晚得享安睡","请随我一同避雨吧","嗯？天晴了吗？","烟花易逝","拾花鸟之一趣","照月风之长路","雪霁银装素","桔高映琼枝","深山踏红叶","耳畔闻鹿鸣","白露与清梦","胧幻与此生","若比君侧时","皆算久长事");
        var $i = $("<span></span>").text(a[a_idx]);
        a_idx = (a_idx + 1) % a.length;
        var x = e.pageX,
            y = e.pageY;
        $i.css({
            "z-index": 30,
            "top": y - 20,
            "left": x,
            "position": "absolute",
            "font-weight": "bold",
            "user-select": "none",
            "color": "rgb("+~~(255*Math.random())+","+~~(255*Math.random())+","+~~(255*Math.random())+")"
        });
        $("body").append($i);
        $i.animate({
                "top": y - 180,
                "opacity": 0
            },
            3000,
            function() {
                $i.remove();
            });
    });
});