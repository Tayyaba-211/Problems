class Solution {
public:
    bool isValid(const string& s) {
        stack<char> st;
        unordered_map<char, char>mapping = {{')', '('}, {']','['},{'}','{'}};

        for(char c : s){
            if(c == '(' || c == '[' || c == '{'){
                st.push(c);
            }else if(c == ')' || c == ']'|| c=='}'){
                if(st.empty() || st.top() != mapping[c]){
                    return false;
                }
                st.pop();
            }
        }
        return st.empty();
        
    }
};
// int main(){
//     string inputexp;
//     getline(cin, inputexp);

//     Solution sol;
//     if(sol.isValid(inputexp)){
//         cout<<"true"<<endl;
//     }else{
//         cout<<"false"<<endl;
//     }
//     return 0;
// }