function BFS(graph2,a,b){
    let graph3 = []
    for(let x of graph2){
        graph3.push([...x])
    }
    let dx = [-1,1,0,0]
    let dy = [0,0,-1,1]
    graph3[a][b] = 0
    let queue = [[a,b]]
    let count = 0
    while(queue.length!==0){
        let [x,y] = queue.shift()
        for(let i=0;i<4;i++){
            let nx = x+dx[i]
            let ny = y+dy[i]
            if(nx<0 || ny<0 || nx>=5 || ny>=5 || graph3[nx][ny] === 'X' || !isNaN(graph3[nx][ny])){
                continue
            }
            if(graph3[nx][ny] === 'P'){
                if(Math.abs(nx-a)+Math.abs(ny-b) <=2){
                    if(graph3[x][y]<=1) {
                        return false
                    }
                    
                }
                else{
                    queue.push([nx,ny])
                    graph3[nx][ny] = graph3[x][y]+1;
                    continue
                }
            }
            graph3[nx][ny] = graph3[x][y]+1;
            queue.push([nx,ny])
        }
    }
    return true
}

function solution(places) {
    var answer = [];
//     갈수있는지없는지 보면됨
//     맨해튼거리계산은 좌표랑 절댓값만 쓰면됨
    for(let x of places){
        let result = 1
        // console.log(x)
//     모든점 돌면서 플레이어가있는 곳에서 출발.
        let graph = []
        for(let q of x){
            graph.push(q.split(""))
        }
        (()=>{
        for(let x=0;x<5;x++){
            for(let y=0;y<5;y++){
                if(graph[x][y] === "P"){
//                     탐색후, 결과에따라 result 0으로 변경
                    if(!BFS(graph,x,y)){
                        result = 0
                        return;
                    }
                }
            }
        }
        })()
        answer.push(result)
    }
    return answer;
}