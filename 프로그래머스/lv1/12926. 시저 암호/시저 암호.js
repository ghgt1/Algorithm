function solution(s, n) {
    var answer = '';
    [...s].forEach((x,i)=>{
        if(s.charCodeAt(i)>=65 && s.charCodeAt(i)<=90){
            if(s.charCodeAt(i)+n>90) answer+=String.fromCharCode(s.charCodeAt(i)+n-26)
            else answer+=String.fromCharCode(s.charCodeAt(i)+n)
        }
        else if(s.charCodeAt(i)>=97 && s.charCodeAt(i)<=122)
            if(s.charCodeAt(i)+n>122) answer+=String.fromCharCode(s.charCodeAt(i)+n-26)
            else answer+=String.fromCharCode(s.charCodeAt(i)+n)
        else answer+=' '
    })
    return answer;
}