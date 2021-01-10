#The code that generates the HTML
def generateHTML(jsonString):
    htmlData = """

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.79.0">
    <title>Starter Template · Bootstrap v5.0</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/starter-template/">



    <!-- Bootstrap core CSS -->
<link href="css/bootstrap.min.css" rel="stylesheet">

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
      <h2 class="text-danger text-center">Everything's Broke!</h2>
    </div>
  </div>
<hr/>
  <div class="row">
    <div class="col">
      <h2 class="text-center">Diagnostics Breakdown</h2>
    </div>
    <div class="col">
      <h2 class="text-center">Support QR</h2>
    </div>
  </div>

</main><!-- /.container -->


  </body>
</html>
    """
    return htmlData
