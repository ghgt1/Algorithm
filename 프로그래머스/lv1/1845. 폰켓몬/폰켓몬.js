function solution(nums) {
    var answer = 0;
    let map = new Map()
    for(let x of nums){
        map.set(x,map.get(x)+1||1)
    }
    if(nums.length/2 < map.size) return nums.length/2
    else return map.size
}