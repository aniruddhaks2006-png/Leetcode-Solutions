char* trafficSignal(int timer) {
    
    char* s=(char*)malloc(10);
    if(timer==0)
        strcpy(s,"Green");
    
    else if(timer==30)
        strcpy(s,"Orange");
    else if(timer>30 && timer<=90)
        strcpy(s,"Red");
    else
        strcpy(s,"Invalid");
    return s;
}
