/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    n = citations.length;
    for (var i = 0; i < n; i++)
    {
        if (citations[i] >= n-i)
            return n-i;
    }
    return 0;
};
