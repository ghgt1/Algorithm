function solution(board, moves) {
    var answer = 0;
//     딱봐도 스택
    let stack = [];
//     moves는 각 배열들의 moves-1인덱스를 보면됨
//     재배치해보자 
    let box = []
    let tmp=[]
    for(let i=0;i<board.length;i++){
        tmp=[]
        for(let j=0;j<board.length;j++){
            if(board[j][i]!==0) tmp.push(board[j][i])
        }
        box.push(tmp)
    }
    console.log(box)
    for(let x of moves){
        if(box[x-1].length !==0){
            if(box[x-1][0] === stack.at(-1)){
                answer+=2
                stack.pop()
                box[x-1].shift()
            }
            else stack.push(box[x-1].shift())
        }
    }
    return answer;
}