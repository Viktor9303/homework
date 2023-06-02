def string_matrix(string):
    res = [[]]
    lst = []
    for index in range(len(string)):
        elem = string[index]
        #2 5
        #print(index)
        if (index + 1) % 3 == 0 :
            lst.append(elem)
            res.append(lst)
        #1 4
        elif (index + 2) % 3 == 0:
            lst.append(elem)
        #3 6
        else:
            lst = []
            lst.append(elem)

    return res[1:]

def get_pos_black(string):
    matrix = [[]]
    lst = []
    for index,el in enumerate(string):
        if el == "*":
           lst.append(index)
           print(index)
        #8 17
        if (index+1) %9 == 0:
            print("index")
            matrix.append(lst)
            lst = []

    return matrix[1:]
print("*****")
print(get_pos_black('*..**.*..****....*'))
print("*****")
def turn_white(matrix,pos_black):
    rules = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,6,4],4:[1,3,5,7],5:[4,2,8],6:[3,7],7:[6,8,4]}

lines_number = input("")
res = ""
for line in range(int(lines_number)*3):
    current_line = "".join(input())
    res += str(current_line)
print(string_matrix(res))
print(res)


