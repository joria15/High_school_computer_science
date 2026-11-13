#how many repeats
rep = (int(input("how many repeats: ")))
#set variable exchangers
a = 0
b = 0
c = 0
#prints c as starting from 0, b will equal 1 if 0 to add 1 and set c as b to make the result print 1
#then add results to make previous value with current value which is 1 again
#how it works: ask how many times you want to repeat, adds current value with past value
#c is the result, so now set b as the result and set a to b before it was the current result for the previous value
#so b is the current result and is the previous result of what b was which was the past current result
#example: b=2 which was c value and a=1 which was the previous result which is b from before c = a=1 + b=2, c = 3, a = b(2) b = c(3)
#c = a(2) + b(3), c = 5, a=b(3), b=c(5) ect...
for i in range(rep):
    print(c)
    c = a + b
    a = b
    b = c
    if b == 0:
        b = 1
        c = b