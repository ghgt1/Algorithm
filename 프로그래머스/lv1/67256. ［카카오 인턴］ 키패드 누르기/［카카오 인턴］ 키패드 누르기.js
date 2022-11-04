function solution(numbers, hand) {
    var answer = '';
//     항상 거리계산을 해두어야함
    let left = [3,0]
    let right = [3,2]
    hand = hand[0].toUpperCase()
    calcDistance = function(arr1,arr2){
        return (Math.abs(arr2[0]-arr1[0]) + Math.abs(arr2[1] - arr1[1]))
    }
    for(let x of numbers){
        if(x === 1 || x === 4 || x===7){
            answer+='L'
            if(x===1) left = [0,0]
            else if(x===4) left= [1,0]
            else left=[2,0]
        }
        else if(x===3 || x===6 || x===9){
            answer+='R'
            if(x===3)right=[0,2]
            else if(x===6)right=[1,2]
            else right=[2,2]
        }
        else{
            if(x === 2){
                if(calcDistance(left,[0,1]) === calcDistance(right,[0,1])){
                    answer+=hand
                    hand === 'L' ? left = [0,1] : right = [0,1]
                }
                else if(calcDistance(left,[0,1])>calcDistance(right,[0,1])){
                    answer+='R'
                    right = [0,1]
                }
                else{
                    answer+='L'
                    left = [0,1]
                }
            }
            else if(x === 5){
                if(calcDistance(left,[1,1]) === calcDistance(right,[1,1])){
                    answer+=hand
                    hand === 'L' ? left = [1,1] : right = [1,1]
                }
                else if(calcDistance(left,[1,1])>calcDistance(right,[1,1])){
                    answer+='R'
                    right = [1,1]
                }
                else{
                    answer+='L'
                    left = [1,1]
                }
            }
            else if(x === 8){
                if(calcDistance(left,[2,1]) === calcDistance(right,[2,1])){
                    answer+=hand
                    hand === 'L' ? left = [2,1] : right = [2,1]
                }
                else if(calcDistance(left,[2,1])>calcDistance(right,[2,1])){
                    answer+='R'
                    right = [2,1]
                }
                else{
                    answer+='L'
                    left = [2,1]
                }
            }
            else if(x === 0){
                if(calcDistance(left,[3,1]) === calcDistance(right,[3,1])){
                    answer+=hand
                    hand === 'L' ? left = [3,1] : right = [3,1]
                }
                else if(calcDistance(left,[3,1])>calcDistance(right,[3,1])){
                    answer+='R'
                    right = [3,1]
                }
                else{
                    answer+='L'
                    left = [3,1]
                }
            }
        }
            
    }
    return answer;
}