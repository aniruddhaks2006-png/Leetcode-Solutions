function isValid(s: string): boolean {
    const si:string[]=[];
    si.push("-1")
    for(const i of s){
        if(i=="(" || i=="[" || i=="{"){
            si.push(i);
        }
        else if(i=="}" && si[si.length-1]=="{"){
             si.pop();
        }
        else if(i=="]" && si[si.length-1]=="["){
              si.pop();
        }
        else if(i==")" && si[si.length-1]=="("){
            si.pop();
        }
        else{
            return false;
        }

    }
    if(si.pop()=="-1")
    {
    return true;
    }
    return false;
};
