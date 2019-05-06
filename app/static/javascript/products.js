
buttons = document.getElementsByClassName("productButton")
for (let button of buttons){
	button.addEventListener("click", (e) => {
		let id = e.srcElement.getAttribute('productId');
		window.location = `http://localhost:8000/product/${id}`
	})
}




