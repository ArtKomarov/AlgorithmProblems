#include <iostream>

// Algorithm explanation by example:
// 5^11 = 5^(8+2+1) = 5^(2^0) * 5^(2^1) * 5^(2^3) = res_0 * res_1 * res_3 where (res_0 eq x), (res_1 eq 1 time x *= x), (res_3 eq 3 times x *= x)
double myPow(double x, long int n) {
    if(n == 0) {
        return 1;
    }
    if(x == 0) {
        return 0;
    }

    double result = 1;
    bool xNegative = x < 0;
    if (xNegative) {
        x = -x;
    }
    bool nNegative = n < 0;
    if (nNegative) {
        n = -n;
    }
    unsigned long nBits = static_cast<unsigned long>(n);

    unsigned long powerOfPow = 1;
    while(nBits > 0) {
        unsigned long lastBit = nBits & 1;
        nBits = nBits >> 1;
        
        if (lastBit == 1) {
            double resultI = x;
            for(unsigned long i = 1; i < powerOfPow; ++i) {
                resultI *= resultI;
            }
            result *= resultI;
        }
        powerOfPow++;
    }

    if (xNegative && n % 2 == 1) {
        result = -result;
    }
    if (nNegative) {
        return 1 / result;
    }
    return result;
}

int main() {
    std::cout << myPow(-1.2, -2) << std::endl;
    return 0;
}