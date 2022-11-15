function solution(N, stages) {
    var answer = [];
    let l1 =Array(N+1).fill(0)
    let l2 = Array(N+1).fill(0)
//     l1은 성공
    for(let x of stages){
        for(let i=1;i<x;i++){
            l1[i]++
        }
    }
//     l2는 도달
    for(let x of stages){
        for(let i=1;i<=x;i++){
            if(!isNaN(l2[i]))l2[i]++
        }
    }
    l1=l1.map((x,i)=>{
        return l2[i]-x
    })
    let l3=[]
    for(let i=1;i<N+1;i++){
        l3.push([l1[i]/l2[i],i])
    }
    l3.sort((a,b)=>{
        return a[1]-b[1]
    })
    l3.sort((a,b)=>{
        return b[0]-a[0]
    })
    l3.forEach(x=>{
      answer.push(x[1])  
    })
    return answer;
}