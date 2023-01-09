const getCombinations = (array, selectNumber) => {
    const results = [];
    if(selectNumber === 1){
        return array.map((element) => [element]);
    }
    array.forEach((fixed, index, origin) => {
        const rest = origin.slice(index+1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((combination) => [fixed, ...combination]);
        results.push(...attached);
    });
    return results;
}

function solution(orders, course) {
    var answer = [];
    let map = {}
    for(let x of orders){
        for(let i=2;i<=x.length;i++){
            let res = getCombinations([...x],i)
            for(let comb of res){
                comb.sort()
                let tmp = comb.join('')
                if(map[tmp]){map[tmp]+=1}
                else{map[tmp] = 1}
            }
        }
    }
    console.log(map)
    for(let x of course){
        let filtered = []
        let max = 0
        for(let key in map){
            if(key.length === x){
                if(map[key] === 1) continue
                if(map[key]>max){
                    filtered = [key]
                    max = map[key]
                } 
                else if (map[key]===max){
                    filtered.push(key)
                }
            }
        }
        answer.push(...filtered)
    }
    // console.log(answer)

//     조합....
//     2개~order의 length까지 모든 조합을 map에 저장
    
    return answer.sort();
}