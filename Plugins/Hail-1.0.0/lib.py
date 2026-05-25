"写了几百年的冰雹算法"
def HailCal(i:float):
    Steps, Value = 0, [i]
    while i != 1:
        i = (i//2) if (i%2)==0 else (i*3+1)
        Value.append((i))
        Steps += 1
    return {"Steps":Steps, "Value":Value, 'IsCyclic':False}

def HailCalN(i:float):
    Steps, Value, IsCyclic = 0, [i], False
    while i != -1:
        i = (i//2) if (i%2)==0 else (i*3+1)
        if i in Value:
            IsCyclic = True
            break
        Value.append((i))
        Steps += 1
    return {"Steps":Steps, "Value":Value, "IsCyclic":IsCyclic}