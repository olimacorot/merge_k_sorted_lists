import unittest
from practicing.merge_k_sorted_lists.main import ListNode
from practicing.merge_k_sorted_lists.main import Solution

class TestMergeKSortedLists(unittest.TestCase):

    def test_it_should_return_a_sorted_list(self):
        solution = Solution()
        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(3, ListNode(6)),
        ]
        want = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))

        self.assertAlmostEqual(want, solution.mergeKLists(lists))
