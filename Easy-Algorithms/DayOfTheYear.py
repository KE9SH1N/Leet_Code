class Solution:
    def dayOfYear(self, date: str) -> int:
       year, month, day = map(int, date.split('-'))
       days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
       if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if(month >2):
                total_days = (sum(days_in_month[:month-1]))+1+day
                return total_days
            else:
                total_days = (sum(days_in_month[:month-1]))+day
                return total_days
       else:
            total_days = sum(days_in_month[:month-1])+day
            return total_days

result = Solution().dayOfYear("2012-01-02")
print(result)