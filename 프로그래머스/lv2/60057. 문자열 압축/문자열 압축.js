function solution(s) {
    var answer = 0;
    let result = []
//     매개변수 서치? 아 근데, 일방향이 아닌데....
//     그냥 완탐?
    for(let i=1;i<=s.length;i++){
        let tmp = ""
        let tmp_res = []
        let index = -1
        for(let j=0;j<=s.length;j+=i){
            let tmp_slice = s.slice(j,j+i)
            if(tmp_slice){
                if(tmp === tmp_slice){
                    tmp_res[index][0]+=1
                }
                else{
                    index++
                    tmp_res.push([1,tmp_slice])
                    tmp = tmp_slice
                }
            }
        }
        let count = 0
        for(let x of tmp_res){
            [num,str] = x
            if(num!==1){
                count+=(str.length+String(num).length)
            }
            else{
                count+=str.length
            }
        }
        result.push(count)
    }
    answer = Math.min(...result)
    
    return answer;
}