<!DOCTYPE html>
<head>
    <html lang="nl">
    <title>Keuzes</title>
    <link rel="stylesheet" href="needed/style.css">
    <?php include 'needed/footer.php'?>
<<<<<<< HEAD
    <?php include 'needed/buttons.php'?>
    <?php include 'library/checksonkunde.php'?>
</head>
=======
    <?php include 'library/checksonkunde.php'?>
</head>

    <div class = "items">
            <a href="paniek.php">Er heerst Paniek</a> |
            <a href="index.php">Index</a>
    </div>
>>>>>>> 03c70c075dc97ed285a59b6551469dd70dce0d3d
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
            Wat zou je graag willen kunnen? <input type="text" name="kunnen" value = "<?php echo $kunnen;?>">
            <span class="error">* <?php echo $kunnenErr;?></span> <br><br>

            Met welk persoon kun je goed opschieten? <input type="text" name="opschieten" value = "<?php echo $opschieten;?>">
            <span class="error">* <?php echo $opschietenErr;?></span> <br><br>

            Wat is je favoriete getal? <input type="text" name="getal" value = "<?php echo $getal;?>">
            <span class="error">* <?php echo $getalErr;?></span> <br><br>

            Wat heb je altijd bij je als je op vakantie bent? <input type="text" name="vakantie" value = "<?php echo $vakantie;?>">
            <span class="error">* <?php echo $vakantieErr;?></span> <br><br>

            Wat is je beste persoonlijke eigenschap? <input type="text" name="goed" value = "<?php echo $goed;?>">
            <span class="error">* <?php echo $goedErr;?></span> <br><br>

            Wat is je slechtse persoonlijke eigenschap? <input type="text" name="slecht" value = "<?php echo $slecht;?>">
            <span class="error">* <?php echo $slechtErr;?></span> <br><br>

            Wat is het ergste dat je kan overkomen? <input type="text" name="overkomen" value = "<?php echo $overkomen;?>">
            <span class="error">* <?php echo $overkomenErr;?></span> <br><br>

            <input type="submit">  
    </form>
    <?php
<<<<<<< HEAD
        if ($everything1 != ""){
=======
        if ($everything != ""){
>>>>>>> 03c70c075dc97ed285a59b6551469dd70dce0d3d
            echo "<br>";
            echo "Er zijn veel mensen die niet kunnen " , $kunnen, ". <br>"; 
            echo "Neem nou ", $opschieten, " zelfs met de hulp van een ", $vakantie, " of zelfs ", $getal, " kan hij niet ", $kunnen,". <br>";
            echo "Dat heeft niet te maken met gebrek van ", $goed, ". ";
            echo "Maar met een te veel aan ", $slecht,". <br>";
            echo "Te veel ", $slecht, " leid tot ", $overkomen, " en dat is niet goed als je wilt ", $kunnen,". <br>";
            echo "Helaas voor ", $opschieten,".";
        }
    ?>
</html>