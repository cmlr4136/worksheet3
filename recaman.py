seqLen = int(input("Please enter how many integers of the Recaman Sequence you would like to see: "))
currentNum = 0
nums = []
finalSeq = []
for k in range(seqLen):
    if currentNum - k > 0:
        if currentNum - k not in nums:
         currentNum = currentNum - k
         nums.append(currentNum)
         finalSeq.append(currentNum)
        else:
            currentNum = currentNum + k
            if currentNum not in nums:
                nums.append(currentNum)
                finalSeq.append(currentNum)
            else:
                finalSeq.append(currentNum)
    else:
        currentNum = currentNum + k
        if currentNum not in nums:
            nums.append(currentNum)
            finalSeq.append(currentNum)
        else:
            finalSeq.append(currentNum)
print(finalSeq)
print(nums)

    

    
