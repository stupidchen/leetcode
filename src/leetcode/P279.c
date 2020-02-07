int numSquares(int n) {
    int f[n + 1];
    f[0] = 0;
    for (int i = 1; i <= n; i++) {
        f[i] = f[i - 1] + 1;
        for (int j = 2; j * j <= i; j++) {
            f[i] = f[i] > f[i - j * j] + 1 ? f[i - j * j] + 1 : f[i];
        }
    }
    return f[n];
}