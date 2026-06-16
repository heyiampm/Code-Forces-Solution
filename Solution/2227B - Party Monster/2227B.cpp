#include <iostream>
#include <string>

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);                
    long t;
    std::cin >> t;
    while(t--){
        long n;
        std::cin >> n;
        std::string s;
        std::cin >> s;
        long cnt(0);
        for(char x : s){
            cnt += (x == '(') - (x == ')');
        }
        std::cout << (cnt ? "NO" : "YES") << "\n";
    }
    return 0;
}
