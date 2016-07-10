/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    var n = citations.length;
    var l = 0;
    var r = n;
    while (l < r)
    {
        var mid = Math.floor((l+r)/2);
        if (citations[mid] >= n-mid)
            r = mid;
        else
            l = mid + 1;
    }
    return n-l;
};
