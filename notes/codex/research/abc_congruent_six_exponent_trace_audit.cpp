// Exhaust the integers p = 24k +/- 1 directly, without a CRT wheel.
// Feed the PARI-generated local tables on stdin using abc_congruent_six_exponent_trace_audit.py.
#include <iostream>
#include <string>
#include <vector>

struct Test {
    int auxiliary, torus_order;
    std::string squares, forced;
};

bool prime(int candidate) {
    for (int d = 2; d <= candidate / d; ++d) {
        if (candidate % d == 0) return false;
    }
    return candidate >= 2;
}

int main() {
    std::vector<Test> tests;
    Test row;
    while (std::cin >> row.auxiliary >> row.torus_order >> row.squares >> row.forced) {
        if (static_cast<int>(row.squares.size()) != row.auxiliary ||
            static_cast<int>(row.forced.size()) != row.torus_order) return 1;
        tests.push_back(row);
    }
    if (tests.size() != 52) return 1;
    constexpr int limit = 1000000000;
    for (int k = 1; 24*k-1 <= limit; ++k) {
        for (int sign : {1,-1}) {
            int p = 24*k + sign;
            if (p < 27431 || p > limit) continue;
            bool possible = true;
            for (const auto &test : tests) {
                int residue = p % test.auxiliary;
                if (sign < 0 && residue) residue = test.auxiliary - residue;
                if (test.squares[residue] == '0' && test.forced[p % test.torus_order] == '1') {
                    possible = false;
                    break;
                }
            }
            if (possible && prime(p)) std::cout << p << '\n';
        }
    }
}
