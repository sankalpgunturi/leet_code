# My Code

from hashlib import new
class Solution:
    def romanToInt(self, s: str) -> int:

        my_list = list(s)
        new_list = []


        for i in range(len(my_list)):
            if my_list[i] == "M":
                new_list.append(1000)
            elif my_list[i] == "D":
                new_list.append(500)
            elif my_list[i] == "C":
                new_list.append(100)
            elif my_list[i] == "L":
                new_list.append(50)
            elif my_list[i] == "X":
                new_list.append(10)
            elif my_list[i] == "V":
                new_list.append(5)      
            elif my_list[i] == "I":
                new_list.append(1)   

        sum = 0
        i = 0
        while i < len(new_list):
            if (((i + 1) < len(new_list)) and (new_list[i + 1] > new_list[i])):
                sum = sum + (new_list[i + 1] - new_list[i])
                i = i + 2
            elif (((i + 1) < len(new_list))) and ((new_list[i + 1] <= new_list[i])):
                sum = sum + new_list[i]
                i = i + 1
            elif (i == (len(new_list) - 1) and (new_list[i] <= new_list[i - 1])):
                sum = sum + new_list[i]
                break
                
        return sum
