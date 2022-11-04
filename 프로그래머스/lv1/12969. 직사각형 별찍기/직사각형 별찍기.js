process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    let answer = ""
    for(let tmp = b;tmp>0;tmp--){
        for(let tmp2=a;tmp2>0;tmp2--){
            answer+='*'
        }
        answer+='\n'
    }
    console.log(answer)
});