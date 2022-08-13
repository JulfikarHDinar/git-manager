# @title Created Functions
def gitCommit(clist, cmtMsg, commitCnt):
    #print(cmtMsg)
    #print(cmtMsg[1:-1])    #excluding quoetes 
    list1 = []
    for i in clist:
        if i[0] != '*':
            list1.append(i)
        elif i[0] == '*':
            list1.append(i[1:])
            break

    list1.append('*'+str(commitCnt)+' '+cmtMsg)

    clist = list1
    return clist

def gitShowCommit(clist):
    for i in clist:
        if i[0] == '*':
            i = i.split()
            currcmt = i[1:]
    currcmt = ' '.join(str(e) for e in currcmt)
    print(currcmt)

def gitShowAllCommit(clist):
    for i in range(len(clist), 0, -1):
        print(clist[i-1])

def gitRemove(clist, rvNum):
    currRmvd = 0
    prev = ''

    for i in clist:
        j = i.split()
        #print(j[0]) #commit number
        if j[0] == rvNum:
            try:
                clist.remove(i)
            except:
                pass

        elif j[0][0] == '*' and j[0][1:] == rvNum:
            #print(j[0][1:]) #commit number (star)
            currRmvd = 1

        if currRmvd != 1:
            prev = i

    if len(prev) != 0 and currRmvd == 1:
        list1 = []
        for i in clist:
            #print(i[0])
            #print(i)
            if i == prev:
                list1.append('*'+i)
            elif i[0] == '*':
                list1.append(i[1:]) 
            else:
                list1.append(i)
        currRmvd = 0
    else:
        list1 = clist

    clist = list1
    #print(clist)
    return clist

def gitJump(clist, jmpNum):
    chck = 0
    llist2 = []
    llist3 = []

    for i in clist:
        j = i.split()
        #print(j[0]) #first number
        if j[0][0]  == '*':
            if j[0][1:] == jmpNum:
                chck = 1
            #print(i[1:])
            llist2.append(i[1:])
        else:
            if j[0] == jmpNum:
                chck = 1
            #print(i)
            llist2.append(i)

    for i in llist2:
        j = i.split()
        #print(i[0]) #int val
        if j[0] != jmpNum:
            llist3.append(i)

    for i in llist2:
        j = i.split()
        #print(i[0]) #int val
        if j[0] == jmpNum:
            llist3.append('*'+i)

    if chck == 1:
        clist = llist3
        chck = 0
        
    #print(clist)   
    return clist

def gitMoveBack(clist):
    prev = ''
    for i in clist:
        j = i.split()
        #print(j[0]) #num
        if j[0][0] == '*':
            #print(j[0].replace('*','')) #without * num
            break
        prev = i

    if len(prev) != 0:
        list1 = []
        for i in clist:
            #print(i[0])
            #print(i)
            if i == prev:
                list1.append('*'+i)
            elif i[0] == '*':
                list1.append(i[1:]) 
            else:
                list1.append(i)
    else:
        list1 = clist

    clist = list1
    return clist

def gitUpdate(clist, newMsg):
    llist2 = []

    for i in clist:
        j = i.split()
        #print(j[0]) #first number
        if j[0][0]  == '*':
            #print(str(j[0])+' '+newMsg)
            llist2.append(str(j[0])+' '+newMsg)
        else:
            llist2.append(i)

    clist = llist2
    return clist
    
################################################################################
def gitCommandString(clist):
    #str2 = input().split()
    commitCnt = 1   #Commit Count
    str2 = ''

    while True:
        str2 = input('[CMD]: ')
        #str2 = 'git commit “commit message1”'.split()
        str2 = str2.split()     #splitting inputted command

        #::::::::::::::::::::::::::::::::::::::::       9. exit     ::::::::::::::::::::::::::::::::::::::
        if str2[0] == 'exit':
            break

        #::::::::::::::::::::::::::::::::::::::::       2. git commit “commit message”  ::::::::::::::::::
        elif str2[0] == 'git' and str2[1] == 'commit' and str2[2][0] == '"' and str2[-1][-1] == '"':         
            #print(str2[2:])    #string after quotes
            cmtMsg = ' '.join(str(e) for e in str2[2:])
            cmtMsg = cmtMsg[1:-1]
            clist = gitCommit(clist, cmtMsg, commitCnt)
            commitCnt+=1
            
        #::::::::::::::::::::::::::::::::::::::::       3. git show commit    ::::::::::::::::::::::::::::
        elif len(str2) == 3 and str2[0] == 'git' and str2[1] == 'show' and str2[2] == 'commit': 
            gitShowCommit(clist)

        #::::::::::::::::::::::::::::::::::::::::       4. git show all commit
        elif len(str2) == 4 and str2[0] == 'git' and str2[1] == 'show' and str2[2] == 'all'  and str2[3] == 'commit': 
            gitShowAllCommit(clist)

        #::::::::::::::::::::::::::::::::::::::::       5. git delete commit_number     ::::::::::::::::::
        elif len(str2) == 3 and str2[0] == 'git' and str2[1] == 'delete':
            rvNum = str2[2]
            clist = gitRemove(clist, rvNum)

        #::::::::::::::::::::::::::::::::::::::::       6. git jump commit_number       ::::::::::::::::::
        elif len(str2) == 3 and str2[0] == 'git' and str2[1] == 'jump':
            jmpNum = str2[2]
            clist = gitJump(clist, jmpNum)

        #::::::::::::::::::::::::::::::::::::::::       7. git move back    ::::::::::::::::::::::::::::::
        elif len(str2) == 3 and str2[0] == 'git' and str2[1] == 'move' and str2[2] == 'back':
            clist = gitMoveBack(clist)

        #::::::::::::::::::::::::::::::::::::::::       8. git update “New Message”     ::::::::::::::::::
        elif str2[0] == 'git' and str2[1] == 'update' and str2[2][0] == '"' and str2[-1][-1] == '"':    
            newMsg = ' '.join(str(e) for e in str2[2:])
            newMsg = newMsg[1:-1]
            clist = gitUpdate(clist, newMsg)

        #::::::::::::::::::::::::::::::::::::::::       invalid     ::::::::::::::::::::::::::::::::::::::
        else:
            print('Invalid Command')
    #print(clist)
    
 
 
##################################################################################
clist =[]
while True:
    initcmd = input('[INIT]: ').strip()
    if initcmd == 'git init':
        gitCommandString(clist)
        break

    elif initcmd == 'exit':
        break

    else:
        print('Invalid Command')
        
#git init
#git commit "commit message1"
#git commit "commit message2"
#git commit "commit message3"
#git commit "commit message4"
#git commit "commit message5"
#git show all commit
#git show commit
#git jump 2
#git show all commit
#git move back
#git move back
#git show all commit
#git update "New Commit Msg"
#git show all commit
#git commit "commit message6"
#git show all commit
#git delete 4
#git show all commit
#git delete 6
#git show all commit
#git commit "last commit"
#git show commit
#git show all commit
#exit

#exit
