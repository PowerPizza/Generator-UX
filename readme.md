# !N∞

Generates all the possible combination for a given set of unique characters.
---
This project creates all the possible combinations of desired length from a given set of unique characters and puts time in an output file.
For example if we have given *ABC* as set of unique characters so possible combination of 2 length from this string are : *AA*, *BB*, *CC*, *AB*, *AC*, *BA* etc...

# How to use in termux
Run the following commands :
```
apt update && apt update
pkg install git
pkg install python
git clone https://github.com/PowerPizza/Generator-UX
cd Generator-UX
ls
pip install -r requirements.txt
python generator_ux.py
```

do *ls* to see output file in your present working directory.

# Purpose of project
1. To generate word lists.
2. To use in brute force attack.
3. For testing of combination regarding projects.

# Prompts
**1. Do you want to continue with this one?**

This prompt asks you to choose unique character list there is one by default present but you can provide your own as well...

**2. Length of combination**

Combination length you need like of 3 characters or 7 characters etc...

**3. Enter output file name**

File will be created in PWD, containing all the unique combinations of provided character list.