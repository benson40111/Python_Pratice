from fractions import Fraction

martix = []

def output():
    for i,j in enumerate(martix):
        if (int(j.count(0)) == column_size + 1):
            flag = 0
        elif (int(j.count(0)) == column_size):
            flag = 1
        else:
            flag = 2
    if (flag == 0):
        print ('N')
    elif (flag == 1):
        print ('0')
    else:
        print ('1')
    for i in range(0, column_size):
        print ('x' + str(i + 1) + ' = ' + str(martix[i][-1]))
        print (str(i + 1) + "Column = " + " ".join(str(x) for x in martix[i]))

try:
    column_size = int(input("How many row? \n"))
    for i in range(0, column_size):
        column_input = input("")
        column = column_input.split()
        column = [int(x) for x in column]
        martix.append(column)

    for i in range(0, column_size):
        for j in range(0, column_size + 1):
            martix[i][j] = Fraction(martix[i][j])

    for i in range(0, column_size):
        first = martix[i][i]
        for j in range(0, column_size + 1):
            martix[i][j] /= first

    for x in range(column_size - 1):
        for i in range(x, column_size):
            if (i != column_size - 1):
                b = martix[i + 1][x] * (-1)
                for j in range(0, column_size + 1):
                    martix[i + 1][j] = martix[x][j] * b + martix[i + 1][j]

        for i in range(0, column_size):
            a = martix[i][i]
            for j in range(0, column_size + 1):
                if (a != 0):
                    martix[i][j] /= a
                else:
                    martix[i][j] = martix[i][j]

    martix.reverse()
    for i in martix:
        i.reverse()

    for x in range(column_size - 1):
        for i in range(x, column_size):
            if (i != column_size - 1):
                c = martix[i + 1][x + 1] * (-1)
                for j in range(0, column_size + 1):
                    martix[i + 1][j] = martix[x][j] * c + martix[i + 1][j]

    martix.reverse()
    for i in martix:
        i.reverse()
    output()

except Exception:
    print ("輸入有錯誤！")
