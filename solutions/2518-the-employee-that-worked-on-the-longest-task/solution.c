int hardestWorker(int n, int** logs, int logsSize, int* logsColSize) {
    int prev = 0;
    int maxi = 0;
    int ans = 0;
    for (int i = 0; i < logsSize; i++) {
        int current = logs[i][1];
        int duration = current - prev;
        if (duration > maxi || (duration == maxi && logs[i][0] < ans)) {
            maxi = duration;
            ans = logs[i][0];
        }
        prev = current;
    }
    return ans;
}
