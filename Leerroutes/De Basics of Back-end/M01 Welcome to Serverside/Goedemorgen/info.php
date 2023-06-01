<?php
    $time = date("G");
    $timemsg = date("g i s A");
    $bericht = "";
    $url = "";

    if ($time < "8"){
        $bericht = "Good night !";
        $url = "images/night.jpg";
    }
    elseif ($time < "12"){
        $bericht = "Good morning !";
        $url = "images/morning.jpg";
    }
    elseif ($time < "18"){
        $bericht = "Good afternoon !";
        $url = "images/afternoon.jpg";
    }
    elseif ($time < "23"){
        $bericht = "Good evening !";
        $url = "images/evening.jpg";
    }

    echo $bericht . "</br>" . "</br>";
    echo $timemsg;
?>

<style>
    body{
        background: url(<?php echo $url; ?>);
        background-position: center top;
        background-size: cover;
        text-align: center;
        margin-top: 300px;
        font-family: cursive;
        font-size: xx-large;
        color: white;
    }
</style>