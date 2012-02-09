#!/usr/bin/env python
import os,string
print "Content-Type: text/html"
print ""
print ""
print "<html><body><pre>"

slices={}


import re,cgi,cgitb

# Some cgi debugging output for the browser
cgitb.enable()

def parseHTML(f):
    # Parse file `f` and get us the contents of tag...
    # intended to retrieve meta stuff.
    meta_regex = re.compile('<META NAME="(.*)" CONTENT="(.*)">',
                            re.IGNORECASE)
    returns = {'author':None, 'desc':None}
    fh = open(f)
    for line in fh:
        result = meta_regex.search(line)
        if result:
            if (result.group(1).upper() == 'AUTHOR'):
                returns['author'] = result.group(2)
            elif (result.group(1).upper() == 'DESCRIPTION'):
                returns['desc'] = result.group(2)
    return returns
    
def tryint(s):
    try:
        return int(s)
    except:
        return s
    
def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
    "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    return l.sort(key=alphanum_key)
    
# Peruse the cgi files...
files = {}
for file in os.listdir('.'):
    if file.endswith('.cgi'):
        file = file.split('.')
        if file[0].startswith('S'):
            print file

htmldir = '/home/meyersh/public_html/'
for file in os.listdir(htmldir):
    if file.endswith('.html'):
        if file not in files:
            files[file] = {}
            files[file]['type'] = '.html'
            meta = parseHTML(htmldir+file)
            files[file]['author'] = meta['author']
            files[file]['desc'] = meta['desc']

        filename = file
        meta = parseHTML(htmldir + filename)
        file = file.split('.')
        if file[0].startswith('S'):
            (slice, part, piece) = (file[0], file[1], file[2])
            
            if slice not in slices:
                slices[slice] = {}
                slices[slice]['filename']=filename
                slices[slice]['desc']=meta['desc']
                slices[slice]['author']=meta['author']
                slices[slice]['parts']={}
            if part not in slices[slice]['parts']:
                slices[slice]['parts'][part] = {}
                slices[slice]['parts'][part]['desc']=meta['desc']
                slices[slice]['parts'][part]['author']=meta['author']
                slices[slice]['parts'][part]['filename'] = filename
                slices[slice]['parts'][part]['pieces'] = {}
            if (piece != 'html'):
                if piece not in slices[slice]['parts'][part]['pieces']:
                    slices[slice]['parts'][part]['pieces'][piece]={}
                    slices[slice]['parts'][part]['pieces'][piece]['filename']=filename
                    slices[slice]['parts'][part]['pieces'][piece]['author']=meta['author']
                    slices[slice]['parts'][part]['pieces'][piece]['desc']=meta['desc']

print slices
keys = slices.keys()
sort_nicely(keys)

print "<h3>Slices:</h3>"
# Keys are unsorted by default in a dictionary...
keys = slices.keys()
sort_nicely(keys)

base_url='http://gimli.morningside.edu/~meyersh'
for slice in keys:
    print "Slice %s" % slice
    for part in slices[slice]:
        print "  %s: %s" % (part, slices[slice][part])
        if ( part == "parts" ):
            for p in slices[slice][part]:
                print "    %s:: %s" % (p, slices[slice][part][p])
                if ( p == 'pieces' and slices[slice][part][p] ):
                    pieces = slices[slice][part][p]
                    for piece in pieces:
                        print "      %s - %s" % (piece, pieces[piece])

requested_slice=cgi.FieldStorage().getfirst('s')
requested_part=cgi.FieldStorage().getfirst('e')

if requested_slice:
    print "<p>Slice! %s" % requested_slice
    if requested_part:
        print "Part! %s" % requested_part
    print "How do we know the description, etc???"
print "</pre></body></html>"
