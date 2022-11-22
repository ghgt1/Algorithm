function solution(lottos, win_nums) {
    var answer = [];
    let hit = 0
    let zero = 0
    lottos.forEach(x=>{
        if(x===0){
            zero++
        }
        else{
            if(win_nums.includes(x)){
                hit++
            }
        }
    })
    answer.push(7-zero-hit)
    answer.push(7-hit)
    answer.forEach((x,i)=>{if(x===7)answer[i]=6})
    return answer;
}