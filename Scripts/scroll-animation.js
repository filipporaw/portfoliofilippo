var works = [document.querySelector(".work1"), document.querySelector(".work2"), document.querySelector(".work3"), document.querySelector(".work4"), document.querySelector(".work5"), document.querySelector(".work6")];
var worksContent = document.querySelector(".works-content");

var title = document.querySelector(".services-title");


window.addEventListener('scroll', function () {
    let scroll = window.pageYOffset;
    if(scroll > 800 && scroll < 7000){
        worksContent.style.marginTop = "0";
        scaleWork(works[0], scroll, 100, 90);
        scaleWork(works[1], scroll, 110, 85);
        scaleWork(works[2], scroll, 120, 80);
        scaleWork(works[3], scroll, 130, 75);
        scaleWork(works[4], scroll, 140, 70);
        scaleWork(works[5], scroll, 150, 65);
    }
    
    $(window).width() > 1400 ? ( scroll > 6000 && scroll < 9500 ? ( title.style.marginRight = `${scroll}px` ) : ( title.style.marginRight = `0` ) ) : ( title.style.marginRight = `0` );
});

function scaleWork(work, scroll, firstScale, secondScale) {
    work.style.transform = (`scale(${(100 - scroll / firstScale) / secondScale})`);
}