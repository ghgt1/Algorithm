function solution(participant, completion) {
    var answer = '';
    let map = {}
    for(let x of participant){
        map[x] = (map[x]||0)+1
    }
    for(let x of completion){
        map[x] = map[x] - 1
    }
    for(let x in map){
        if(map[x]!==0)
            return x
    }
    return answer;
}