function solution(msg) {
    var answer = [];
//     사전 생성
    let dic = {}
    for(let i=0;i<26;i++){
        dic[String.fromCharCode(i+65)] = i+1
    }
    let index = 27
    let pointer = 0
    let tmp = ""
    while(pointer !== msg.length){
//         가장긴 일치를 찾아야함
        tmp += msg[pointer]
        while(dic[tmp]){
            pointer++
            let tmp2 = tmp
            tmp+=msg[pointer]
            if(dic[tmp]){continue}
            else{answer.push(dic[tmp2])
                dic[tmp] = index++
                tmp = ""}
        }
    }
    
    return answer;
}