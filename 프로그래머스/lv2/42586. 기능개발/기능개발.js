function solution(progresses, speeds) {
    var answer = [];
//     일단 날짜 계산을 다 해야함
    let date = []
    for(let i=0;i<progresses.length;i++){
        if((100-progresses[i])%speeds[i] !==0){
            date.push(parseInt((100-progresses[i])/speeds[i])+1)
        }
        else{
            date.push(parseInt((100-progresses[i])/speeds[i]))
        }
    }
    let stack = []
    date.forEach(item=>{
        if(stack.length ===0) stack.push(item)
        else{
            if(stack[0] < item){
                answer.push(stack.length)
                stack = []
                stack.push(item)
            }
            else{
                stack.push(item)
            }
        }
    })
    if(stack.length !==0){
        answer.push(stack.length)
    }
    return answer;
}