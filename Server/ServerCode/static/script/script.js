window.onload = function() {
    let inputFile = document.querySelectorAll("input[type='file']");
    let imgCheck = document.getElementsByClassName("imgCheck");
    for(let i in inputFile) {
        inputFile[i].onchange = function(e) {
            e.preventDefault();
            let appendImg = document.querySelector('article');//willChange

            let file = uploadImg.files[0],
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
    
    let uploadImg = document.getElementById('backPic');
            let createDiv = document.createElement('div');
            createDiv.setAttribute('id', 'blackCover');
            
            uploadImg.onchange = function (e) {
                e.preventDefault();
                let appendImg = document.querySelector('article');//willChange
                
                let file = uploadImg.files[0],
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
            };
};