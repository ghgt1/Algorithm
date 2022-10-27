function solution(cacheSize, cities) {
    var answer = 0;
    let cache = []
//     cache에 넣으면서 hit miss따진다. 꽉찻을때부터는 교체가능
    for(let i=0;i<cities.length;i++){
        cities[i] = cities[i].toLowerCase()
    }
    for(let x of cities){
        if(cache.length<cacheSize){
            if(!cache.includes(x)){
            cache.push(x)
                answer+=5}
            else{
                cache.splice(cache.indexOf(x),1)
                cache.push(x)
                answer+=1
            }
        }
        else{
            if(!cache.includes(x)){
                if(cacheSize!==0){
                answer+=5
                cache.shift()
                cache.push(x)}
                else{
                    answer+=5
                }
            }
            else{
                cache.splice(cache.indexOf(x),1)
                cache.push(x)
                answer+=1
            }
        }
    }
    return answer;
}