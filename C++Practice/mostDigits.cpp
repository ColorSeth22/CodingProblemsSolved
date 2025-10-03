#include <vector>
#include <string>

int findLongest(const std::vector<int>& numbers) {
  int maxDigits = 0;
  int maxNumber = 0;
  for (int number : numbers) {
    std::string str_number = std::to_string(number);
    if (str_number.length() > maxDigits) {
      maxDigits = str_number.length();
      maxNumber = number;
    }
  }

    return maxNumber;
}