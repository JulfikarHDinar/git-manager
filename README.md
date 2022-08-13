## GIT Manager
 <br/>
We are about to create a GIT Manager on console using Python 3. We cannot use any database or UI framework. For Managing GIT we need to follow our custom command. Our Commands is listed below - <br/>
 <br/>
 
**1. git init**   <br/>
-- This command will be the start of GIT Manager. Without this command, we cannot execute other command. <br/>
 <br/>
 
**2. git commit "commit message"**   <br/>
-- By this command, we will store this commit message with a auto generated sequence number. The sequence number must be integer and start with 1. <br/>

**3. git show commit** <br/>
-- By this command, we can show the current commit message. <br/>
 <br/>
**4. git show all commit** <br/>
-- By this command, we can view all commit commit message with sequence number. Need to show star on current commit. Like - <br/>
\*1 message-one <br/>
2 message-two <br/>
3 message-three <br/>
 <br/>
**5. git delete commit_number** <br/>
-- By this command, we can delete specified commit with mentioned commit_number. If commit number is current commit then current commit pointer will move backward. <br/>
 <br/>
**6. git jump commit_number** <br/>
-- By this command, we can jump to an specific commit_number. Then Commit sequence will change as the specified commit-number will be current commit. For example – we have three commit message as - <br/>
\*1 message-one <br/>
2 message-two <br/>
3 message-three <br/>
 <br/>
(here \* means current commit). Now we execute "git jump 3". then current commit will be 3 and sequence will change. Output will be - <br/>
\*3 message-three <br/>
1 message-one <br/>
2 message-two <br/>
 <br/>
**7. git move back** <br/>
-- By this command, Our current commit pointer will be one step backward. And Sequence will remain same, only pointer will move. For example – we have three commit message as - <br/>
\*1 message-one <br/>
2 message-two <br/>
3 message-three <br/>
 <br/>
(here \* means current commit). Now we execute git move back. then current commit will be 2. Output will be - <br/>
1 message-one <br/>
\*2 message-two <br/>
3 message-three <br/>
 <br/>
(special note: on any point when when we commit new message using second command, then new message will be current commit pointer and anything that was forward will be deleted. For example <br/>
– we have three commit message as - <br/>
1 message-one <br/>
\*2 message-two <br/>
3 message-three <br/>
(here \* means current commit). Now we execute git commit "new message". then current commit will be 4 and sequence will change. Output will be - <br/>
\*4 new message <br/>
2 message-two <br/>
3 message-three) <br/>
 <br/>
**8. git update "New Message"** <br/>
-- By this command, we can update current commit message. <br/>
 <br/>
**9. exit** <br/>
-- this the the termination command. <br/>
 <br/>
 <br/>
**INPUT** – is a line of string as command <br/>
**OUTPUT** – Only with command 3 & 4 we can see the output <br/>
 <br/>
 <br/>
| Sample Input  | Sample Output |
| ------------- | ------------- |
| git init  | commit message three |
| git commit “commit message one”  | \*3 commit message three |
| git commit “commit message two”  | 2 commit message two |
|git commit “commit message three” | 1 commit message one  |
|git show commit  | \*2 commit message two  |
| git show all commit  |3 commit message three  |
| git jump 2 | 1 commit message one |
| git show all commit  |\*4 commit message four |
| git move back  | 3 New message |
| git update “New Message”  | 1 commit message one |
| git commit “commit message four”  |  |
| git show all commit  |    |
| exit |   |
|   |   |
