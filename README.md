# StyleSense-Generative--AI-Powered-Fashion-Recommendation-System
<!DOCTYPE html>
<html>
<head>
<title>StyleSense AI</title>
</head>

<body>

<h1>StyleSense AI Fashion Recommendation</h1>

<label>Style:</label>
<input type="text" id="style"><br><br>

<label>Occasion:</label>
<input type="text" id="occasion"><br><br>

<label>Color:</label>
<input type="text" id="color"><br><br>

<button onclick="recommend()">Get Outfit</button>

<p id="result"></p>

<script>

function recommend(){

let tops = ["White Shirt","Black T-Shirt","Denim Jacket"];
let bottoms = ["Blue Jeans","Black Jeans","Grey Trousers"];
let shoes = ["Sneakers","Boots","Loafers"];

let top = tops[Math.floor(Math.random()*tops.length)];
let bottom = bottoms[Math.floor(Math.random()*bottoms.length)];
let shoe = shoes[Math.floor(Math.random()*shoes.length)];

document.getElementById("result").innerHTML =
"Recommended Outfit: " + top + " + " + bottom + " + " + shoe;

}

</script>

</body>
</html>
