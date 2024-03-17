<?php 

$con=mysqli_connect ("localhost","root","","feed") or die(mysqli_error());

 if((isset($_POST['submit'])))
{

  $Candidatename=$con->real_escape_string($_POST['candidatename']);
  $Mobileno=$con->real_escape_string($_POST['mobileno']);
  $Emailid=$con->real_escape_string($_POST['emailid']);
  $Feedback=$con->real_escape_string($_POST['feedback']);




    $sql="INSERT INTO back (candidatename, mobileno, emailid, feedback) VALUES('".$Candidatename."','".$Mobileno."','".
    $Emailid."','".$Feedback."')";

    if(!$result = $con->query($sql)){
   
       die('Error occured ['.$con->error.']');
   }

   else

      echo "Thank you!submitted a ours feedback";

}

?>
