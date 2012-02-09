#!/usr/bin/php-cgi
<?PHP
   $url = 'http://gimli.morningside.edu/~meyersh/gitweb/?p=git;a=rss';
   $MAX_POSTS=4;
   ?>
<!doctype html>
<head>
  <title>Shauns CSCI-310 Page!</title>
  <link rel="stylesheet" href="css/screen.css" type="text/css" />

</head>
<body class="index">
  
  <div class="nav">
    <ul>
      <li class="date">
		<script type="text/javascript">
		  <!-- 
			   // Array of day names
			   var dayNames = new Array("Sunday", "Monday", "Tuesday", "Wednesday", 
			   "Thursday", "Friday", "Saturday");
			   var now = new Date();
               document.write("Happy " + dayNames[now.getDay()] + ".");
               // -->
        </script>
      </li>
      <li class="home"><a href="~/meyersh">Home</a></li>
      <li><a href="gitweb/">Code</a></li>
      <li><a href="about.html">About Me</a></li>
  </div>
  
  <div class="container">
    <div class="box-container" id="products">
      <div class="headline">
		<h1>Shaun Meyer's CSCI WebPage</h1>
		<h5>Welcome to my <del>CSCI-310</del> Website. Hopefully all kinds of cool things will go here.</h5>
      </div>
    </div>

    <hr/>

  </div>
  <div class="box-container manifesto">

    <div class="belief">
      <div class="column">
		<div class="belief top">
		  <h3>News</h3>
		  <h4>Nov/2011</h4>
          <p>New page layout and it's completely fluid!</p>

		</div>
      </div>
    </div>

    <div class="belief">
      <div class="column">
		<div class="belief top">
		  <h3>Git</h3>
		  <h4>Git is Magic</h4>
		  <p>You won't regret learning this powerful code management tool. Try this 
			<a href="http://www-cs-students.stanford.edu/~blynn/gitmagic/">spellbook.</a>
		</div>
      </div>
    </div>
    
    <div class="belief">
      <div class="column">
		<div class="belief top">
		  <h3>Code</h3>
		  <h4>Source browser</h4>
		  <p>Source code & Changelog is available for browsing/download 
			<a href="http://gimli.morningside.edu/~meyersh/gitweb/">here.</a></p>
		</div>
      </div>
    </div>
    
    <div class="belief">
      <div class="column">
		<div class="belief top">
		  <h3>Paper</h3>
		  <h4>CSCI-270: Paper - Rock - Scissors game.</h4>
		  <p><a href="prs/">Play</a> Paper, Rock, Scissors against the computer.</p>
		</div>
      </div>
    </div>




    <div class="belief">
      <div class="column">
		<div class="belief top">
		  <h3>Javascript</h3>
		  <h4><A href="http://gimli.morningside.edu/~meyersh/310/bfs/">
			  Tabular adjacency matrix example</a></h4>
		  <p>As promised in class (and nearly finished) example of 
			Slice 3 Project 2.</p>
		</div>
      </div>
    </div>

  </div>

  <hr/>

  <div class="customers">
    <h2>Latest updates to the Git Repo</h2>
    <p>
	  <?PHP
		 require_once("magpierss/rss_fetch.inc");
		 $rss = fetch_rss($url);
		 $counter = 0;
		 foreach ($rss->items as $item) {
	  $href = $item['link'];
	  $title = $item['title'];
      $author = $item['author'];
	  $pubDate = $item['pubDate'];             
	  echo "<p><a href=$href>$title</a> ($author$pubDate)</p>";
      $counter++;
      if ($counter > $MAX_POSTS) { break;}
      }
	  ?>
    </p>

  </div>

  <hr/>

  
  <div class="footer">
    <p>All <del>text and</del> design is copyright ©1999-2011 37signals, LLC. All rights reserved.</p>
  </div>

</div>
</body>
</html>
