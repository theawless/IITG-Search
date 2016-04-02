
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
				Search :<input type="text" name="search"><br>

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
$data= $_POST["search"]; 
// Execute the python script with the JSON data 
$result = shell_exec('python x.py ' . escapeshellarg(json_encode($data)) . ' 2>&1'); 
// Decode the result 
$resultData = json_decode($result, true); 
// This will contain: array('status' => 'Yes!' ---."<br />" ;

$length = count($resultData);
//for($i=1;$i<=$length;$i++)

 //   echo "<a href='$resultData[$i]'>"."$resultData[$i]"."</a>"."<br />" ;

?> 


<?php

$start=0;
$limit=8;

if(isset($_GET['id']))
{
	$id=$_GET['id'];
	$start=($id-1)*$limit;
}
else{
	$id=1;
}

?>
<ul>
<?php
//print 10 items
for($i=$start;$i<$start+$limit;$i++) 
echo "<a href='$resultData[$i]'>"."$resultData[$i]"."</a>"."<br />" ; 
?>
</ul>
<?php
$rows=$length;
$total=ceil($rows/$limit);?>

<?php if($id>1)
{
	//Go to previous page to show previous 10 items. If its in page 1 then it is inactive
	echo "<li><a href='?id=".($id-1)."' class='button'>PREVIOUS</a></li>";
}
if($id!=$total)
{
	////Go to previous page to show next 10 items.
	echo "<li><a href='?id=".($id+1)."' class='button'>NEXT</a></li>";
}
?>

<?php
//show all the page link with page number. When click on these numbers go to particular page. 
		for($i=1;$i<=$total;$i++)
		{
			if($i==$id) { echo "<li class='current'>".$i."</li>"; }
			
			else { echo "<li><a href='?id=".$i."'>".$i."</a></li>"; }
		}
?>
	<footer class="navbar-default navbar-fixed-bottom" id="footer">
		<div class = "container" id="developers">
			<b>Developed By:</b>
			<span><span class="color">R</span>ajan garg, <span class="color">A</span>bhinav prince, <span class="color">A</span>bhinav singh</span>
			<br>
			<b>Design:</b>
			<span>Raja<span class="color">n</span> Garg</span>
		</div>
		<div class = "container" id="contact">
			<span id='contactUs'><a href="http://goo.gl/forms/F2m0sWZbX2">Contact Us</a></span>
		</div>
	</footer>

	<script type="text/javascript" src="jquery.js"> ></script>
	<script src="bootstrap-3.3.5-dist/js/bootstrap.min.js"></script>	
	 <script src="filestyle/src/bootstrap-filestyle.js"></script>	
	<script type="text/javascript" src="main.js" ></script>

</body>
</html>
