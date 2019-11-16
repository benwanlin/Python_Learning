"""
Author: Ben
Date: 11/16/2019
"""


class ListNode:
    def __init__(self, data):
        """constructor to initiate the object."""

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        """method to compare the value with the node data."""
        if self.data == value:
            return True
        else:
            return False


class SingleLinkedList:
    def __init__(self):
        """constructor to initiate this object."""

        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        """add an item at the end of the list"""

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return

    def list_length(self):
        """returns the number of list items"""

        count = 0
        current_node = self.head

        while current_node is not None:
            # increase counter by one
            count += 1

            # jump to the linked node
            current_node = current_node.next

        return count

    def output_list(self):
        """outputs the list (the value of the node, actually)"""

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def unordered_search(self, value):
        """search the linked list for the node that has this value"""

        # define current_node
        cureent_node = self.head

        # define position
        node_id = 0

        # define list of result
        result = []

        while cureent_node is not None:
            if cureent_node.has_value(value):
                result.append(node_id)

            # jump to the linked node
            cureent_node = cureent_node.next
            node_id += 1

        return result


node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = "Berlin"
node4 = ListNode(15)

track = SingleLinkedList()
print("track length: %i" % track.list_length())

for current_item in [node1, node2, node3, node4]:
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()

current_item.
