window.onload = function() {
    let loginSubmit = document.getElementById("loginSubmit");
    if(loginSubmit != null){
        submit.onclick = function () {
            var xhr = new XMLHttpRequest();
            
            username = document.getElementById("loginId").value;
            password = document.getElementById("loginPw").value;
            
            
            xhr.onreadystatechange = function() {
                if(this.readyState == 4){
                    if(this.status == 200){
                        alert("Success! " + this.responseText);
                    }else if(this.status == 400){
                        alert("Fail! " + this.responseText);
                    }else{
                        alert(this.status + this.responseText);
                    }
                }
            };
            params = "username=" + username + "&password=" + password;
            
            console.log(params);
            
            xhr.open("POST", "http://lapio.kr/api/login.php", true);
            
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            
            xhr.send(params);

            return false;
        }
    }

    let signupSubmit = document.getElementById("signupSubmit");
    if(signupSubmit != null){
        submit.onclick = function () {
            var xhr = new XMLHttpRequest();
            
            username = document.getElementById("signupId").value;
            password = document.getElementById("signupPw").value;
            nickname = document.getElementById("signupNickname").value;
            email = document.getElementById("signupEmail").value;

            xhr.onreadystatechange = function() {
                if(this.readyState == 4){
                    if(this.status == 200){
                        alert("Success! " + this.responseText);
                    }else if(this.status == 400){
                        alert("Fail! " + this.responseText);
                    }else{
                        alert(this.status + this.responseText);
                    }
                }
            };
            params = "username=" + username + "&password=" + password + "&nickname=" + nickname + "&email=" + email;
            
            console.log(params);
            
            xhr.open("POST", "http://lapio.kr/api/register.php", true);
            
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            
            xhr.send(params);

            return false;
        }
    }
};