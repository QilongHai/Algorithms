/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 func merge_tow_sorted_list(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil {
        return l2
    }
    if l2 == nil {
        return l1
    }
    dummy := &ListNode{}
    cur := dummy
    for l1 != nil && l2 != nil {
        if l1.Val < l2.Val {
            cur.Next = l1
            l1 = l1.Next
        } else {
            cur.Next = l2
            l2 = l2.Next
        }
        cur = cur.Next
    }
    if l1 != nil {
        cur.Next = l1
    }
    if l2 != nil {
        cur.Next = l2
    }
    return dummy.Next
}

func merge(lists []*ListNode, start int, end int) *ListNode {
    if start == end {
        return lists[start]
    }
    if start > end {
        return nil
    }
    mid := start + (end - start) / 2
    l1 := merge(lists, start, mid)
    l2 := merge(lists, mid+1, end)
    return merge_tow_sorted_list(l1, l2)
}


func mergeKLists(lists []*ListNode) *ListNode {
    if lists == nil || len(lists) == 0 {
        return nil
    }
    return merge(lists, 0, len(lists)-1)
}