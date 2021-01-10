#The code that generates the HTML
def generateHTML(jsonString):
    htmlData = """

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Nebra Hotspot Diagnostics</title>
    <!-- Bootstrap core CSS -->
<link href="bootstrap.min.css" rel="stylesheet">
    <!-- Favicons -->
<meta name="theme-color" content="#7952b3">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

      body {
        padding-top: 5rem;
      }

    </style>

  </head>
  <body>

<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Nebra Helium Hotspot Diagnostics Page</a>
  </div>
</nav>

<main class="container">

  <div class="row">
    <div class="col">
      <h1 class="text-center">Diagnostics Information</h1>
      <h2 class="text-danger text-center"></h2>
    </div>
  </div>
<hr/>
  <div class="row">
    <div class="col">
      <h2 class="text-center">Diagnostics Breakdown</h2>
        <table class="table">
          <tbody>
            <tr>
              <td>ECC Detected</td>
              <td>{ecc}</td>
            </tr>
            <tr>
              <td>ETH0 MAC</td>
              <td>{E0}</td>
            </tr>
            <tr>
              <td>WLAN0 MAC</td>
              <td>{W0}</td>
            </tr>
            <tr>
              <td>RPi Serial</td>
              <td>{RPI}</td>
            </tr>
            <tr>
              <td>BT Detected</td>
              <td>{BT}</td>
            </tr>
            <tr>
            <td>LoRa OK?</td>
              <td>{LOR}</td>
            </tr>
          </tbody>
        </table>
    </div>
    <div class="col">
      <h2 class="text-center">Support QR</h2>
      <img src="diagnosticsQR.png" class="img-thumbnail">
    </div>
  </div>

</main><!-- /.container -->


  </body>
</html>
    """ % jsonString
    return htmlData
