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

const t0 = new Date().getTime();
console.log(fibo(45));
console.log((new Date().getTime() - t0) / 1000);
