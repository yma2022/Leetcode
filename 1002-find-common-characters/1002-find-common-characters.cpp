class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<string> result;
        if (words.size() == 0) return result;
        int record[26] = {0};
        for (int i = 0; i < words[0].size(); i++){
            record[words[0][i] - 'a']++;
        }
        
        int recordOther[26] = {0};
        for (int i = 1; i < words.size(); i++){
            memset(recordOther, 0, 26 * sizeof(int));
            for (int j = 0; j < words[i].size(); j++){
                recordOther[words[i][j] - 'a']++;
            }
            for (int k = 0; k < 26; k++){
                record[k] = min(record[k], recordOther[k]);
            }
        }
        
        for (int i = 0; i < 26; i++){
            while (record[i] != 0){
                string s(1, i + 'a');
                result.push_back(s);
                record[i]--;
            }
        }
        return result;
    }
};