func spiralOrder(matrix [][]int) []int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return []int{}
    }
    var rows = len(matrix)
    var cols = len(matrix[0])
    var res = make([]int, rows * cols)
    var idx = 0
    var left = 0
    var right = cols - 1
    var top = 0
    var bottom = rows - 1

    for left <= right && top <= bottom {
        for col := left; col <= right; col++ {
            res[idx] = matrix[top][col]
            idx++
        }
        for row := top+1; row <= bottom; row++ {
            res[idx] = matrix[row][right]
            idx++
        }
        if left < right && top < bottom {
            for col := right - 1; col > left; col-- {
                res[idx] = matrix[bottom][col]
                idx++
            }
            for row := bottom; row > top; row-- {
                res[idx] = matrix[row][left]
                idx++
            }
        }
        left++
        right--
        top++
        bottom--
    }
    return res
}