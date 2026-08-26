function isPalindrome(x: number): boolean {
    const y: string = x.toString();
    const reversed: string = y.split("").reverse().join("");

    return y === reversed;
}
