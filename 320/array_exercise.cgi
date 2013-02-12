#!/usr/bin/perl

# Generate two random dice rolls (6-sided) and display the
# distribution chart of 36,000 rolls.
#
# Shaun Meyer, Feb 2013
#

my $sides     = 6;
my $num_dice  = 2;
my $num_rolls = 36000;
my @results   = ();

# Generate one random roll.
sub roll_die {
    int(rand($sides));
}

# The sum of two die
sub sum_of_roll {
    &roll_die + &roll_die;
}

# Populate the results
for ($i = 0; $i < $num_rolls; $i++) {
    $results[&sum_of_roll]++;
}

print "Content-Type: text/html", "\n\n";
print <<"HEAD";
<html>
  <head>
    <title>Die Rolling.</title>
    <link rel="stylesheet" type="text/css" href="/~meyersh/bootstrap/css/bootstrap.css">
  </head>
  <body>
  <div class="container-fluid">
    <div class="fluid-row">
    <div class="span5">
    <h3>Dice Rolling!</h3>

  <table class="table-bordered table-striped">
    <caption>Rolled dice 36,000 times.</caption>
  <thead><td>Sum of Dice</td><td>Occurrences</td></thead>
HEAD

for ($i = 0; $i < @results; $i++) {
    my $val = $results[$i];
    my $sum = $num_dice + $i;
    print "<tr><td>$sum</td><td>$val</td></tr>\n";
}

print <<"FOOT";
    </table>
  </div></div></div>
  </body>
</html>
FOOT
