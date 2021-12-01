//
// Created by glebg on 01.12.2021.
//
#include <iostream>
#include <fstream>
#include <vector>


/*
int main(){
    std::ifstream infile("in.txt");
    int measurement{};
    int prev_measurment{-1};
    int count{};
    int i{};
    while (infile >> measurement){
        ++i;
        if (prev_measurment == -1){
            count = -1;
        }
        std::cout << measurement << " " << prev_measurment << "\n";
        if (measurement > prev_measurment){
            ++count;
        }
        prev_measurment = measurement;
    }
    std::cout << i << "\n";
    std::cout << count;
    return 0;
}
*/

int main(){
    std::ifstream file("in.txt");
    std::vector<int> measurements{};
    int measurement;
    int count{};
    int index{0};
    while (file >> measurement){
        measurements.push_back(measurement);
        if (measurements.size() < 4){
            continue;
        }
        if (measurements[index] < measurements[index + 3]){
            ++count;
        }
        ++index;
    }
    std::cout << count;
    return 0;
}