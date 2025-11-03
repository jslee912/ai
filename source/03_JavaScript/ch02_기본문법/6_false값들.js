// false로 해석되는 값들 : 0, "",Nan, null, undefined   cf. 빈배열[]은 true/ 파이썬에서는 빈배열[]은 false
var i;
console.log(Boolean(i));
console.log(Boolean(0));
console.log(Boolean(NaN));
console.log(Boolean(Number("a")));
console.log(Boolean(""));
console.log(Boolean(null));
console.log();
console.log("0==false의 결과 :", 0==false);
console.log("0===false의 결과 :", 0===false);
// ctrl+j(터미널창) node 파일명