#!/bin/sh
#
# DESCRIPTION
# This is just a very thin wrapper around the neato (undirected grapher) piece of 
# GraphViz.
# Presently, it's not installed on gimli so I just use the version installed on fiery
# (my workstation) via SSH and redirect it to the browser here (the images are 
# never stored).
# This is probably VERY CPU expensive, but with 0MB used in harddrive space it is 
# a very clear example of Time Vs Space tradeoffs.
#
# CREATED BY: Shaun Meyer
#    CREATED: 18 Feb 2011
#

echo "Content-Type: image/png"
echo ""

GRAPHPATH=/home/staff/meyersh/public/graphs

# Get the GRAPH= query string out of $QUERY_STRING env variable.
GRAPH=`echo "$QUERY_STRING" | grep -oE "(^|[?&])GRAPH=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`

# Check if the file exists before trying to graph it.
if [ -e ${GRAPHPATH}/${GRAPH} ]; then
    /home/staff/meyersh/bin/dot_cli $GRAPH | 
    /home/staff/meyersh/bin/dot -Tpng -s50
fi
