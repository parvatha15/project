<?php

$host="localhost";
$username="root";
$password="";
$db="good";

$conn=new mysqli($host, $username, $password, $db);

if(isset($_POST['submit'])){

  $bloodgroup=$_POST['bloodgroup'];
  $sql=mysqli_query($conn,"select * from student where bloodgroup='$bloodgroup'");
 while($data=mysqli_fetch_array($sql)){

?>

<p>NAME:<?php echo $data['name'];?></p>
<p>GENDER:<?php echo $data['gender'];?></p>
<p>BLOODGROUP:<?php echo $data['bloodgroup'];?></p>
<p>PHONENO:<?php echo $data['phoneno'];?></p>
<p>EMAILID:<?php echo $data['emailid'];?></p>
<hr>

<?php } }?>