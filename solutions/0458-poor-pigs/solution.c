int poorPigs(int buckets, int md, int mt) {
    int rounds=mt/md;
    int pig=0;
     while (pow(rounds+1,pig)<buckets){
        pig++;
     }
     return pig;
}
