function solution(dartResult) {
    var answer = 0;
    let res= [0,0,0]
    let count = 0
    dartResult = [...dartResult]
    dartResult.forEach((x,i)=>{
        console.log(res)
        if(x.charCodeAt()<=57 && x.charCodeAt()>=48){
            res[count] = Number(x)
            count++
            if(dartResult[i-1]==='1' && dartResult[i]==='0'){
                res[count-2] = 10
                count--
//                 foreach는 continue도 못쓰네 ㅋㅋ
            }
        }
        else if(x==='D') res[count-1] = res[count-1]*res[count-1]
        else if(x==='T') res[count-1] = res[count-1]*res[count-1]*res[count-1]
        else if(x==='*'){
            res[count-1] = res[count-1]*2
            if(count>=2) res[count-2] = res[count-2]*2
        }
        else if(x==='#') res[count-1] = res[count-1] * (-1)
    })
    answer = res.reduce((a,b)=>a+b,0)
    return answer;
}