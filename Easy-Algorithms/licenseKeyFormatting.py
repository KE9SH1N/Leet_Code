class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new = s.replace("-", "").upper()
        first_group_len = len(new) % k
        result = []
        if first_group_len:
            result.append(new[:first_group_len])
        for i in range(first_group_len, len(new), k):
            result.append(new[i:i + k])
        return '-'.join(result)
result = Solution().licenseKeyFormatting("5F3Z-2e-9-w",5)
print(result)