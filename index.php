#!/usr/bin/php-cgi
<?PHP
   $url = 'http://gimli.morningside.edu/~meyersh/gitweb/?p=git;a=rss';
   $MAX_POSTS=4;
   ?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Shauns CSCI website">
    <meta name="author" content="Shaun Meyer">
    <title>Shauns CSCI-310 Page!</title>
    <!-- <link rel="stylesheet" href="css/screen.css" type="text/css" /> -->
    <!-- Le styles -->
    <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
  </head>
  <body>
    
    <div class="navbar">
      <div class="navbar-inner">
        <a class="brand" href="#">Title</a>
        <div class="container-fluid">
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="navbar-text">
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
              <li class="active"><a href="~/meyersh">Home</a></li>
              <li class="inactive"><a href="gitweb/">Code</a></li>
              <li class="inactive"><a href="about.html">About Me</a></li>
          </div>
        </div>
      </div>
    </div>

    <header class="jumbotron subhead" id="overview">
      <div class="container-fluid">
        <h1>Shaun Meyer's CSCI WebPage</h1>
	    <p class="lead">Welcome to my <del>CSCI-310</del> Website. 
          Hopefully all kinds of cool things will go here.</p>
      </div>
    </header>

    <div class="container-fluid">
      <div class="row-fluid">

        <div class="span12">
          <h2>Development tricks</h2>
          <p>Tools to build tools, it's just turtles all the way down.</p>
          <h3>Makefiles</h3>
          <p>If you're not using makefiles, you're typing way more than you have to. </p>
          <p>Have a file, <tt>whatever.cpp</tt>? To compile it just type 
            <pre>make whatever</pre>
            Thanks to the power of implicit make rules, this will execute something like
            <pre>g++ whatever.cpp -o whatever</pre></p>

          <p>Make also leads right into our next section, coding
          across multiple files</p>

            
          <h3>Coding across multiple files</h3>
          <p>Are you using multiple files? Combined with make files, code reuse can be a breeze.</p>

          <p>You've just polished off your new
          function, <code>vector_summation()</code>. It's brilliant and
          will save you hours everywhere. It looks like this:
            <pre>
int vector_summation(vector<int> vec) 
{
  int res = 0;
  for (int i = 0; i < vec.size(); i++)
    res += vec[i];

  return res;
}</pre></p>
                      
          <p>Now how to get it into as many programs as possible? My
          recommendation here is to save it into a cpp file,
          perhaps <tt>vector_helpers.cpp</tt> will be generic enough
          for future expansion. Now, put the function prototype along
          with a header guard into something
          like <tt>vector_helpers.hpp</tt>.</p>
          
          <p>You'll find <tt>vector_helpers.hpp</tt> looking like this:
<pre>#ifndef __VECTOR_HELPERS_HPP__
#define __VECTOR_HELPERS_HPP__

int vector_summation(vector<int> vec);

#endif</pre>
          
          <p>Now, in any file you want to use this function from put <code>#include "vector_helpers.hpp"</code> at the top.
          <p>All that remains is to compile and link. If you're
          incredibly ambitious, you type this every single time you
          want to compile:
            <pre>g++ vector_helper.cpp myprog.cpp -o myprog</pre> 

            Why would you this type this more than once?? Crack open a file
            called <tt>Makefile</tt> in the same directory and add the
            following:

            <pre>myprog: vector_helper.cpp myprog.cpp
        g++ vector_helper.cpp myprog.cpp -o myprog
            </pre>

            <p>This stanza isn't as hairy as it seams. The first thing
            (before the colon), <code>myprog</code>, is
            the <i>target</i>. Typing <code>make myprog</code> will
            cause make to examine this target. To the right of the
            colon are the <i>dependencies</i>. This says that myprog
            depends on <code>vector_helper.cpp</code>
            and <code>myprog.cpp</code>. If either one of them is
            newer than the <tt>myprog</tt> binary, make will
            rebuild. Otherwise make knows there is no need to
            recompile. You can hammer on <code>make myprog</code> all
            day and it will only re-compile if one of its dependencies has changed.</p>

            <p>The following line is indented by a <i>tab</i>(this is
            important). <code>g++ vector_helper.cpp myprog.cpp -o
            myprog</code> directs make with the command to execute to
            create this target. We're being somewhat sloppy here, but
            this notifies <tt>make</tt> with the exact command to
            enter.</p>

        </div>
      </div>        
      <div class="row-fluid">

        <div class="span12">
          <h3>Git is Magic</h3>
          <p>You won't regret learning this powerful code management tool. Try this 
		    <a href="http://www-cs-students.stanford.edu/~blynn/gitmagic/">spellbook.</a>
	    </div>

        <div class="span3">
            <h4>Pente WebApp</h4>
            <p><a href="431/pente">A work in progress, should be awesome.</a></p>
        </div>

	    <div class="span3">
	      <h4>Source browser</h4>
	      <p>Source code & Changelog is available for browsing/download 
		    <a href="http://gimli.morningside.edu/~meyersh/gitweb/">here.</a></p>
	    </div>

	    <div class="span3">
	      <h3>Paper</h3>
	      <h4>CSCI-270: Paper - Rock - Scissors game.</h4>
	      <p><a href="prs/">Play</a> Paper, Rock, Scissors against the computer.</p>
	    </div>

	    <div class="span3">
	      <h3>Javascript</h3>
	      <h4><A href="http://gimli.morningside.edu/~meyersh/310/bfs/">
		      Tabular adjacency matrix example</a></h4>
	      <p>As promised in class (and nearly finished) example of 
		    Slice 3 Project 2.</p>
	    </div>


        <div class="span9">
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


      </div>
  </body>
</html>
