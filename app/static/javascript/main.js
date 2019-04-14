function register(){
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'http://localhost:8000/register', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    

	var login = document.getElementById("login").value;
    var password = document.getElementById("password").value;
    var age = document.getElementById("age").value;

	var body = "login=" + login + "&password=" + password + "&age="+age;
	xhr.send(body); 
}

function log(){
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'http://localhost:8000/login', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    

	var login = document.getElementById("login").value;
    var password = document.getElementById("password").value;

	var body = "login=" + login + "&password=" + password;
	xhr.send(body); 

	xhr.onreadystatechange = function() { 
		var xhr2 = new XMLHttpRequest();
		xhr2.open('GET', 'http://localhost:8000/news', true);
		xhr2.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		xhr2.send(); 	
		xhr2.onreadystatechange = function() { 
			if (xhr.responseText == "Пользователь был найден")
				document.location.href="http://localhost:8000/news"
		}
	}
	  
}