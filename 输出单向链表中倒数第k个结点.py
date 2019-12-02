while True:
    try:
        """
        Author: Ben
        Date: 11/17/2019
        Filename: 输出单向链表中，倒数第k个结点
        """


        class Listed_Node:
            def __init__(self, data):
                self.data = data
                self.next = None
                return

            def has_value(self, value):
                if self.data == value:
                    return True
                else:
                    return False

        class Single_Linked_List:
            def __init__(self):
                self.head = None
                self.tail = None
                return

            def add_node(self, item):
                if not isinstance(item, Listed_Node):
                    item = Listed_Node(item)

                if self.head is None:
                    self.head = item
                else:
                    self.tail.next = item
                self.tail = item
                return

            def get_kth_to_end(self, k):
                total = 1
                current_node = self.head

                while current_node.next is not None:
                    current_node = current_node.next
                    total += 1

                current_node = self.head
                count = 1
                while current_node.next is not None and count + k <= total:
                    current_node = current_node.next
                    count += 1

                return current_node.data

        single_linked_list = Single_Linked_List()
        count = int(input().strip())
        node_values = [int(i) for i in input().strip().split()]
        for i in range(count):
            single_linked_list.add_node(node_values[i])

        kth_to_end = int(input().strip())
        if kth_to_end == 0:
            print(0)
        else:
            print(single_linked_list.get_kth_to_end(kth_to_end))
    except:
        break