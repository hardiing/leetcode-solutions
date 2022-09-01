class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode() # set up dummy list for output
        tail = dummy # set the tail of the dummy list

        while list1 and list2: # while both lists aren't null
            if list1.val < list2.val: # if value of 1 < 2
                tail.next = list1 # add to tail of output
                list1 = list1.next # and move to next node
            else:
                tail.next = list2 # otherwise put list 2 at tail
                list2 = list2.next # and move to next node
            tail = tail.next # move the tail to the next node

        if list1: # if lists aren't null after comparing all of one
            tail.next = list1 # append them to the end of the output
        elif list2:
            tail.next = list2

        return dummy.next
