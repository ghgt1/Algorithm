function solution(s) {
    var answer = true;
    if(s.length !==4 && s.length!==6)
        return false
    else{
        for(let x of s){
            if(isNaN(Number(x)))
                return false
        }
        return true
    }
}