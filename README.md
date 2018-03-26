# num-sum
A script to score the cumulative sum of a list of digits

 - `numgen.py` generates this list
 - `numchk.py` outputs the score

# numgen
Run this script and enter:
 - The number of tests to generate (`a`)
 - The number of digits per test (`b`)

This will generate `a` files with `b` digits each

They will be named `q_###.txt`. For example, `q_012.txt`

# numchk
Before running this script you must create a `.txt` file for each answer in the same format as `q###.txt`, and name it `a_###.txt`.

Place these files in the same directory as `numchk.py` then run the script.

For example:

|`q000.txt`|`a000.txt`|
|:--------:|:--------:|
|3|3|
|1|4|
|4|8|
|1|9|
|5|14|
|9|23|

Output: `000 6 0 6`

[file id, # correct, # wrong, # total]

|`q001.txt`|`a001.txt`|
|:--------:|:--------:|
|3|3|
|1|4|
|4|8|
|1|9|
|5|20|
|9|29|

Output: `000 5 1 6`

Explanation: 9+5=20 is wrong, so the cumulative sum is replaced. Then, 20+9=29 is correct
