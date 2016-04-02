
<!DOCTYPE html>
<html>
<head>

	<meta charset="UTF-8">  
	<title>Web Crawler</title>
	<link rel="stylesheet" href="bootstrap.css">
	<link rel="stylesheet" href="main1.css">
	<link rel="stylesheet" href="style.css">
</head>
<body class='bgcolor'>
	<div class="container">
		<div class="row">
		<div class="col-md-4 col-md-offset-4" style="padding-bottom:50px">
		
			<div class="img">		
					
			</div>
			<br><br>
			<div class="outer">
			<div class="panel panel-default">
				<br>
				<div class="name">
					IITG SEARCH
				</div>
				<div class="tag">
					Easing up your life!
				</div>
				<br>
				<form action="welcome.php" method="post">
				Search :<input id="automplete-5" type="text" name="search"><br>
				<input type="radio" name="exe" < value="con" >Contents<br>
				<input type="radio" name="exe" value="pdf">Pdf<br>
				<input type="radio" name="exe" value="img">Image<br>
				<input type="radio" name="exe" value="repo">Repo<br>

				<input type="submit">
				</form>
		    	<div class="progress" id="progressb" style="display:none; margin:20px auto">
		    	  <div class="progress-bar progress-bar-striped active" role="progressbar" id="progressBar" aria-valuenow="0"
		    	  aria-valuemin="0" aria-valuemax="100">
		    	    <span class="sr-only"></span>
		    	  </div>
		    	</div>
		    	<h3 id="status"></h3>
			    <div class="alert alert-info" role="alert" id="uploadAlert" style="display:none; color: #2baae1">
			    	<span class="msg color" style="font: 14px Roboto-Regular"></span>
			    </div>
			</div>
			</div>
		</div>
		</div>
	</div>

<?php 
$a= $_POST["search"]; 
$b=$_POST['exe'];
$data=array($a,$b);
// Execute the python script with the JSON data 
$result = shell_exec('python x.py ' . escapeshellarg(json_encode($data)) . ' 2>&1'); 
// Decode the result 
$resultData = json_decode($result, true); 
// This will contain: array('status' => 'Yes!' ---."<br />" ;

$length = count($resultData);
for($i=1;$i<$length;$i++)
echo "<a href='$resultData[$i]'>"."$resultData[$i]"."</a>"."<br />" ;

?> 


	<footer class="navbar-default navbar-fixed-bottom" id="footer">
		<div class = "container" id="developers">
			<b>Developed By:</b><br>
			Rajan garg<br>
			Abhinav singh<br>
			Abhinav prince<br>
			<br>
			<b>Design:</b><br>
			Rajan garg<br>
		
	</footer>

	<script type="text/javascript" src="jquery.js"> ></script>
	<script src="bootstrap-3.3.5-dist/js/bootstrap.min.js"></script>	
	 <script src="filestyle/src/bootstrap-filestyle.js"></script>	
	<script type="text/javascript" src="main.js" ></script>

</body>
</html>
