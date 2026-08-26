/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
     const inside=[-1];
    const star=[-1];
    for(let i=0;i<s.length;i++){
        if(s[i]=="("){
            inside.push(i);
        }
        else if(s[i]=="*"){
            star.push(i);
        }
        else{
            if(inside[inside.length-1]==-1 && star[star.length-1]==-1){
                return false;
            }
            else if(inside[inside.length-1]!=-1)
            {
                inside.pop();
            }
            else if(star[star.length-1]!=-1){
                star.pop();
            }
        }
    }
    while(inside[inside.length-1]!=-1 && star[star.length-1]!=-1){
    if(inside.pop()>star.pop()){
        return false;
    }
    }
    if(inside.length>1){
        return false;
    }   
    return true;
};
