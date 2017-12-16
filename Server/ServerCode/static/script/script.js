window.onload = function() {
    let inputFile = document.querySelectorAll("input[type='file']");
    let createDiv = document.createElement('div');
    createDiv.setAttribute('id', 'blackCover');
    
    for(let i in inputFile) {
        inputFile[i].onchange = function(e) {
            e.preventDefault();
            let appendImg = inputFile[i].previousSibling.previousSibling.previousSibling.previousSibling;//willChange

            let file = inputFile[i].files[0],
                reader = new FileReader();

            reader.onload = function (event){
                let img = new Image();
                img.src = event.target.result;

                appendImg.innerHTML = '';
                appendImg.appendChild(img);
                appendImg.appendChild(createDiv);
            };
            reader.readAsDataURL(file);
            return false;
        }
    }
};
function bllllllllllla(){
    document.getElementById("customp").innerHTML = "<img src=\"/static/images/vtrImg/picture (25).jpg\" style=\"width:100%; height: 100%;\">";
}