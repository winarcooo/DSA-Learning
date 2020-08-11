def binary(numbers, target):
    first = 0
    last = len(numbers)-1
    found = False

    while(first <= last and not found):
        mid = (first + last)//2
        if numbers[mid] == target:
            found = True
        else:
            if target < numbers[mid]:
                last = mid-1
            else:
                first = mid+1
    
    return found