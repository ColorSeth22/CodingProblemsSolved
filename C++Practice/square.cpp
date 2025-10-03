# include <string>
# include <sstream>

int square_digits(int num) {
    std::string num_str = std::to_string(num);
    std::string result;
    for (char &c : num_str) {
        int digit = c - '0';
        int squared = digit * digit;
        result += std::to_string(squared);
    }
    return std::stoi(result);
}