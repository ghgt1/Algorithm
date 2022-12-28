function solution(numbers, target) {
    var answer = 0;
//     + - 다 달아보면 될듯
//     BFS 느낌으로
    
    
    function DFS(index,sum){
        if(index === numbers.length){
//             끝에 다다르면 확인한다
            if(sum===target){
                answer++
            }
            return
        }
        DFS(index+1, sum-numbers[index])
        DFS(index+1,sum+numbers[index])
    }
    
    DFS(0,0)
    return answer;
}