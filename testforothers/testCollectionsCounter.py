#!/usr/bin/env python
# coding: utf-8
from collections import Counter
text='Welcome to the worlds largest collection of computer and technology related tutorials on the web. Feel free to browse through our library of over 7,000 videos and tutorials. We have courses in programming, web design, video editing, game development, and more. Join the over 180 million people who have already enjoyed the benefits of online learning.'
words=text.split()
print words
counter=Counter(words)
top_three=counter.most_common(3)
print top_three
