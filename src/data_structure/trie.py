from copy import deepcopy


class TrieNode(object):
    """
    Node class of Trie. It consist of two part: value and the set of pointer to the children.
    """
    def __init__(self, val=None, using_deepcopy=False):
        """
        Initialize a Trie node with specific value.
        :param val: The value of new node.
        :param using_deepcopy: Whether using deepcopy to set node value.
        """
        self.next = {}
        if using_deepcopy:
            self.val = deepcopy(val)
        else:
            self.val = val


class Trie(object):
    """
    Class of Trie, which is a kind of search tree—an ordered tree data structure used to store a dynamic set or
    associative array where the keys are usually strings. (See: https://en.wikipedia.org/wiki/Trie)
    """
    def __init__(self, init_val=None, enable_deepcopy=False):
        """
        Init a Trie using specific initial value.
        :param init_val: Initial value of each Trie node.
        :param enable_deepcopy: Whether using the deepcopy to initialize the value of Trie node. This option is useful
        to avoiding initialize all nodes with a same reference when using list/dict as initial value.
        """
        self.enable_deepcopy = enable_deepcopy
        self.init_val = init_val
        self.root = TrieNode(self.init_val, self.enable_deepcopy)

    def insert(self, string, value, insert_on_path=False, reduce_func=lambda x, y: y):
        """
        Insert a new string to the Trie with specific value.
        :param string: The string which is used for inserting.
        :param value: The value which is used for inserting.
        :param insert_on_path: Whether set value of each node on the inserting path. This option is useful in some
        scenario such as counting the number of a specific prefix in a bunch of string.
        :param reduce_func: The function which is used for setting the value. The default value of this param will let
        each node save the latest value.
        """
        i, n = 0, len(string)
        node = self.root
        while i < n:
            if string[i] not in node.next:
                node.next[string[i]] = TrieNode(self.init_val, self.enable_deepcopy)

            if insert_on_path:
                node.val = reduce_func(node.val, value)
            node = node.next[string[i]]

            i += 1
        node.val = reduce_func(node.val, value)

    def get(self, string, reduce_func=lambda x, y: y, init_val=None):
        """
        Lookup the node value by specific string.
        :param string: The string which is used for lookup.
        :param reduce_func: The function which is used for reducing the value of nodes on the lookup path. The default
        value of this param will let the lookup process find the value of the "terminal" node.
        :param init_val: Initial value which is used for reducing. That is, the lookup process will return
        reduce_func(...reduce_func(val2, reduce_func(init_val, val1))...). The default value is None.
        :return: (bool, object). First member indicates whether the node with specific string is found
        and the second member is the reduced value on the lookup path.
        """
        i, n = 0, len(string)
        node = self.root
        v = init_val
        while i < n:
            if string[i] not in node.next:
                return False, v
            v = reduce_func(v, node.val)
            node = node.next[string[i]]
            i += 1

        v = reduce_func(v, node.val)
        return True, v
