int mySqrt(int x) {
    if (x == 0 || x == 1)
        return x;

    for (long long i = 1; i <= x / 2; i++) {
        if (i * i > x) {
            return i - 1;
        }
        else if (i * i == x) {
            return i;
        }
    }

    return x / 2;
}
