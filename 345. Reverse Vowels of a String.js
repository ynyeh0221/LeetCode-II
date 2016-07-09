// memory limit exceed

/**
 * @param {string} s
 * @return {string}
 */
String.prototype.replaceAt = function(index, character)
{
    return this.substr(0, index) + character + this.substr(index+character.length);
}

var reverseVowels = function(s) {
    var vowel = ['A','E','I','O','U','a','e','i','o','u'];
    var l = 0;
    var r = s.length-1;
    while (l <= r)
    {
        var indl = vowel.indexOf(s[l]);
        var indr = vowel.indexOf(s[r]);
        if (indl != -1 && indr != -1)
        {
            var temp = s[l];
            s = s.replaceAt(l, s[r]);
            s = s.replaceAt(r, temp);
            l += 1;
            r -= 1;
        }
        else if (indl == -1 && indr != -1)
            l += 1;
        else if (indl != -1 && indr == -1)
            r -= 1;
        else
        {
            l += 1;
            r -= 1;
        }
    }
    return s;
};
