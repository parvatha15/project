<?php 

error_reporting(0);

$con=mysqli_connect ("localhost","root","","good") or die(mysqli_error());

 if((isset($_POST['submit'])))
{

  $Name=$con->real_escape_string($_POST['name']);
  $Gender=$con->real_escape_string($_POST['gender']);
  $Bloodgroup=$con->real_escape_string($_POST['bloodgroup']);
  $Dateofbirth=$con->real_escape_string($_POST['txtbirthdate']);
  $Age=$con->real_escape_string($_POST['txtage']);
  $Weight=$con->real_escape_string($_POST['weight']);
  $Address=$con->real_escape_string($_POST['address']);
  $Aadhaarno=$con->real_escape_string($_POST['aadhaarno']);
  $PhoneNo=$con->real_escape_string($_POST['phoneno']);
  $Emailid=$con->real_escape_string($_POST['emailid']);
  


    $sql="INSERT INTO student(name,gender,bloodgroup,txtbirthdate,txtage,weight,address,aadhaarno,phoneno,emailid) VALUES('".$Name."','".$Gender."','".
    $Bloodgroup."','".$Dateofbirth."','".$Age."','".$Weight."','".$Address."','".$Aadhaarno."',
    '".$PhoneNo."','".$Emailid."')";

    if(!$result = $con->query($sql)){
   
       die('Error occured ['.$con->error.']');
   }

   else

      echo "Thank you!submitted a ours feedback";

}

?>

   