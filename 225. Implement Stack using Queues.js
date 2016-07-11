/**
 * @constructor
 */
var Stack = function() {
    this.q1 = [];
    this.q2 = [];
};

/**
 * @param {number} x
 * @returns {void}
 */
Stack.prototype.push = function(x) {
    this.q1.push(x);
};

/**
 * @returns {void}
 */
Stack.prototype.pop = function() {
    while (this.q1.length > 1)
        this.q2.push(this.q1.shift());
    this.q1.shift();
    while (this.q2.length > 0)
        this.q1.push(this.q2.shift());
};

/**
 * @returns {number}
 */
Stack.prototype.top = function() {
    while (this.q1.length > 1)
        this.q2.push(this.q1.shift());
    var temp = this.q1.shift();
    this.q2.push(temp);
    while (this.q2.length > 0)
        this.q1.push(this.q2.shift());
    return temp;
};

/**
 * @returns {boolean}
 */
Stack.prototype.empty = function() {
    return this.q1.length === 0 ? true : false;
};
