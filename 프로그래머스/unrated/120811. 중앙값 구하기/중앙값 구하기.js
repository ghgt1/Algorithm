function solution(array) {
    var answer = 0;
    array.sort(function compare(a,b){
        return a-b;
    });
    console.log(array)
    answer = array[(array.length-1)/2];
    return answer;
}