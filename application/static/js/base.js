$(document).ready(function() {
    $('#dash-nav').click(function(){
      console.log("clicked");
        $('.active').removeClass('active');
        $('#dash-nav').addClass('active');
    });

    $('.sidenav').sidenav();

});
