/*
 * Very naïve approach.
 *
 * Algorithm:
 *     s
 */

var _input = "";
const MARKER = '∏';

// Gets all unique substrings of a string.
function getSubstrings(str) {
    var result = new Set();

    // For an offset {i} ∈ [0, len({str})], get all substrings sizes {S} ∈ [j - i, len({str}) - i].
    for (var i = 0; i < str.length; ++i) {
        for (var j = i + 1; j < str.length + 1; ++j) {
            result.add(str.slice(i, j));
        }
    }

    return Array.from(result);
}

// Replaces [start, end] of a string {str} with repeated character {rstr}.
function innerRepeat(str, start, end, rstr) {
    return str.substring(0, start) + rstr.repeat(end - start) + str.substring(end, str.length);
}

// Gets letter islands for a string {str} given substring {s}.
function getIslands(str, s) {
    var ind = -1, tstr = str;

    // Find and mark all substrings with {MARKER}.
    while ((ind = str.indexOf(s, ind + 1)) !== -1) {
        tstr = innerRepeat(tstr, ind, ind + s.length, MARKER);
    }

    // RegExp search for all occurrences of groups of {MARKER}.
    return (tstr.match(new RegExp(`${MARKER}+`, 'g')) || { length: 0 }).length;
}

// Wrapper function that gets all substrings and counts islands for each
// substring.
function processData({ str, islands }) {
    return getSubstrings(str).filter(s => getIslands(str, s) === islands).length;
}

// Read, convert input, and send to {processData}.
process.stdin
    .resume()
    .setEncoding("ascii")
    .on("data", function (input) {
        _input += input;
    })
    .on("end", function () {
        var { 0: str, 1: islands } = _input.split('\n');
        console.log(processData({ str, islands: +islands }));
    });
