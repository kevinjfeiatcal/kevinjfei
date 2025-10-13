# homework 5
"""
 git vs github:
    git is the terminal (language it uses) and github is online website useful for sharing projects.

terminal vs command line:
    the command line is the method of interaction with the terminal, which lets one run code directly from the computer.

local vs remote repo:
    local is on computer, remote is online

version control:   
    records changes to files so one can revert or collarboate on it safetly.

staging area:
    where git stores files that are ready to be committed. 

git add:
    adds files to the staging area

git commit:
    saves the changes locally

git push:
    sends changes to the remote repo

git status:
    tells about the status of the files 

git pull:
    pulls from the remote repo

pwd:
    tells about the working directory

ls:
    lists all the things inside the working directory

cd:
    moves around directories

nano:
    text editor in the terminal

touch:
    makes new file

mv: 
    moves or renames file

rm:
    deletes 

cat:
    prints contents of a file


 --  Judy's Directory System -- 

 1: pwd
 2: ls
 3: cd to move, then pull
 4: mv (file name) (directory)
 5. cd
 6: cat
 7: git add, git commit, git push origin main
 8: perhaps pull first 
    git pull origin main, git push origin main

 """

# 4.1:
def checkDataType(var):
    return type(var).__name__

# 4.2:
def evenOrOdd(int):
    if int % 2 == 0:
        return "Even"
    return "Odd"

# 5:
def sumWithLoop(list):
    total = 0
    for i in list:
        total += i
    return total

# 6.1
def duplicateList(list):
    newList = []
    for item in list:
        newList.append(item)
        newList.append(item)
    return newList

# 6.2
def square(num):
    return num**num


print(duplicateList([1,2,3,4,5]))
