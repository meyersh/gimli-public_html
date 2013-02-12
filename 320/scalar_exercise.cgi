#!/usr/bin/perl -wT
# The Scalar Exercise (compute the area of a trapazoid)
# Shaun Meyer, Feb 2013

print "Content-Type: text/html\n\n";

my $base_a = 20;
my $base_b = 50;
my $height = 40;
my $area   = (.5 * $height * ($base_a + $base_b));

print <<"EOF";
<html>\n
    <head>\n
      <title>Trapezoid page</title>\n
    </head>\n
    <body>\n
      <h3>The Trapezoid Page</h3>\n

      <p><i>Shauns page that calculates and prints the area of a
      trapezoid.</i></p>\n

      <p>
        Base: $base_a<br/>\n
        Second Base: $base_b<br/>\n
        Height: $height<br/>\n

        Area (1/2 x height x (base<sub>1</sub>+ base<sub>2</sub>)):
        $area<br/>\n

      </p>\n
    </body>\n
</html>
EOF
exit 0;
