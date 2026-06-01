char* categorizeBox(int length, int width, int height, int mass) {
    int x=0,y=0;
    long long vol=(long long)length *width*height;
    if((vol)>=1e9)
        x=1;
    
    if(length>=1e4 || width>=1e4 || height>=1e4)
        x=1;
    if(mass>=100)
        y=1;
    if(x<1 && y<1)
        return "Neither";
    if(x>0 && y>0)
        return "Both";
    if(x>0)
        return "Bulky";
    else
        return "Heavy";
        
}
