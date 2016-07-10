/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    n = citations.length;
    citations.sort(function(a,b){return a-b});
    for (var i = 0; i < n; i++)
    {
        if (citations[i] >= n-i)
            return n-i;
    }
    return 0;
};
