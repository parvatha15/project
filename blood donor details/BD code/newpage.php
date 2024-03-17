<?php 

$con=mysqli_connect("localhost","root","","school") or die(mysqli_error());

 if((isset($_POST['submit'])))
{

  $Name=$con->real_escape_string($_POST['name']);
  $Fathername=$con->real_escape_string($_POST['fathername']);
  $Gender=$con->real_escape_string($_POST['gender']);
  $Occupation=$con->real_escape_string($_POST['occuption']);
  $Address=$con->real_escape_string($_POST['address']);
  $City=$con->real_escape_string($_POST['city']);
  $username=$con->real_escape_string($_POST['username']);
  $Password=$con->real_escape_string($_POST['password']);
  $LastDonateDate=$con->real_escape_string($_POST['lastday']);



    $sql="INSERT INTO bag(name,fathername,gender,occuption,address,city,username,password,lastday) VALUES('".$Name."','".$Fathername."','".$Gender."','".$Occupation."','".$Address."','".$City."',
      '".$username."','".$Password."','".$LastDonateDate."')";

   

    if(!$result = $con->query($sql)){
   
       die('Error occured ['.$con->error.']');
   }

   else

      echo "Thank you!submitted registration";

}

?>

   