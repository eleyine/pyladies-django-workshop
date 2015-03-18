
(function(Reveal) {

    $('.github').each(function () {
        var pre = $(this).attr("data-github-pre");
        var post = $(this).attr("data-github-post");
        var preHtml = "";
        if (pre) {
            preHtml = '<div class="pre"> git reset --hard <span class="tag">' + pre + '</span></div>';
        } else if (!!post) {
            preHtml = '<div style="font-size: 0.7em;"  class="pre">(pssst: git reset --hard <span class="tag">' + post + '</span>)</div>';
        }
        var postHtml = '';
        if (post)
            postHtml = '<div class="post"> git diff <span class="tag">' + post + '</span></div>' 
        $(this).html(preHtml + postHtml);
    });

    var fragmentShownHiddenEvents = function fragmentShownHiddenEvents() {
        // angular.element('body').scope().$digest();
    }

    Reveal.addEventListener( 'fragmentshown', function( event ) {
    // event.fragment = the fragment DOM element
        console.log('Fragment shown!')
        // fragmentShownHiddenEvents();
        // angular.element('body').scope().$digest();
    });

    Reveal.addEventListener( 'fragmenthidden', function( event ) {
    // event.fragment = the fragment DOM element
        console.log('Fragment hidden!')
        fragmentShownHiddenEvents();
    });

    // if (Reveal.isReady()) {
    //         init({ currentSlide: Reveal.getCurrentSlide() });
    //         return;
    //     }

    // Reveal.addEventListener('ready', function(e) {
    //     window.RevealCodeFocus = RevealCodeFocus(Reveal, hljs);
    //     RevealCodeFocus.init(e);
    //     console.log('try agadin');
    // });

    // the code below can be added to the end of your Reveal slide deck to implement
    // per slide theme setting via the data-theme attribute
    // I put this in right below the call to Reveal.initialize()
     
    // the code is smart enough to restore the previous default theme 
    // (or slide specific theme) as you move forward and backward
    // it also takes into account vertical slide stacks with a data-theme
    // attribute on the outer <section> tag and allows individual vertical
    // slides to specify their own override
     
    // this code is released into the public domain
    // written by James Brown  http://www.bldesign.com
     
    // implement slide specific theme loading via data-theme
    Reveal.addEventListener('slidechanged', function SlideChangedHandler (event) {
        // console.log('slide change: '); console.log(event);
        // event.previousSlide, event.currentSlide, event.indexh, event.indexv
     
        // first time called, remember what the default theme is
        if (!SlideChangedHandler.defaultTheme)
            SlideChangedHandler.defaultTheme = Reveal.getConfig().theme;
     
        // is this slide part of a verticle stack?  check for parent theme override & apply to this slide
        if (!event.currentSlide.dataset.theme && event.currentSlide.parentNode.nodeName == 'SECTION' && event.currentSlide.parentNode.dataset.theme)
            event.currentSlide.dataset.theme = event.currentSlide.parentNode.dataset.theme;
        
        // if this slide has a data-theme attribute, set it as the theme
        if (event.currentSlide.dataset.theme)
            Reveal.configure({ theme: event.currentSlide.dataset.theme });
        // if the previous slide had a custom theme and this slide does not (hence the else), reset the theme
        else if (event.previousSlide && event.previousSlide.dataset.theme)
            Reveal.configure({ theme: SlideChangedHandler.defaultTheme});
     
    } );

})(Reveal);