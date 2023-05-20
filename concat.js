// What i think is in the concat function
class Str {
  constructor(info) {
  this.info = info;
  }
  concat(arg1) {
  var s1 = this.info.toString();
  var s2 = arg1.toString();
  return s1 + s2
  }
  get info() {
  return this.info;
  }
}

var string1 = new Str("Hello ");
var string2 = new Str("World!");
string1.concat(string2);
console.log(string1);
