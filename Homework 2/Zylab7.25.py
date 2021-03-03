# Joshua Jaja ID:1543343 Zylab 7.25:

def exactChange(userTotal):
    if (userTotal <= 0):
        return None
    else:
        nDo = userTotal // 100
        userTotal %= 100

        nQ = userTotal // 25
        userTotal %= 25

        NDI = userTotal // 10
        userTotal %= 10

        NN = userTotal // 5
        nP = userTotal % 5

        return (nDo, nQ, NDI, NN, nP)



def main():
    n = int(input())
    r = exactChange(n)
    if(r == None):
        print("no change")
    else:
        nDo = r[0]
        nQ = r[1]
        NDI = r[2]
        NN = r[3]
        nP = r[4]

        if nDo > 0:
            if nDo == 1:
                print('%d dollar' % nDo)
            else:
                print('%d dollars' % nDo)

        if nQ > 0:
            if nQ == 1:
                print('%d quarter' % nQ)
            else:
                print('%d quarters' % nQ)

        if NDI > 0:
            if NDI == 1:
                print('%d dime' % NDI)
            else:
                print('%d dimes' % NDI)

        if NN > 0:
            if NN == 1:
                print('%d nickel' % NN)
            else:
                print('%d nickel' % NN)

        if nP > 0:
            if nP == 1:
                print('%d penny' % nP)
            else:
                print('%d pennies' % nP)

main()

