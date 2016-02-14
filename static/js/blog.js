// static/js/blog.js

console.log('initializing material js');
$.material.init();
$(document).ready(function(){
  // cache the window object
  $window = $(window);

  $('section[data-type="background"]').each(function(){
    // declare the variable to affect the defuned data-type
    var $scroll = $(this);

    $(window).scroll(function(){
      var yPos = -($window.scrollTop() / $scroll.data('speed'));
      var coords = '50% '+ yPos + 'px';
      $scroll.css({ backgroundPosition: coords });
    });
  });

});
