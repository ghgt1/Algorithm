function solution(str1, str2) {
    var answer = 0;
//     우선 두개를 잘라내야함
    let l1 = {}
    let l2 = {}
    for(let i =0;i<str1.length-1;i++){
        if(str1[i].toUpperCase().charCodeAt()>=65 && str1[i].toUpperCase().charCodeAt()<=90&&str1[i+1].toUpperCase().charCodeAt()>=65 && str1[i+1].toUpperCase().charCodeAt()<=90){
            if(l1[str1.substring(i,i+2).toUpperCase()]){
                l1[str1.substring(i,i+2).toUpperCase()]++
            }
            else{
                l1[str1.substring(i,i+2).toUpperCase()] = 1
            }
        }
    }
    for(let i =0;i<str2.length-1;i++){
        if(str2[i].toUpperCase().charCodeAt()>=65 && str2[i].toUpperCase().charCodeAt()<=90&&str2[i+1].toUpperCase().charCodeAt()>=65 && str2[i+1].toUpperCase().charCodeAt()<=90){
            if(l2[str2.substring(i,i+2).toUpperCase()]){
                l2[str2.substring(i,i+2).toUpperCase()]++
            }
            else{
                l2[str2.substring(i,i+2).toUpperCase()] = 1
            }
        }
    }
    let intersection = 0
    let union = 0
    for(let key in l1){
        if(l2[key]){
            intersection += Math.min(l1[key],l2[key])
            union += Math.max(l1[key],l2[key])
        }
        else{
            union+=l1[key]
        }
    }
    for(let key in l2){
        if(!l1[key]){
            union+=l2[key]
        }

    }
    // console.log(l1,l2)
    // console.log(intersection,union)
    answer =(Math.floor((intersection/union)*65536))
    if(Object.entries(l1).length ===0 && Object.entries(l2).length ===0) answer = 65536
    return answer;
} 