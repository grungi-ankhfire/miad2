 function myFunction() {
  var scrolling = window.scrollY;                 // GET NUMBER OF PIXELS THAT DOCUMENT HAS BEEN SCROLLED VERTICALLY
  var header = document.getElementById("animated-header"); // GET THE ELEMENT WITH ID="header" FROM HTML
  if(scrolling >= 90) {                           // IF PAGE SCROLLED MORE THAN 90px
    header.classList.add('header-collapsed');                 // MAKE HEADER'S HEIGHT 60px
  } else {                                        // IF PAGE SCROLLED LESS THAN 90px
    header.classList.remove('header-collapsed'); // HEADER'S HEIGHT = STARTING HEIGHT(150px) - NUMBER OF PIXELS THAT PAGE HAS BEEN SCROLLED
  };
};
window.onscroll = function() { myFunction(); };   // ACTIVATE FUNCTION ON SCROLL