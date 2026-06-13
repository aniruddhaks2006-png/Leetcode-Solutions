bool isprime(int n) {
    if (n < 2)
        return false;
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}
int countPrimeSetBits(int left, int right) {
    int sum = 0;
    for (int i = left; i <= right; i++) {
        int count = 0;
        int j = i;
        while (j != 0) {
            if (j % 2 == 1)
                count++;
            j /= 2;
        }
        if (isprime(count))
            sum++;
    }
    return sum;
}
