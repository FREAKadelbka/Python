def is_monotic(nums):
    MUCHENIE=[]
    MUCHENIE.extend(nums)
    ZOO=[]
    ZOO.extend(nums)
    MECHENIE.sort()
    ZOO.reverse()
    if nums == MUCHENIE:
        return True
    elif MUCHENIE == ZOO:
        return True
    else:
        return False
nums = []
print ("Вводится список, который начинается [ и заканчивается знаком ], без запятых и пробелов")
nums - input("nums = ")
PROGA = nums[1:-1]
PROGA2 = (PROGA.split(","))
i = iter(PROGA)
d = list(iter(lambda: int(next(i)), None))
print (is_monotonic (d))          
          
    
