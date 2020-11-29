# BasicFileSplitter
Very basic file splitter in Python 2.

# Background
It was created in 2008, where I was still learning how to program. What I wanted to achived from this, is to know how the very famous [Hacha](http://hacha.com.es) application worked.

It operated by reading the full file (and storing it in virtual memory) and then split in chunk files. Later I noticed that you can optimize this by reading only chunk size, writing the chunk file, discard current chunk data and go to next one.
