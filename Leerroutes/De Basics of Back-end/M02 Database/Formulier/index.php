<!DOCTYPE html>
    <head>
        <html lang="nl">
        <title>Welcome</title>
        <link rel="stylesheet" href="library/style.css">
        <?php include 'library/checks.php'; ?>
    </head>

    <body>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
            Name: <input type="text" name="name" value = "<?php echo $name;?>">
            <span class="error">* <?php echo $nameErr;?></span> <br><br>
            E-mail: <input type="text" name="email" value = "<?php echo $email;?>">
            <span class="error">* <?php echo $emailErr;?></span> <br><br>

            <input type="submit">  
        </form>

        <?php
        if ($name && $email != "") {
            echo "<h2>Your Input:</h2>";
            echo "Name: ", $name;
            echo "<br>";
            echo "Email: ", $email;
            echo "<br>";
        }
        ?>
    </body>
</html>