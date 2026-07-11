
int numberOfArrays(int* difference, int differenceSize, int lower, int upper) {
    long long minpref=0;
    long long maxpref=0;
    long long pref=0;
    for(int i=0;i<differenceSize;i++){
        pref+=difference[i];
        minpref=pref<minpref?pref:minpref;
        maxpref=pref>maxpref?pref:maxpref;
    }
        long long x=(long long)(upper-maxpref)-(lower-minpref)+1;
        return 0>x?0:(int)x;
    }

