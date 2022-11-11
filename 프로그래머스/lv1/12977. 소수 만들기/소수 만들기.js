function solution(nums) {
    var answer = 0;
    
    function prime(a){
        for(let i=2;i*i<=a;i++){
            if(a%i===0) return false
        }
        return true
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')
//     3중포문해도 10만번 정도임
//     각각에 대해서 소수판별을 10만미만으로 계산하면됨
    let total = 0
    for(let i =0;i<nums.length-2;i++){
        for(let j=i+1;j<nums.length-1;j++){
            for(let k=j+1;k<nums.length;k++){
                total = nums[i] + nums[j] + nums[k]
//                 소수면
                if(prime(total))answer++
            }
        }
    }
    return answer;
}