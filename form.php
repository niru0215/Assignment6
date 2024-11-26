<!DOCTYPE html>
<html>
<head>
    <title>Integer Input Form</title>
</head>
<body>
    <form action="process.php" method="get">
        <label for="integers">Enter integers (comma-separated):</label>
        <input type="text" id="integers" name="integers" required>
        <br>
        <label for="threshold">Threshold:</label>
        <input type="number" id="threshold" name="threshold" required>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
