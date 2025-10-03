#include <string>
#include <algorithm>
#include <cctype>

bool sp_eng(const std::string& sentence) {
    std::string lowerSentence = sentence;
    std::transform(lowerSentence.begin(), lowerSentence.end(), lowerSentence.begin(),
                   [](unsigned char c){ return std::tolower(c); });
    return lowerSentence.find("english") != std::string::npos;
}

