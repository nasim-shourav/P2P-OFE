var _ = require('underscore');
const JsonFind = require('json-find');

let arrayTwo = {
  'A' : '1',
  'B' : '3',
  'C' : '5',
  'G' : '8',
  'D': '4'
};
entries = Object.entries(arrayTwo)
k = Object.keys(arrayTwo);
vals = Object.values(arrayTwo);
SimpArray = [];


let countries = Object.keys(arrayTwo).reduce((acc, k) => {
  let country = arrayTwo[k];
  acc[country] = acc[country] || [];
  acc[country].push(k);
  return acc;
}, {});


new1 = countries['3'];


fin = _.difference(k, new1)

console.log("Fin", fin );


vals.forEach(function(item){
  if (item === '3'){
    function getKeyByValue(object, value) {
      return Object.keys(object).find(key => object[key] === value);
    }
    a = getKeyByValue(arrayTwo,'3');

    b = (_.invert(arrayTwo))['3'];
    SimpArray.push(b);
  }
});
console.log("Entries", entries);
console.log("Keys", k);
console.log("new1", new1);
// console.log("SimpArray", SimpArray);
// console.log("vals", vals);



