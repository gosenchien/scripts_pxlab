<?php// phpinfo(); ?>

<?php
   $host        = "host=127.0.0.1";
   $port        = "port=5432";
   $dbname      = "dbname=analysis";
   $credentials = "user=balajan";

   $db = pg_connect( "$host $port $dbname $credentials"  );
   if(!$db){
	       echo "Error : Unable to open database";
   } else {
	       printf("Opened database successfully <br>");
   }
    $sql =<<<EOF
      SELECT number, proj, stage, dsn FROM device_data;
      EOF;
   $ret = pg_query($db, $sql);
      if(!$ret){
	          echo pg_last_error($db);
	          exit;
	       } 
      while($row = pg_fetch_row($ret)){
	      printf("Number=%3d <br> Project=%s, Stage=%s, DSN=%s <br><br>", $row[0], $row[1], $row[2], $row[3]);
//         printf("GeoName = ". $row[0] . "&nbsp;");
//         printf("Region = ". $row[1] ."&nbsp;");
//         printf("State = ". $row[2] ."&nbsp;");
//         printf("County =  ".$row[4] ."<br>");
      }
      echo "Operation done successfully";
      pg_close($db);
?>
