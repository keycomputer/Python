##https://www.cbseguess.com/uploads_papers/QP_083_computer_science_new.pdf
##Q 37 a
##def POP_PUSH(LPop, LPush, N):
##    if N > len(LPop):
##        print("Pop not possible")
##    else:
##        for i in range(N):
##            elem = LPop.pop()
##            LPush.append(elem)
##
##LPop = [10,15,20,30]
##LPush = []
##POP_PUSH(LPop, LPush, 2)
##print(LPop)
##print(LPush)

##Q37 b
##def POPSTACK(L) :
##    if len(L) == 0:
##        return None
##    else:
##        elem = L.pop()
##        return elem
##
##L1 = [1,2,3,4,5]
##print(POPSTACK(L1))
##print(POPSTACK(L1))
##print(POPSTACK(L1))

##https://meritbatch.com/cbse-sample-papers-for-class-12-computer-science-set-10/
##Q 30

##def push(status, list1):
##    for i in list1:
##        if i[2].lower() == 'goa':
##           status.append(i)
##
##def pop(status):
##    if len(status) ==0 :
##        print("Empty Stack ")
##    else:
##        print(status.pop())
##
##
##L1 = [["Gurdas", "99999999999","Goa"],["Julee", "8888888888","Mumbai"],
##      ["Murugan","77777777777","Cochin"],
##["Ashmit", "1010101010","Goa"]]
##status = [] 
##push(status , L1)
##pop(status)
##pop(status)







            
