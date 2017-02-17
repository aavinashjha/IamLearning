from linked_list import LLOperations


def test_normal_deletion():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)

    LLOperations.print_my_linked_list(linked_list)

    LLOperations.delete_node(linked_list, 3)
    LLOperations.print_my_linked_list(linked_list)


def test_head_deletion():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    LLOperations.print_my_linked_list(linked_list)
    LLOperations.delete_node(linked_list, 1)
    LLOperations.print_my_linked_list(linked_list)


def test_tail_deletion():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    LLOperations.print_my_linked_list(linked_list)

    LLOperations.delete_node(linked_list, 5)
    LLOperations.print_my_linked_list(linked_list)


def test_linked_list_has_loop():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    assert LLOperations.linked_list_has_loop(linked_list) is False

    LLOperations.create_loop(linked_list, 3)
    assert LLOperations.linked_list_has_loop(linked_list) is True


def test_linked_list_loop_length_3():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    assert LLOperations.get_length_of_loop(linked_list) == 0
    LLOperations.create_loop(linked_list, 3)
    assert LLOperations.get_length_of_loop(linked_list) == 3


def test_linked_list_loop_length_1():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    assert LLOperations.get_length_of_loop(linked_list) == 0
    LLOperations.create_loop(linked_list, 5)
    assert LLOperations.get_length_of_loop(linked_list) == 1


def test_linked_list_loop_length_5():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    assert LLOperations.get_length_of_loop(linked_list) == 0
    LLOperations.create_loop(linked_list, 1)
    assert LLOperations.get_length_of_loop(linked_list) == 5


def test_loop_removal():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    LLOperations.print_my_linked_list(linked_list)

    LLOperations.create_loop(linked_list, 1)
    assert LLOperations.linked_list_has_loop(linked_list) is True
    assert LLOperations.get_length_of_loop(linked_list) == 5

    LLOperations.remove_loop(linked_list)
    assert LLOperations.linked_list_has_loop(linked_list) is False
    LLOperations.print_my_linked_list(linked_list)


def test_reversing_linked_list():
    user_input = '1,2,3,4,5'
    linked_list = LLOperations.make_my_linked_list(user_input)
    LLOperations.print_my_linked_list(linked_list)
    LLOperations.reverse_a_linked_list(linked_list)
    LLOperations.print_my_linked_list(linked_list)