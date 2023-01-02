function solution(fees, records) {
    var answer = [];
//     일단 모든 시간들을 분으로 해야겠다
    function calMin(time){
        let tmpHour = Number(time.slice(0,2))
        let tmpMin = Number(time.slice(3,5))
        return (tmpHour*60 + tmpMin)
    }
    let map = {}
    for(let x of records){
        let l1 = x.split(" ")
        if(map[l1[1]]){
            map[l1[1]].push(calMin(l1[0]))
        }
        else{
            map[l1[1]]= [calMin(l1[0])]
        }
    }
    for(let x in map){
        if(map[x].length %2 !==0){
            map[x].push(1439)
        }
    }
    for(let x in map){
        let total = 0
        map[x].forEach((item,idx)=>{
            if(idx%2===1){
                total+=(map[x][idx] - map[x][idx-1])
            }
        })
        map[x] = total
    }
    for(let x in map){
        let price = 0
        if(map[x]<=fees[0]){
            map[x] = fees[1]
        }
        else{
            map[x] = fees[1] + (Math.ceil((map[x]-fees[0])/fees[2])*fees[3])
        }
    }
    let l1 = []
    for(let x in map){
        l1.push([x,map[x]])
    }
    l1.sort((a,b)=>a[0]-b[0])
    l1.forEach(item=>{
        answer.push(item[1])
    })
    return answer;
}