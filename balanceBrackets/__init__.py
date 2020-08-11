def balanceBrackets(brackets):
    if len(brackets) == 0: return -1

    brackets = list(brackets)

    stack = []
    for bracket in brackets:
        if isOpen(bracket):
            stack.append(bracket)
        else:
            if isPair(stack[-1], bracket):
                stack.pop()
            else:
                return "unbalance"
    
    if len(stack) == 0:
        return "balance"
    
    return "unbalance"

def isOpen(bracket):
    openBracket = ["[","(","{"]
    if bracket in openBracket:
        return True
    return False

def isPair(x, y):
    if x == "{" and y == "}":
        return True
    elif x == "[" and y == "]":
        return True
    elif x == "(" and y == ")":
        return True
    else:
        return False


if __name__ == "__main__":
    brackets = "(){}{"
    balanceBrackets(brackets)