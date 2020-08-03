<html>
<body>
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>"> Name: <input type="text" name="fname">
<input type="submit">
</form>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	// collect value of input field
	$name = htmlspecialchars($_REQUEST['fname']);
	if (empty($name)) { echo "Name is empty "; } else { echo "<h4>$name </h4>"; }
}
?>

<?php
print "Setup 6 number<br/>";
$first = rand(1,18);
$secnd = rand(19,30);
//third = rand(20,30);
//if ( $third == $secnd ) {$third = rand(20,30);}
$forth = rand(30,50);
//$fifth = rand(30,40);
//if ( $fifth == $forth ) {$fifth = rand(30,40);}

//$sixth = rand(40,50);
print "The first solution is:" .$first. "," .$secnd. "," .$forth. "... <br/>";
echo "Finish guessing.....<br/>";
?>

<?php 
printf("<h3>Another test~</h3>") ;
print $_SERVER['PHP_SELF'];
echo "<br>";
print $_SERVER['SERVER_NAME'];
echo "<br>";
print $_SERVER['SERVER_ADMIN'];
echo "<br>";
print $_SERVER['HTTP_HOST'];
echo "<br>";
print $_SERVER['HTTP_REFERER'];
echo "<br>";
print $_SERVER['HTTP_USER_AGENT'];
echo "<br>";
print $_SERVER['SCRIPT_NAME'];
?>
</body>
</html>
