function solution(A,B){
    var answer = 0;
//     이론상 큰수는 작은수랑 매치되게하면 됨
//     sort하자
    A.sort((a,b)=>a-b)
    B.sort((a,b)=>a-b).reverse()
    for(let i=0;i<A.length;i++){
        answer+=A[i]*B[i]
    }
    return answer;
}