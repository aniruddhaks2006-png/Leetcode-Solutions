double findMedianSortedArrays(int* nums1, int num1Size, int* nums2, int num2Size) {

        int a[num1Size+num2Size];
        int min, temp;

        // copy nums1 elements
        for (int i = 0; i < num1Size; i++) {
            a[i] = nums1[i];
        }

        // copy nums2 elements
        for (int i = num1Size; i <num1Size+num2Size; i++) {
            a[i] = nums2[i - num1Size];
        }

        // selection sort
        for (int i = 0; i < num1Size+num2Size; i++) {
            min = i;

            for (int j = i + 1; j < num1Size+num2Size; j++) {
                if (a[min] > a[j]) {
                    min = j;
                }
            }

            temp = a[min];
            a[min] = a[i];
            a[i] = temp;
        }

        // copy back to nums1
       
        
    
    
    if((num1Size+num2Size)%2==0)
    {
        double med=(a[(num1Size+num2Size)/2]+a[(num1Size+num2Size)/2-1])/2.0;
        return med;
    }
    else
    {
        double med=a[(num1Size+num2Size)/2];
        return med;
    }
} 
    

