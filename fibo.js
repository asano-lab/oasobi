// フィボナッチ数列
const fibo = (n) => {
    if (n <= 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fibo(n - 1) + fibo(n - 2);
}

const n = 45;

const os = require('os');
console.log(os.cpus()[0].model);
console.log(`nodejs v${process.versions.node}`);

const t0 = new Date().getTime();

console.log(`fibo(${n}) = ${fibo(n)}`);

console.log((new Date().getTime() - t0) / 1000, "秒");
