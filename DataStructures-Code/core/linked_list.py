class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head


class LLOperations:

    def connect_nodes(first, second):
        if first is not None:
            first.next = second

    def make_my_linked_list(user_input):
        first = None
        for element in user_input.split(','):
            second = Node(int(element))
            LLOperations.connect_nodes(first, second)
            if first is None:
                ll = LinkedList(second)
            first = second
        return ll

    def create_loop(linked_list, data):
        head = linked_list.head
        mover = head
        while mover is not None:
            if mover.data == data:
                loop_node = mover
            if mover.next is None:
                last_node = mover
            mover = mover.next
        last_node.next = loop_node

    def print_my_linked_list(linked_list):
        head = linked_list.head
        while(head is not None):
            print(head.data, end='')
            head = head.next
        print(' ')

    def delete_node(linked_list, data):
        head = linked_list.head
        mover = head
        prev = None
        while mover is not None:
            if mover.data == data:
                if mover is head:
                    linked_list.head = head.next
                else:
                    prev.next = mover.next
                break
            prev = mover
            mover = mover.next

    def linked_list_has_loop(linked_list):
        head = linked_list.head
        fp = head
        sp = head

        while fp is not None:
            if fp and fp.next and fp.next.next:
                fp = fp.next.next
            else:
                return False
            if sp and sp.next:
                sp = sp.next
            if fp == sp:
                return True
        return False

    def get_length_of_loop(linked_list):
        head = linked_list.head
        count = 0
        if LLOperations.linked_list_has_loop(linked_list):
            sp = head
            fp = head
            while fp is not None:
                if fp and fp.next and fp.next.next:
                    fp = fp.next.next
                if sp and sp.next:
                    sp = sp.next
                if fp == sp:
                    loop_node = sp
                    break

            while True:
                count += 1
                sp = sp.next
                if sp == loop_node:
                    break

        return count

    def remove_loop(linked_list):
        head = linked_list.head
        if LLOperations.linked_list_has_loop(linked_list):
            sp = head
            fp = head
            while fp is not None:
                if fp and fp.next and fp.next.next:
                    fp = fp.next.next
                if sp and sp.next:
                    prev = sp
                    sp = sp.next
                if fp == sp:
                    break
            prev.next = None

    def reverse_a_linked_list(linked_list):
        head = linked_list.head
        current = head
        later = None
        while current is not None:
            prev = current

            current = current.next
            prev.next = later
            if current:
                later = current.next
            else:
                later = None
                print('I have reached here')
                linked_list.head = prev

            current.next = prev

            if later:
                temp = later.next
                later.next = current
                current = temp


if __name__ == '__main__':
    user_input = input('Enter the numbers you want to store in linked list')
    linked_list = LLOperations.make_my_linked_list(user_input)
    LLOperations.print_my_linked_list(linked_list)
    LLOperations.reverse_a_linked_list(linked_list)
    LLOperations.print_my_linked_list(linked_list)
