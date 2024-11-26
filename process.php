<?php
if (isset($_GET['integers']) && isset($_GET['threshold'])) {
    $integers = $_GET['integers'];
    $threshold = $_GET['threshold'];

    // Call the Python script
    $command = escapeshellcmd("python3 bitwise_operations.py '$integers' $threshold");
    $output = shell_exec($command);

    echo "<pre>$output</pre>";
} else {
    echo "Error: Missing input values.";
}

