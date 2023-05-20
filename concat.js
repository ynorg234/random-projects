// What i think is in the concat function
class Str {
  constructor(info) {
  this.info = info;
  }
  concat(arg1) {
  var s1 = this.text.toString();
  var s2 = arg1.text;
  this.info = s1 + s2;
  }
  concatStr(arg1) {
    var s1 = this.text.toString();
    var s2 = arg1;
    this.info = s1 + s2;
  }
  get text() {
    return this.info;
  }
}

var string1 = new Str("Hello, ");
var string2 = new Str("World");
var string3 = ", This";
var string4 = " Is a Test.";
string1.concat(string2);
string1.concatStr(string3);
string1.concatStr(string4);
console.log(string1.info);
