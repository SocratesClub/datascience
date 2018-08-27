import nltk, pymysql

infilename = input("Enter the name of the file to index: ")

# Change this line to match your MySQL server settings
conn = pymysql.connect(user="dsuser", passwd="badpassw0rd", db="dsbd")
cur = conn.cursor()

QUERY = "INSERT INTO indexer (word,position,pos) VALUES "
wpt = nltk.WordPunctTokenizer()

offset = 1
with open(infilename) as infile:
    # Process the text incrementally, one line at a time
    # A word cannot span across lines, anyway!
    for text in infile:
        # Tokenize and add POS tags
        pieces = enumerate(nltk.pos_tag(wpt.tokenize(text)))
        
        # Create a query; do not forget to escape the words!
        words = ["(\"%s\",%d,\"%s\")" % (conn.escape_string(w), 
                                         i + offset, 
                                         conn.escape_string(pos)) 
                 for (i, (w, pos)) in pieces]
        
        # Execute the query
        if words:
            cur.execute(QUERY + ','.join(words))

            # Advance the word pointer
            offset += len(words)

# Commit the changes
conn.commit()
conn.close()
