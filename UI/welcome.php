
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
		    	<div class="form-group">
				
					<input type="text" name="search"><br>
					
				
		    	</div>
		    		    	
		    	<div id="submit">
		    	<button type="button" class="btn btn-primary" name="submit" id="submitButton">
				
		    		<span style="font: bold 17px Roboto"><input type="submit"></span>
		    	</button>
		    	</div>
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
echo $_POST['search'];
$data= $_POST['search'];    
// Execute the python script with the JSON data
$result = shell_exec('python x.py' . escapeshellarg(json_encode($data)));

// Decode the result
$resultData = json_decode($result, true);
// This will contain: array('status' => 'Yes!'
for($i=1;$i<=2;$i++)
echo $resultData[$i]."<br />" ;

?>



	<script type="text/javascript" src="jquery.js"> ></script>
	<script src="bootstrap-3.3.5-dist/js/bootstrap.min.js"></script>	
	 <script src="filestyle/src/bootstrap-filestyle.js"></script>	
	<script type="text/javascript" src="main.js" ></script>

</body>
</html>
