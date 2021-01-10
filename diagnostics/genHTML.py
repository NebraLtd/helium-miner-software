#The code that generates the HTML
def generateHTML(dictString):
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
      .bg-dark {
        background-color:#03a9f4!important;
      }
      .img-thumbnail {
        max-width:300px;
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
      <h2 class="text-center">Name: %(BN)s</h2>
""" % dictString
    if(dictString["ecc"] == True and dictString["E0"] != "FF:FF:FF:FF:FF:FF" and dictString["W0"] != "FF:FF:FF:FF:FF:FF" and dictString["BT"] == True and  dictString["LOR"] == True):
        htmlData = htmlData + """<h2 class="text-success text-center">All Ok</h2>"""
    else:
        htmlData = htmlData + """<h2 class="text-danger text-center">Errors Found</h2>"""
    htmlData = htmlData + """
    </div>
  </div>
<hr/>
  <div class="row">
    <div class="col">
      <h2 class="text-center">Diagnostics Breakdown</h2>
        <table class="table">
          <tbody>
            <tr class="bg-info">
              <th>Frequency</th>
              <td>%(BA)s</td>
            </tr>
            <tr """ % dictString
    if(dictString["ecc"] == True):
        htmlData = htmlData + """class='bg-success text-white'"""
    else:
        htmlData = htmlData + """class='bg-danger text-white'"""
    htmlData = htmlData + """ >
              <th>ECC Detected</th>
              <td>%(ecc)s</td>
            </tr>
            <tr """ % dictString
    if(dictString["E0"] == "FF:FF:FF:FF:FF:FF"):
        htmlData = htmlData + """class='bg-warning text-dark'"""
    else:
        htmlData = htmlData + """class='bg-info text-dark'"""
    htmlData = htmlData + """>
              <th>ETH0 MAC</th>
              <td>%(E0)s</td>
            </tr>
            <tr """ % dictString
    if(dictString["W0"] == "FF:FF:FF:FF:FF:FF"):
        htmlData = htmlData + """class='bg-warning text-dark'"""
    else:
        htmlData = htmlData + """class='bg-info text-dark'"""
    htmlData = htmlData + """>
              <th>WLAN0 MAC</th>
              <td>%(W0)s</td>
            </tr>
            <tr class="bg-info">
              <th>RPi Serial</th>
              <td>%(RPI)s</td>
            </tr>
            <tr """ % dictString
    if(dictString["BT"] == True):
        htmlData = htmlData + """class='bg-success text-white'"""
    else:
        htmlData = htmlData + """class='bg-danger text-white'"""
    htmlData = htmlData + """ >
              <th>BT Detected</th>
              <td>%(BT)s</td>
            </tr>
            <tr """ % dictString
    if(dictString["LOR"] == True):
        htmlData = htmlData + """class='bg-success text-white'"""
    else:
        htmlData = htmlData + """class='bg-danger text-white'"""
    htmlData = htmlData + """ >
              <th>LoRa OK?</th>
              <td>%(LOR)s</td>
            </tr>
            <tr """ % dictString
    if(dictString["LTE"] == True):
        htmlData = htmlData + """class='bg-success text-white'"""
    else:
        htmlData = htmlData + """class='bg-warning text-dark'"""
    htmlData = htmlData + """ >
              <th>LTE Detected</th>
              <td>%(LTE)s</td>
            </tr>
          </tbody>
        </table>
    </div>
    <div class="col">
      <h2 class="text-center">Support QR</h2>
      <div class="text-center">
        <img src="diagnosticsQR.png" class="img-thumbnail">
      </div>
    </div>
  </div>

</main><!-- /.container -->


  </body>
</html>
    """ % dictString
    return htmlData
