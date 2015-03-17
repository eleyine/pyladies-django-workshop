
(function(angular, Reveal) {

    var fragmentShownHiddenEvents = function fragmentShownHiddenEvents() {
        angular.element('body').scope().$digest();
    }

    Reveal.addEventListener( 'fragmentshown', function( event ) {
    // event.fragment = the fragment DOM element
        console.log('Fragment shown!')
        // fragmentShownHiddenEvents();
        angular.element('body').scope().$digest();
    });

    Reveal.addEventListener( 'fragmenthidden', function( event ) {
    // event.fragment = the fragment DOM element
        console.log('Fragment hidden!')
        fragmentShownHiddenEvents();
    });
})(window.angular, Reveal);