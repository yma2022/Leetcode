class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s) - 1
        s_list = list(s)
        while left < right:
            if s_list[left] in vowels and s_list[right] not in vowels:
                right -= 1
            elif s_list[left] not in vowels and s_list[right] in vowels:
                left += 1
            else:
                if s_list[left] in vowels and s_list[right] in vowels:
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)
                
        