#include <vector>
#include <map>

using std::vector;
using std::map;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> nums_map;
		int i = 0;
		while (i < nums.size()) {
			if (nums_map.find(nums[i]) != nums_map.end())
				return {nums_map.find(nums[i])->second,i };
			nums_map[target-nums[i]] = i;
			i++;
        }
			return {};
    }
};