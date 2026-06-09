int nthUglyNumber(int n) {
    int ugly[n];
    ugly[0] = 1;

    int i2 = 0, i3 = 0, i5 = 0;

    for (int i = 1; i < n; i++) {
        int next = ugly[i2] * 2;

        if (ugly[i3] * 3 < next)
            next = ugly[i3] * 3;

        if (ugly[i5] * 5 < next)
            next = ugly[i5] * 5;

        ugly[i] = next;

        if (next == ugly[i2] * 2) i2++;
        if (next == ugly[i3] * 3) i3++;
        if (next == ugly[i5] * 5) i5++;
    }

    return ugly[n - 1];
}
