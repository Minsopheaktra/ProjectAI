(function($){
  $(function(){

    // $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $("[data-activates=nav-mobile]").sideNav({
      edge: 'left',
      menuWidth: 220
    });
    $("[data-activates=slide-out1]").sideNav({
      edge: 'right',
      menuWidth: 300
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space
// Initialize collapse button
// $(".button-collapse").sideNav();
// // Initialize collapsible (uncomment the line below if you use the dropdown variation)
// //$('.collapsible').collapsible();
// $('.button-collapse').sideNav({
//       menuWidth: 220, // Default is 300
//       edge: 'left', // Choose the horizontal origin
//       closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
//       draggable: true // Choose whether you can drag to open on touch screens
//     }
//   );
// $(function() {
//   $("[data-activates=slide-out]").sideNav();
//   $("[data-activates=slide-out1]").sideNav({
//     edge: 'right'
//   });
// });
// Show sideNav
// $('.button-collapse').sideNav('show');
// // Hide sideNav
// $('.button-collapse').sideNav('hide');
// // Destroy sideNav
// $('.button-collapse').sideNav('destroy');
$('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrainWidth: false, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: -15, // Spacing from edge
      belowOrigin: true, // Displays dropdown below the button
      alignment: 'right', // Displays dropdown with edge aligned to the left of button
      stopPropagation: false // Stops event propagation
    }
  );
  $(document).ready(function(){
    $('.collapsible').collapsible();
  });
//   $('.collapsible').collapsible({
//   accordion: false, // A setting that changes the collapsible behavior to expandable instead of the default accordion style
//   onOpen: function(el) { alert('Open'); }, // Callback for Collapsible open
//   onClose: function(el) { alert('Closed'); } // Callback for Collapsible close
// });
// Open
// $('.collapsible').collapsible('open', 0);
//
// // Close
// $('.collapsible').collapsible('close', 0);
//
// // Destroy
// $('.collapsible').collapsible('destroy');
