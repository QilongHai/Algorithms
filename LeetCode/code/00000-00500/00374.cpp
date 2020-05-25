/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int i = 1;
        int j = n;
        int mid;
        while (i <= j) {
            mid = i + (j - i) / 2;
            int res = guess(mid);
            if (res == 0) {
                return mid;
            } else if (res == 1) {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }
        return -1;
    }
};