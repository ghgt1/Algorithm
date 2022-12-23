function solution(clothes) {
    var answer = 1;
    let map ={}
    let l1 = []
    for(let x of clothes){
        if(map[x[1]]){
            map[x[1]].push(x[0])
        }
        else{
            map[x[1]] = [x[0]]
        }
    }
    for(let value in map){
        l1.push(map[value].length+1)
    }
    l1.forEach(item=>{
        answer*=item
    })
    return answer-1;
}