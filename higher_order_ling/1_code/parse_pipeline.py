# Pipeline for parsing the text grids for POS tagging using EC166_B11 as an example:


# You have to start off on the server in your terminal
# so log on using this
piassh

# after you've entered your password, go to your scripts directory
cd /home/ncahn/scripts

# before run the parse textgrid function you need the files you care about
# so copy over what you want to parse to your current wd
# you only neec to copy the .TextGrid over and not the .wav file
cp /data_store1/human/prcsd_data/EC166/EC166_B11/EC166_B11.TextGrid .


# once you've copied that over now you care about parse_textgrid.sh
# this takes 2 arguments: the text grid and the .wav file
# it will look like this:
./parse_textgrid.sh EC166_B11.TextGrid EC166_B11.wav

# when you run this, the output will be found in your current wd
# this is /home/ncahn/scripts
# the output will be a .data file
# EC166_B11.data
	# Almost there!
# Because your newly parsed .data file has the time stamps, you want to remove those and put it into a new .txt file
# Use this to do that
cat EC166_B11.data | awk '{$1="" ;$2="";$(NF)="";$(NF-1)="";$(NF-2)=""; print $0}'| sed 's/"//g' > EC166_B11.txt


# This will output in your current wd (/home/ncahn/scripts)
# now...how do I run nltk on this .txt file?
# for now, just drag and drop it into the higher_order_ling directory
# /Users/nathancahn/higher_order_ling

# now you can open your Jupyter notebook and get POS tags/tokens
# for the following I worked in a notebook out of /Users/nathancahn/higher_order_ling/1_code
# I outputed to /Users/nathancahn/higher_order_ling/2_pipeline/tmp

import nltk
import pandas as pd
import numpy as np

EC166_B11 = open("/Users/nathancahn/higher_order_ling/0_data/EC166_B11.txt")

results_EC166_B11 = []

for i in EC166_B11:
    tokens = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(tokens)
    results_EC166_B11.append(tokens) # alternate between tokens and tagged to change results
    print(results_EC166_B11)

 with open("/Users/nathancahn/higher_order_ling/tok_EC166_B11.txt", "w") as output:
    output.write(str(results_EC166_B11))