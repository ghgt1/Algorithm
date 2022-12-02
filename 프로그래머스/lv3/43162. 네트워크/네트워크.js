function solution(n, computers) {
    var answer = 0;
    let graph = Array.from(Array(n + 1), () => Array());
    let check = Array(n + 1).fill(true);
    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){
            if(computers[i][j]===1) graph[i+1].push(j+1)
        }
    }
    function DFS(v) {
        for (let x of graph[v]) {
          if (check[x]) {
            check[x] = false;
            DFS(x);
          }
        }
      }
      for (let i = 1; i <= n; i++) {
        if (check[i]) {
          answer++;
          check[i] = false;
          DFS(i);
        }
      }
    return answer;
}