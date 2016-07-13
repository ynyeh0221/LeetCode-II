/**
 * @constructor
 */
var Queue = function() {
    this.s1 = [];
    this.s2 = [];
};

/**
 * @param {number} x
 * @returns {void}
 */
Queue.prototype.push = function(x) {
    this.s1.push(x);
};

/**
 * @returns {void}
 */
Queue.prototype.pop = function() {
    if (this.s2.length > 0)
        this.s2.pop();
    else
    {
        while (this.s1.length > 0)
            this.s2.push(this.s1.pop());
        this.s2.pop();
    }
};

/**
 * @returns {number}
 */
Queue.prototype.peek = function() {
    if (this.s2.length > 0)
        return this.s2[this.s2.length-1];
    else
    {
        while (this.s1.length > 0)
            this.s2.push(this.s1.pop());
        return this.s2[this.s2.length-1];
    }
};

/**
 * @returns {boolean}
 */
Queue.prototype.empty = function() {
    return (this.s1.length === 0 && this.s2.length === 0) ? true : false;
};
