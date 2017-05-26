var multipleOf3Regex = new function() {this.test = function(bin) {if( !(/\s/g.test(bin)) && (parseInt(bin, 2) % 3 == 0) && (typeof bin === "string")){return true}else{return false}}}

Test.assertEquals(multipleOf3Regex.test(0), false);
Test.assertEquals(multipleOf3Regex.test(true), false);
Test.assertEquals(multipleOf3Regex.test(" 0"), false);
Test.assertEquals(multipleOf3Regex.test("abc"), false);
Test.assertEquals(multipleOf3Regex.test("000"), true);

Test.assertEquals(multipleOf3Regex.test("110"), true);
Test.assertEquals(multipleOf3Regex.test("111"), false);
Test.assertEquals(multipleOf3Regex.test((12345678).toString(2)), true);