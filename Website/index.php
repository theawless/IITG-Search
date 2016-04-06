<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Web Crawler</title>
    <link rel="stylesheet" href="bootstrap.css">
    <link rel="stylesheet" href="main1.css">


    <script src="jquery-ui-1.11.4/jquery-ui.css"></script>
    <script src="jquery-2.2.2.min.js"></script>
    <script src="jquery-ui-1.11.4/jquery-ui.js"></script>
    <link href="http://www.jqueryscript.net/css/jquerysctipttop.css" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <script>
        $.get("autocomplete.txt").done(function (data) {

            $("#autocomplete").autocomplete({source: data.split('\n'), minLength: 3,});
        });
    </script>

    <style type="text/css">

        .paging-nav {
            text-align: right;
            padding-top: 2px;
        }

        .paging-nav a {
            margin: auto 1px;
            text-decoration: none;
            display: inline-block;
            padding: 1px 7px;
            background: #91b9e6;
            color: white;
            border-radius: 3px;
        }

        .paging-nav .selected-page {
            background: #187ed5;
            font-weight: bold;
        }

        .paging-nav,
        #tableData {
            width: 900px;
            margin: 0 auto;
            font-family: Arial, sans-serif;
        }
    </style>

</head>
<body style="background-color:slategrey">
<div class="container ">
    <div class="row">
        <div class="col-md-4 col-md-offset-4" style="padding-bottom:10px">

            <div class="outer">
                <div class="panel panel-danger" style="width:400px">

                    <div class="name">
                        IITG SEARCH
                    </div>

                    <div class="tag">
                        Easing up your life!
                    </div>
                    <form action="index.php" method="post" id="labnol">

                        Search :
                        <input id="autocomplete" type="text" name="search"><br><br>
                        Contents :
                        <input type="radio" name="exe" value="site_content">Site
                        <input type="radio" name="exe" value="doc_content">Documents<br>

                        Filenames:
                        <input type="radio" name="exe" value="doc_url">Documents
                        <input type="radio" name="exe" value="repo_url">Repository
                        <input type="radio" name="exe" value="image_url">Image<br>
                        <input type="submit">
                        <img onclick="startDictation()" src="//i.imgur.com/cHidSVu.gif"/>


                    </form>

                </div>
            </div>
        </div>
    </div>
</div>
<table id="tableData" class="table table-bordered" style="background-color: whitesmoke;font-size: larger">
    <thead>
    <tr>
        <th>INDEX</th>
        <th>URL</th>
    </tr>
    </thead>
    <tbody>
    <?php

    $a = $_POST["search"];
    $b = $_POST['exe'];
    $a = str_replace(' ', '*', $a);
    $result = exec('python get_results.py ' . $a . ' ' . $b);
    $resultData = json_decode($result, true);
    $length = count($resultData);
    for ($i = 1; $i < $length; $i++) {
        echo "<tr>";
        echo "<td>";
        if ($b == "image_url") {
            echo "<a href=" . "\"" . $resultData[$i] . "\"" . " ><img width='70px' height='50px' src=" . "\"" . $resultData[$i] . "\"" . "/></a>";
        } else {
            echo $i;
        }
        echo "</td>";
        echo "<td>";
        echo "<a href='$resultData[$i]'>" . "$resultData[$i]" . "</a>" . "<br/>";
        echo "</td>";
        echo "</tr>";
    }
    ?>
    </tbody>
</table>

<footer style="background-color:whitesmoke;font-size: larger">

    <?php
    if ($resultData['suggestion'] != "") {
        echo "<br><p align='center'>Did you mean " . $resultData['suggestion'] . "?</p>";
    }
    echo "<p align='center'>Time taken to do this query: " . $resultData ['time'] . " seconds</p>";
    ?>
</footer>
<script type="text/javascript" src="paging.js"></script>
<script type="text/javascript">
    $(document).ready(function () {
        $('#tableData').paging({limit: 7});
    });
</script>


<script type="text/javascript">

    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-36251023-1']);
    _gaq.push(['_setDomainName', 'jqueryscript.net']);
    _gaq.push(['_trackPageview']);

    (function () {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
    })();

</script>

<script>
    function startDictation() {

        if (window.hasOwnProperty('webkitSpeechRecognition')) {

            var recognition = new webkitSpeechRecognition();

            recognition.continuous = false;
            recognition.interimResults = false;

            recognition.lang = "en-US";
            recognition.start();

            recognition.onresult = function (e) {
                document.getElementById('autocomplete').value
                    = e.results[0][0].transcript;
                recognition.stop();
                document.getElementById('labnol').submit();
            };

            recognition.onerror = function (e) {
                recognition.stop();
            }

        }
    }
</script>

</body>
</html>
