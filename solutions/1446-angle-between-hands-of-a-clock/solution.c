double angleClock(int hour, int minutes) {
    double minit=6.0*minutes;
    double hrs=30.0*hour+0.5*minutes;
    double x=fabs(minit-hrs);
    return (x<360.0-x)?x:360.0-x;
    
}
