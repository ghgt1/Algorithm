function solution(graph) {
    var answer = 0;
  //     최단거리니까 BFS접근
  let dx = [-1, 1, 0, 0];
  let dy = [0, 0, -1, 1];
  let n = graph.length;
  let m = graph[0].length;
  function BFS(x, y) {
    let queue = [];
    queue.push([x, y]);
    while (queue.length) {
      let [x, y] = queue.shift();
      if (x === n - 1 && y === m - 1) return;
      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
        if (graph[nx][ny] === 1 ) {
          graph[nx][ny] = graph[x][y] + 1;
          queue.push([nx, ny]);
        }
          
      }
        graph[x][y] = 0
    }
  }
  BFS(0, 0);
  answer = graph[n - 1][m - 1];
    if(answer === 1) answer = -1
    return answer;
}