# Define build_bst() below...

def build_bst(my_list):
    if len(my_list) == 0:
        return "No Child"

    middle_idx = len(my_list) // 2
    middle_val = my_list[middle_idx]

    print("Middle Index: " + str(middle_idx))
    print("Middle Value: " + str(middle_val))

    tree_node = {"data": middle_val}
    tree_node["left_child"] = build_bst(my_list[: middle_idx])
    tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])
    return tree_node


# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
