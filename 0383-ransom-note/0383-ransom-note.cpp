class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int record[26] = {0};
        for (char ch: magazine){
            record[ch - 'a']++;
        }
        for (char ch: ransomNote){
            record[ch - 'a']--;
        }
        for (int i = 0; i < 26; i++){
            if (record[i] < 0){
                return false;
            }
        }
        return true;
    }
};