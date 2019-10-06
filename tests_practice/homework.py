
def list_without_duplicates(list1, list2):
    result_list = []
    for i in list1:
        for k in list2:
            if i == k:
                result_list.append(i)
    for num in result_list:
        if num not in result_list:
            result_list.append(num)
    # return [num for num in result_list if num not in result_list]
    # for j in range(len(result_list)):
    #     if result_list[j] == result_list[j - 1]:
    #         result_list.remove(j)
    return result_list

