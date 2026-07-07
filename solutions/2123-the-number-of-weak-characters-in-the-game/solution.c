int cmp(const void *a, const void *b) {
    const int *x = *(const int**)a;
    const int *y = *(const int**)b;
    if (x[0] != y[0])
        return y[0]-x[0];  
    return x[1]-y[1];       
}
int numberOfWeakCharacters(int** properties, int propertiesSize, int* propertiesColSize) {
    qsort(properties, propertiesSize, sizeof(properties[0]), cmp);
    int maxdef = properties[0][1];
    int count =0;
    for (int i =1;i< propertiesSize;i++) {
        if (properties[i][1]<maxdef)
            count++;
        else
            maxdef =properties[i][1];
    }
    return count;
}
