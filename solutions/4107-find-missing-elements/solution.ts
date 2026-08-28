function findMissingElements(nums: number[]): number[] {
    nums.sort((a,b)=>a-b);
    let x=nums[0];
    let i=0
    let a:number[]=[];
    while(i<nums.length){
        if(x!==nums[i]){
            a.push(x);
            x+=1;
        }
        else{
            x+=1;
            i+=1;
        }
        
    }
    return a
};
