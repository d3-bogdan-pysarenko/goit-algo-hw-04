def merge_two_sorted_lists(a, b):
    """Merging 2 ALREADY sorted lists"""
    i = 0
    j = 0
    result = []
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_k_sorted_lists(lists):
    """Merging ALREADY sorted lists"""
    if not lists:
        return []
    merged = lists[0]
    for i in range(1, len(lists)):
        merged = merge_two_sorted_lists(merged, lists[i])
    return merged


# Testing
lists = [[1, 4, 5], [1, 3, 4], [2, 6], [3,92, 105,216], [144, 216, 291], [8,10,15,21]]
merged_list = merge_k_sorted_lists(lists)
print("Merged sorted list:", merged_list)
