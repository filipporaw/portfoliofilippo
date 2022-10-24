var image = document.querySelector(".swap-image");
var currentPos = 0;
var images = ["./Images/Image-swaper/1-image.jpg", "./Images/Image-swaper/2-image.jpg", "./Images/Image-swaper/3-image.jpg", "./Images/Image-swaper/4-image.jpg"];

function volgendefoto() {
if (++currentPos >= images.length)
    currentPos = 0;

    image.src = images[currentPos];
}

setInterval(volgendefoto, 1250);