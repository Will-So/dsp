# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

Command | Notes
-- | --
json2csv -k user.name,remote_ip -i input.json -o output.csv | Handels nested csv as well via user.name where name is nested in user. -k is the fields
cat ch1.md &#124; wc | basic  piping of ch1 to wc
git shortlog -s -n | -s counts the number of commits; -n sorts by number of commits. 
wc -l newdataset.csv | Returns the number of lines
`head -1 newdataset.csv | wc -w`| returns the number of columns in a file IF every column name is only 1 word. This is usually the case with csv files and virtually always the case with tsv files. Run just the first command first to verify that this is the case.
rm -R temp | recursively removes a folder
chmod -R 777 /dir | Only use on non-important VPS. 
head -20 filename |
`>>` | appends to a file
sh -c | Creates a child process shell which inheretics parent shell's env
sed -n '500000,$p' data.txt > file.txt | -n supresses input. 
sed -n '1,4d' data.txt | deletes lines
more text.txt
`ps -fA | grep python`
df -h 
set -e | runs script to completion ignoring errors
open -e ~/.bash_profile
git status -v | shows line by line differences since last commit
sudo fdisk -h | Only works on Ubuntu; shows all available drives
git branch -a | Shows all branches, including remote ones
!! | Repeats last command
cc vs gcc | usually linked to the same file 







---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

`ls` lists all of the files in the directory. `ls -a` lists all of the files, including hidden files, in the directory. `ls -l` lists more details about each of the files. `ls -lh` makes it easier to read how big each of the files are. If we are interested in the size of all of the files, then it makes sense to even combine all 3. `ls -lah`

---


---

What does `xargs` do? Give an example of how to use it.

xargs reads items and executes the command one or more times. ` find Devel/ -name "*.py" | xargs wc -l`. Number of lines of all of the Python files in Devel directory

---

