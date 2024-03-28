def main() :
    expression = input().split('-')
    result = 0

    result += interpretExpression(expression[0])
    for i in expression[1:] :
        result -= interpretExpression(i)

    print(result)

def interpretExpression(expression) :
    temp = expression.split('+')
    result = 0
    for i in temp :
        result += int(i)
    return result

main()