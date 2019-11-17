# while True:
#     try:
#         """
#         Author: Ben
#         Date: 11/16/2019
#         """
#
#
#         class ListNode:
#             def __init__(self, data):
#                 """constructor to initiate the object."""
#
#                 # store data
#                 self.data = data
#
#                 # store reference (next item)
#                 self.next = None
#                 return
#
#             def has_value(self, value):
#                 """method to compare the value with the node data."""
#                 if self.data == value:
#                     return True
#                 else:
#                     return False
#
#
#         class SingleLinkedList:
#             def __init__(self):
#                 """constructor to initiate this object."""
#
#                 self.head = None
#                 self.tail = None
#                 return
#
#             def add_list_item(self, item):
#                 """add an item at the end of the list"""
#
#                 if not isinstance(item, ListNode):
#                     item = ListNode(item)
#
#                 if self.head is None:
#                     self.head = item
#                 else:
#                     self.tail.next = item
#
#                 self.tail = item
#                 return
#
#             def list_length(self):
#                 """returns the number of list items"""
#
#                 count = 0
#                 current_node = self.head
#
#                 while current_node is not None:
#                     # increase counter by one
#                     count += 1
#
#                     # jump to the linked node
#                     current_node = current_node.next
#
#                 return count
#
#             def output_list(self):
#                 """outputs the list (the value of the node, actually)"""
#
#                 current_node = self.head
#
#                 result_string = ''
#                 while current_node is not None:
#                     result_string += str(current_node.data) + ' '
#                     current_node = current_node.next
#                 print(result_string)
#                 return
#
#             def unordered_search(self, value):
#                 """search the linked list for the node that has this value"""
#
#                 # define current_node
#                 cureent_node = self.head
#
#                 # define position
#                 node_id = 0
#
#                 # define list of result
#                 results = []
#
#                 while cureent_node is not None:
#                     if cureent_node.has_value(value):
#                         results.append(node_id)
#
#                     # jump to the linked node
#                     cureent_node = cureent_node.next
#                     node_id += 1
#
#                 return results
#
#             def remove_list_item_by_id(self, item_id):
#                 """remove the list item with the item id"""
#
#                 current_id = 0
#                 current_node = self.head
#                 previoud_node = None
#
#                 while current_node is not None:
#                     if current_id == item_id:
#                         if previoud_node is not None:
#                             previoud_node.next = current_node.next
#                         else:
#                             self.head = current_node.next
#                         return
#
#                     previoud_node = current_node
#                     current_node = current_node.next
#                     current_id += 1
#
#                 return
#
#             def insert_list_item_after_item_id(self, item_id, item):
#                 """insert the list item with the item_id"""
#                 current_id = 0
#                 current_node = self.head
#                 previous_node = None
#
#                 if not isinstance(item, ListNode):
#                     item = ListNode(item)
#
#                 while current_node is not None:
#                     if current_id == item_id:
#                         next_node = current_node.next
#                         item.next = next_node
#                         current_node.next = item
#                         return
#                     current_id += 1
#                     previous_node = current_node
#                     current_node = previous_node.next
#                 return
#
#
#         listed_node_len = int(input().strip())
#         listed_nost_obj = SingleLinkedList()
#         listed_nost_obj.add_list_item(int(input().strip()))
#
#         for i in range(listed_node_len - 1):
#             new_item, item = [int(j) for j in input().strip().split()]
#             item_ids = listed_nost_obj.unordered_search(item)
#             for item_id in item_ids:
#                 listed_nost_obj.insert_list_item_after_item_id(item_id, new_item)
#
#         item_to_remove = int(input().strip())
#         item_ids = listed_nost_obj.unordered_search(item_to_remove)
#         for item_id in item_ids:
#             listed_nost_obj.remove_list_item_by_id(item_id)
#
#         listed_nost_obj.output_list()
#
#
#     except:
#         break

while True:
    try:
        s = input().split()
        num = int(s[0])
        res = [s[1]]
        for i in range(num - 1):
            a = s[2 + i * 2]
            b = s[3 + i * 2]
            res.insert(res.index(b) + 1, a)
        rm = s[-1]

        res.remove(rm)
        print(' '.join(res) + ' ')
    except:
        break