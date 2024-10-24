seqLen = int(input("Please enter how many integers of the Recaman Sequence you would like to see: "))
currentNum = 0
nums = []
for k in range(seqLen):
    if currentNum - k > 0:
        if currentNum - k not in nums:
         currentNum = currentNum - k
         nums.append(currentNum)
        else:
            currentNum = currentNum + k
    else:
        currentNum = currentNum + k
        if currentNum not in nums:
            nums.append(currentNum)
    print(currentNum)

    

    
