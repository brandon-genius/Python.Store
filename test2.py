
##### List



def test_1():
    print("basic python list")

    nums = [1,2,3,4,5,4563456,4356456]

    #read
    print(nums[3])
    print(nums[1])

    #add
    nums.append(55)

    #remove by element
    nums.remove(4563456)

    #remove by index
    del nums[0]

    print(nums)


    #loop
    for n in nums:
        print(n)



#call

test_1()