func twoSum(nums []int, target int) []int {
    res := []int {}
    dict := make(map[int]int)
    for i, val := range nums {
        if j, exist := dict[target-val]; exist {
            res = append(res, j)
            res = append(res, i)
        }
        dict[val] = i
    }
    return res
}