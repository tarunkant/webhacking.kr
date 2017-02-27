<?php
for($i=1500000;$i<2000000;$i++){                     #you can take any range of large values of i.
  $key = md5((string)$i,true);
  if(strpos($key,"'='")) echo $i;
  }
  
?>
