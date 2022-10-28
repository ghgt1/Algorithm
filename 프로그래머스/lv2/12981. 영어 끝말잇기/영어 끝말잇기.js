function solution(n, words) {
    var answer = [];
    let count = 0
    let records=[]
    let compare=words[0][0]
    while(true){
        for(let index=0;index<n;index++){
            if(n*count+index == words.length)
                return [0,0]
            if(records.includes(words[n*count+index])){
                return [index+1,count+1]
            }
            else{
                if(compare!==words[n*count+index][0]){
                    return [index+1,count+1]
                }
                else{
                    records.push(words[n*count+index])
                    compare = words[n*count+index].slice(-1)
                }
            }
        }
        count++
    }

    return [0,0];
}