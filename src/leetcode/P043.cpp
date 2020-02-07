class Solution {
    public: 
        string multiply(string num1, string num2) {
            vector<int> val1 = convertToVector(num1);
            vector<int> val2 = convertToVector(num2);
            vector<int> val3 = multiply(val1, val2);
            return convertToString(val3);
        }
        vector<int> convertToVector(string num) {
            vector<int> result;
            for (vector<int>::size_type i = num.size() - 1; i >= 0; i--) {
                result.push_back(num[i] - '0');
                if (i == 0) break;
            }
            return result;
        }
        string convertToString(vector<int> num) {
            string str = "";
            string::size_type i = num.size() - 1;
            while (num[i] == 0 && i > 0) i--;
            while (i >= 0) {
                str += char(num[i] + '0');
                if (i == 0) break;
                i--;
            }
            return str;
        }
        vector<int> multiply(vector<int> num1, vector<int> num2) {
            vector<int>::size_type i, j;
            int k;

            vector<int> result(num1.size() + num2.size(), 0);
            for (i = 0; i < num1.size(); i++) {
                k = 0;
                for (j = 0; j < num2.size(); j++) {
                    result[i + j] += num1[i] * num2[j] + k;
                    k = result[i + j] / 10;
                    result[i + j] %= 10;
                }
                while (k != 0) {
                    result[i + j] += k;
                    k = result[i + j] / 10;
                    result[i + j] %= 10;
                    j++;
                }
            }
            return result;
        }
};
