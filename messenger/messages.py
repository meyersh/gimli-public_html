#!/usr/bin/env python
# Message handler for class project
# Shaun Meyer, Feb 2013
#

import sys
import cgitb
import cgi
import json
import sqlite3
import hashlib 
import datetime
import os

cgitb.enable()

print "Content-type:text/plain\n"

posts_dir = "/home/staff/meyersh/private/"
posts_suffix = ".post"
posts_database = "/home/staff/meyersh/private/messages.sqlite"

now = datetime.datetime.now()

POST_DATA = json.load(sys.stdin)
#print POST_DATA

if 'action' not in POST_DATA:
    print('{}')
    exit;

class Post(object):
    """ A post container. We populate this with data from json operations. """
    def __init__(self, data):
        """ kwargs should be a dictionary with keys 'name', 'body', and 
        'reply_to'. Lets unpack these into self.name, etc. """
        self.timestamp = now

        self.__dict__.update( data )

        if not isinstance(self.timestamp, datetime.datetime):
            self.timestamp = datetime.datetime.strptime(self.timestamp, "%Y-%m-%dT%H:%M:%S.%f")

        if self.name is None:
            self.name = "Anonymous"

    def hash(self):
        # Generate a hash of the post.
        h = hashlib.md5()
        h.update(self.name)
        h.update(self.body)
        h.update(self.reply_to)
        return h.hexdigest()

    def toJson(self):
        return json.dumps(self.toDict(), indent=4, sort_keys=True)

    def toDict(self):
        return {'name': self.name,
                'body': self.body, 
                'reply_to': self.reply_to,
                'id': self.hash(),
                'timestamp': self.timestamp.isoformat(),
                }

def post_exists(post_id):
    return os.path.exists(posts_dir + post_id + posts_suffix)

def read_post(post_id):
    if not post_exists(post_id):
        return None

    with open(posts_dir + post_id + posts_suffix) as f:
        return Post(json.load(f))

    return None

def remove_post(post_id):
    try:
        if post_exists(post_id):
            os.remove(posts_dir + post_id + posts_suffix)

        conn = sqlite3.connect(posts_database)
        c = conn.cursor()
        c.execute("DELETE FROM message_index WHERE msg_id=?", (post_id,))
        c.close()
        conn.commit()
    except:
        return False
    return True

if POST_DATA['action'] == "NEW_POST":

    def write_post(post):
        # Write to File.
        post_file = posts_dir + post.hash() + posts_suffix

        print post.toJson()

        with open(post_file, 'w') as file:
            file.write(post.toJson())

        # Now write to DB
        conn = sqlite3.connect(posts_database)
        c = conn.cursor()

        c.execute("INSERT INTO message_index VALUES (?,?,?)", (post.hash(), post.reply_to, now ))
        conn.commit()
        c.close()

    # Create new post, write it to the file, and return it to the ajax 
    # for display.
    new_post = Post(POST_DATA)
    if not post_exists(new_post.reply_to):
        new_post.reply_to = "root"

    write_post(new_post)

elif POST_DATA['action'] == "DELETE_POST":
    if 'post_id' in POST_DATA:
        if remove_post(POST_DATA['post_id']):
           pass; # This will signal the js to remove the post. 

elif POST_DATA['action'] == "READ_POSTS":
    ''' Paruse the SQlite database of post indexes for posts that should
    be displayed. The SQlite schema was created with:

    CREATE TABLE message_index (msg_id TEXT PRIMARY KEY, 
                                reply_to TEXT, 
                                timestamp DATE);
                                '''
    conn = sqlite3.connect(posts_database)
    
    c = conn.cursor()

    rootc = conn.cursor()
    rootc.execute("SELECT * FROM message_index ORDER BY (reply_to == 'root') DESC, timestamp ASC")

    result_set = []
    for (msg_id, reply_to, timestamp) in rootc.fetchall():
        result_set.append(read_post(msg_id).toDict())        

    print json.dumps({'action': 'ALL_POSTS', 'posts': result_set}, indent=4)

else:
    print("Something went wrong.")
