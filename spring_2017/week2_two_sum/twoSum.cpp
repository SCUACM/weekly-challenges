// Given an array of integers, return indices of the two numbers such that they
// add up to a specific target.

// You may assume that each input would have exactly one solution, and you may
// not use the same element twice.

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // ----- N^2 solution -----
        // For each element in vector, iterate through the rest of the elements
        // and check to see if numbers sum to target


        // ----- N solution (two passes) -----
        // Hash Table: Constant Look up Time (unless there are collisions)
        // Unordered_Map: Key=num, Value=index

        unordered_map<int, int> hashTable;
        vector<int> result;
        vector<int>::iterator it = nums.begin();

        // Place all items into hash table
        for (int i = 0; it != nums.end(); it++, i++) {
            hashTable[nums[i]] = i;
        }

        // Check to see if complement is available for all items in hashtable
        for (it = nums.begin(); it != nums.end(); it++) {
            int complement = target - *it;

            // Check to see if the complement is found
            if ((hashTable.find(complement)) != hashTable.end()) {

                // Check to make sure they do not both have same index
                if (hashTable[*it] == hashTable[complement]) {
                    continue;
                }

                cout << *it << " " << complement << endl;

                result.push_back(hashTable[*it]);
                result.push_back(hashTable[complement]);

                return result;
            }

        }

        return result;
    }
};

int main() {
    Solution x;

    vector<int> arr;
    vector<int> res;
    vector<int>::iterator it;

    arr.push_back(1);
    arr.push_back(3);
    arr.push_back(8);
    arr.push_back(14);
    arr.push_back(12);
    arr.push_back(9);
    arr.push_back(20);

    res = x.twoSum(arr, 11);

    for (it = res.begin(); it != res.end(); it++) {
        cout << *it << endl;
    }
}
