//弹出信息
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
//回到顶部
$(window).scroll(function(){
    $('#to-top').hide();
    if ($(window).scrollTop()>=500){
        $('#to-top').show();
    };
});
$("#to-top").click(function () {
        var speed=400;//滑动的速度
        $('body,html').animate({ scrollTop: 0 }, speed);
        return false;
 });
