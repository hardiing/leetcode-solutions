// easy difficulty

var isPalindrome = function(x) {
    if (parseFloat(x.toString().split("").reverse().join("")) === x) {
        return true;
    } else {
        return false;
    }
};