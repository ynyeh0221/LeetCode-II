/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    let A = 0, B = 0;
    let dic = {};
    for (let i = 0; i < secret.length; i++)
    {
        if (secret[i] == guess[i])
            A += 1;
        else
        {
            if (!(secret[i] in dic))
                dic[secret[i]] = 0;
            dic[secret[i]] += 1;
        }
    }
    for (let i = 0; i < secret.length; i++)
    {
        if (secret[i] != guess[i] && dic[guess[i]] > 0)
        {
            B += 1;
            dic[guess[i]] -= 1;
        }
    }
    return A.toString() + 'A' + B.toString() + 'B';
};
