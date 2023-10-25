php
<?php
    if(isset($_POST['submit'])){
        $text = $_POST['text'];
        file_put_contents('adatok.txt', $text);
        echo "Text saved to text.txt";
    }
?>