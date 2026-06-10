int finalValueAfterOperations(char** operations, int operationsSize) {
    int x=0;
    for(int i =0;i<operationsSize;i++){
        if(strcmp(operations[i],"++X")==0){
            ++x;
        }
        else if(strcmp(operations[i],"X++")==0){
            x++;
        }
       else if(strcmp(operations[i],"--X")==0){
            --x;
        }
    else if(strcmp(operations[i],"X--")==0){
            x--;
        }
        else
            continue;
    }
    return x;
}
