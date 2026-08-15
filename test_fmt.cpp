#include <iostream>
#include <string>
#include <fmt/core.h>
int main() { std::cout << fmt::format("{:?}", std::string("test")); return 0; }
