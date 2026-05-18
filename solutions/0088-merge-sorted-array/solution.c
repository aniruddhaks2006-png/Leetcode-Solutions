void merge(int* nums1, int nums1Size, int m,
           int* nums2, int nums2Size, int n) {

    if (m == 0) {
        for (int i = 0; i < n; i++) {
            nums1[i] = nums2[i];
        }
        return;
    }
    else if (n == 0) {
        return;
    }
    else {
        int a[m + n];
        int min, temp;

        // copy nums1 elements
        for (int i = 0; i < m; i++) {
            a[i] = nums1[i];
        }

        // copy nums2 elements
        for (int i = m; i < m + n; i++) {
            a[i] = nums2[i - m];
        }

        // selection sort
        for (int i = 0; i < m + n; i++) {
            min = i;

            for (int j = i + 1; j < m + n; j++) {
                if (a[min] > a[j]) {
                    min = j;
                }
            }

            temp = a[min];
            a[min] = a[i];
            a[i] = temp;
        }

        // copy back to nums1
        for (int i = 0; i < m + n; i++) {
            nums1[i] = a[i];
        }
    }
}
