//弹出信息
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
//回到顶部
$(window).scroll(function(){
    $('#to-top').hide();
    if ($(window).scrollTop()>=600){
        $('#to-top').show();
    };
});
$("#to-top").click(function () {
        var speed=400;//滑动的速度
        $('body,html').animate({ scrollTop: 0 }, speed);
        return false;
 });
//导航栏鼠标滑过自动展开下拉菜单
$(document).ready(function(){
 var $dropdownLi = $('.navbar-fixed-top li.dropdown');
 $dropdownLi.mouseover(function() {
 $(this).addClass('open');
 }).mouseout(function() {
 $(this).removeClass('open');
 });
});
