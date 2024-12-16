def pingPong(a,state):
    run = 0
    runMax = len(a)
    increment = 0
    while run < runMax:
        a.insert(run+(increment+1), "Pong!") #0#1+2#2+3 #2#3#4
        increment=increment+1
        run+=1
    if state == False:
        a.pop()
    print(a)

#Example 1
pingPong(["Ping!"], True)

#Example 2
pingPong(["Ping!", "Ping!"], False)

#Example 3
pingPong(["Ping!", "Ping!", "Ping!"], True)