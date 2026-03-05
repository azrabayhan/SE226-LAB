#include <iostream>
#include <string>

int main() {
    std::string name;
    std::string studentID;

    std::cout << "What is your name?\n";
    std::getline(std::cin, name);

    std::cout << "Hello " << name << ".\n";

    std::cout << "What is your Student ID?\n";
    std::getline(std::cin, studentID);

    std::cout << "Your ID is " << studentID << ".\n";

    return 0;
}
#include <iostream>

int main() {
    long totalSeconds;

    std::cout << "Enter total number of seconds:\n";
    std::cin >> totalSeconds;

    int hours = totalSeconds / 3600;
    int minutes = (totalSeconds % 3600) / 60;
    int seconds = totalSeconds % 60;

    std::cout << totalSeconds << " seconds is "
              << hours << " hours, "
              << minutes << " minutes, and "
              << seconds << " seconds.\n";

    return 0;
}
#include <iostream>
#include <cmath>

int main() {
    double x1, y1, x2, y2;

    std::cout << "Enter x1: ";
    std::cin >> x1;
    std::cout << "Enter y1: ";
    std::cin >> y1;
    std::cout << "Enter x2: ";
    std::cin >> x2;
    std::cout << "Enter y2: ";
    std::cin >> y2;

    double distance = std::sqrt(std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2));

    std::cout << "Distance between points: " << distance << "\n";

    return 0;
}
#include <iostream>

int main() {
    std::cout << "*******\n"
                 " *****\n"
                 "  ***\n"
                 "   *\n";
    return 0;
}