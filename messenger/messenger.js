var numPosts = 0;

function clear_form() {
    /* Reset the submission form. */
    with (document.getElementById("submission_form")) {
        name.value = "Anonymous";
        post.value = "";
    }
}

function clear_posts() {
    /* Rest the posts div (for deletion/modifications) */
    posts = document.getElementById('posts');

    while (posts.childNodes.length) {
        posts.removeChild(posts.childNodes[0]);
    }
}

function parse_body(s) {
    /* Given a string, s, containing the body of a post, parse it and
       return a document element that can be inserted into a web
       page. */

    /* Markup language:
     * = BOLD
     / = ITALIC
     _ = UNDERLINE
     - = STRIKE-THRU
    */

    var parsed = document.createElement("div");
    var cur_node = parsed; 

    // Count how deep we are in a given tag (not yet implemented.)
    var parsing = {'*': 0,
                   '/': 0,
                   '_': 0,
                  };
    
    // Mapping of c -> tag elements
    var tag_element = {'*': 'B',
                       '/': 'I',
                       '_': 'U',
                      };

    // A stack (push for every tag symbol, then match/pop when we see
    // the closing symbol.)
    var parsing_stack = new Array();
    Array.prototype.top = function() {return this[this.length-1];};

    for (var i = 0; i < s.length; i++) {
        var c = s[i]; // The current character we're parsing.

        if (c in parsing) { // We've found a valid parse-token
            // Matched a closing tag
            if (c == parsing_stack.top()) {
                parsing_stack.pop();
                if (cur_node != parsed) {
                    cur_node = cur_node.parentNode;

                    // Matched an opening tag    
                } 
            }
            else {
                parsing_stack.push(c);
                var new_node = document.createElement(tag_element[c]);
                cur_node.appendChild(new_node);
                cur_node = new_node;
            }
        } 
        else {
            cur_node.appendChild( document.createTextNode(c));
        }
        
    }
    return parsed;
}

function read_post_from_json(json_str) {
    /* Add a given post (from JSON) to the posts div. */
    console.log("Reading post from JSON response.");
    var json_str = JSON.parse(json_str);
    console.log(json_str);

    if (document.getElementById(json_str['id']))
        return; // Ignore existing elements.

    var element          = document.createElement("div");
    element.setAttribute("id", json_str['id']);
    console.log("Handling id: " + element.id);
	var post_text        = json_str['body'];
 	var post_author_text = json_str['name'];
    post_author_text     = post_author_text ? post_author_text : "Anonymous";
    
    var datestamp = new Date(json_str['timestamp']);
    datestamp = datestamp.toLocaleString();

    var reply_link = document.createElement("a");
    reply_link.setAttribute('href', '#');
    reply_link.onclick = function() {
        // document.getElementById("reply-to").value = element.id;

        // I can't really imagine how to make this more brittle. 
        document.getElementById("reply-to").value = this.parentNode.parentNode.id; 
        console.log(this.parentNode.parentNode.id + " Called to respond to " + element.id);
    }
    reply_link.className = "control";
    reply_link.appendChild(document.createTextNode("[Reply to post " + json_str['id'] + "]"));

    var delete_link = document.createElement("a");
    delete_link.setAttribute('href', '#');
    delete_link.onclick = function() {
        // I can't really imagine how to make this more brittle. 
        remove_post(this.parentNode.parentNode.id);
        console.log("Marking " + this.parentNode.parentNode.id + " for deletion.");
        clear_posts(); // clear the posts div
        load_posts(); 
    }
    delete_link.className = "control";
    delete_link.appendChild(document.createTextNode("[Delete]"));

    var signature = document.createElement("div");
    signature.className = "signature";

    signature.appendChild(reply_link);
    signature.appendChild(delete_link)

    signature.appendChild(
        document.createTextNode(" " + post_author_text + " (" + datestamp + ") says:"));

	element.appendChild(signature);
    element.appendChild(parse_body(json_str['body']));

    if (document.getElementById(json_str['reply_to'])) {
        document.getElementById(json_str['reply_to']).appendChild(element);
        // Ensure that our color is the opposite of the parent
        element.className = document.getElementById(
            json_str['reply_to']).className == "even" ? "odd" : "even";
    }
    else {
        document.getElementById('posts').appendChild(element);
        // As a top-level post, ensure that the colors alternate. 
        element.className = document.getElementById('posts').childElementCount % 2 ? "odd" : "even";
    }

}



function read_posts_from_json(json_str) {
    console.log("Reading posts from JSON response.");
    var json_str = JSON.parse(json_str);
    console.log(json_str);

    for (var p = 0; p < json_str['posts'].length; p++) {
        if (document.getElementById(json_str['posts'][p]['id']))
            continue; // Skip existing elements.

        var element          = document.createElement("div");
        element.setAttribute("id", json_str['posts'][p]['id']);
        console.log("Handling id: " + element.id);
	    var post_text        = json_str['posts'][p]['body'];
 	    var post_author_text = json_str['posts'][p]['name'];
        post_author_text     = post_author_text ? post_author_text : "Anonymous";
        
        var datestamp = new Date(json_str['posts'][p]['timestamp']);
        datestamp = datestamp.toLocaleString();

        var reply_link = document.createElement("a");
        reply_link.setAttribute('href', '#');
        reply_link.onclick = function() {
            // document.getElementById("reply-to").value = element.id;

            // I can't really imagine how to make this more brittle. 
            document.getElementById("reply-to").value = this.parentNode.parentNode.id; 
            console.log(this.parentNode.parentNode.id + " Called to respond to " + element.id);
        }
        reply_link.className = "control";
        reply_link.appendChild(document.createTextNode("[Reply to post " + json_str['posts'][p]['id'] + "]"));

        var delete_link = document.createElement("a");
        delete_link.setAttribute('href', '#');
        delete_link.onclick = function() {
            // I can't really imagine how to make this more brittle. 
            remove_post(this.parentNode.parentNode.id);
            console.log("Marking " + this.parentNode.parentNode.id + " for deletion.");
            clear_posts(); // clear the posts div
            load_posts(); 
        }
        delete_link.className = "control";
        delete_link.appendChild(document.createTextNode("[Delete]"));

        var signature = document.createElement("div");
        signature.className = "signature";

        signature.appendChild(reply_link);
        signature.appendChild(delete_link)

        signature.appendChild(
            document.createTextNode(" " + post_author_text + " (" + datestamp + ") says:"));

	    element.appendChild(signature);
        element.appendChild(parse_body(json_str['posts'][p]['body']));

        if (document.getElementById(json_str['posts'][p]['reply_to'])) {
            document.getElementById(json_str['posts'][p]['reply_to']).appendChild(element);
            // Ensure that our color is the opposite of the parent
            element.className = document.getElementById(
                json_str['posts'][p]['reply_to']).className == "even" ? "odd" : "even";
        }
        else {
            document.getElementById('posts').appendChild(element);
            // As a top-level post, ensure that the colors alternate. 
            element.className = document.getElementById('posts').childElementCount % 2 ? "odd" : "even";
        }
    }
}

function new_post_element() {
    /* Fetch the form elements from the post form and create a post element for
     * insertion into a div. I wanted to do a proof-of-concent, so this does 
     * EXTREMELY basic parsing (Randy Campbell would be happy to see this Finite
     * State parser) which looks for text enclosed in slashes and places that
     * text in italics. 
     */

	var element          = document.createElement("div");
    element.id = numPosts + 1;
	var post_text        = document.getElementById("post").value;
 	var post_author_text = document.getElementById("name").value;
    post_author_text     = post_author_text ? post_author_text : "Anonymous";
    
    var datestamp = new Date();
    datestamp = datestamp.toLocaleString();


    var reply_link = document.createElement("a");
    reply_link.onclick = function() {document.getElementById("reply-to").value = element.id;}
    reply_link.setAttribute('href', '#');
    reply_link.appendChild(document.createTextNode("[Reply to post " + element.id + "]"));

    var signature = document.createElement("div");
    signature.className = "signature";

    signature.appendChild(reply_link);

    signature.appendChild( document.createTextNode(" " + post_author_text + " (" + datestamp + ") says:"))

	element.appendChild(signature);
	console.log("Parsing: " + post_text);

	var emph_buffer = "";
	var post_buffer = "";
	var parsing_emph = false; 
	for (var i = 0 ; i < post_text.length; i++) {
	    var c = post_text[i];
	    if (parsing_emph)
            emph_buffer += c;
        else
            post_buffer += c;

        if (c == "/") {
		    if (parsing_emph) {
			    // We've found the "closing tag."
                emph_buffer = "/" + emph_buffer; // prefix a slash.
                post_buffer = post_buffer.slice(0,-1); // remove trailing slash
                console.log("parsed emphasis: '" + emph_buffer + "'.");
 			    var new_emph = document.createElement("em");
			    new_emph.appendChild( document.createTextNode(emph_buffer) );

			    element.appendChild( document.createTextNode(post_buffer) );
			    element.appendChild( new_emph );
                emph_buffer = "";
                post_buffer = "";
		    } else {
                emph_buffer = "";
		    }
            parsing_emph = !parsing_emph; 
        } 
	    
	} 	  

    // Fetch text from any remaing buffers into the element. 
    element.appendChild( document.createTextNode(post_buffer + emph_buffer) );
    return element;
}

function submit_post() {
    /* insert a new post element into the posts div. */
    // var posts = document.getElementById("posts");
    // var new_post = new_post_element(); 
    // new_post.className = posts.childElementCount % 2 ? "odd" : "even";
    // var reply_to = document.getElementById("reply-to").value;

    // if (reply_to == Number(0) || document.getElementById(reply_to) == null) {
    //     console.log("Adding top-level post (ID: " + new_post.id + ")");
    //     posts.appendChild(new_post);
    // } else {
    //     console.log("Adding reply post (ID: " + new_post.id + ") replies to " + reply_to);
    //     new_post.className = document.getElementById(reply_to).className == "odd" ? "even" : "odd";
    //     document.getElementById(reply_to).appendChild(new_post);
    // }

    
    var json_post = JSON.stringify(
        {'action': 'NEW_POST',
         'name': document.getElementById('name').value, 
         'reply_to': document.getElementById('reply-to').value, 
         'body': document.getElementById('post').value});

    console.log("Sending JSON: " + json_post);
    sendData(json_post, 
             "http://gimli.morningside.edu/~meyersh/messenger/messages.py", 
             "POST",
              read_post_from_json);

    clear_form();
    numPosts++;
}

function load_posts() {
    var json_post = JSON.stringify({'action': 'READ_POSTS'});

    sendData(json_post, 
             "http://gimli.morningside.edu/~meyersh/messenger/messages.py", 
             "POST", 
             read_posts_from_json);
}

function remove_post(post_id) {
    var json_post = JSON.stringify({'action': 'DELETE_POST', 
                                    'post_id': post_id});
    sendData(json_post, 
             "http://gimli.morningside.edu/~meyersh/messenger/messages.py", 
             "POST");

}

document.onload = load_posts();
