class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0,j=0;
        string st;
        while(i<word1.size() && j<word2.size()){
            st.push_back(word1[i]);
            st.push_back(word2[j]);
            i++;
            j++;
        }
        while(i<word1.size()){
            st.push_back(word1[i]);
            i++;
        }
         while(j<word2.size()){
            st.push_back(word2[j]);
            j++;
        }
        return st;
    }
};
