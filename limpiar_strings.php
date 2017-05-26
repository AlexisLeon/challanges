<?php 
$str = "áéíóúÁÉÍÓÚ|@#¢∞¬÷“”≠¸‚][}{–≤…„!·$%&/()=?¿*^Ç¨_:;'¡`+´ç.-,'";
$string = htmlentities($str);
$string = preg_replace('/\&(.)[^;]*;/', '\\1', $string);
echo $string;
?>