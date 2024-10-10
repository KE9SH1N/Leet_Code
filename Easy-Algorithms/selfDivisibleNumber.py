class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result_list=[]
        for number in range(left, right+1):
            if(len(str(number)) == 1):
                if(number%number ==0):
                    result_list.append(number)
            else:
                digits = [int(digits) for digits in str(number)]
                divisible = True
                for digit in digits:
                    if(digit==0):
                        divisible= False
                        break
                    if(number%digit !=0):
                        divisible = False
                        break
                
                if(divisible):
                   result_list.append(number)
        return result_list
    
print(Solution().selfDividingNumbers(1,22))





# left = 1
# right = 22
# result_list =[]

# for number in range(left, right):
#     if(len(str(number)) ==1):
#         if(number%number ==0):
#             result_list.append(number)
    
#     else:
#         d = [int(d) for d in str(number)]
#         divisible_by_all_digits = True
#         for m in d:
#             if m == 0:
#                 continue
#             if(number%m !=0):
#                 divisible_by_all_digits = False
#                 break
#         if(divisible_by_all_digits):
#             result_list.append(number)
        
        

# print(result_list)