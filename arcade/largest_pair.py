
class LargestPair:
    def adjacent_elements_product(input_array):
        largest_pair = 0
        for i in range(len(input_array)-1):
            import pdb; pdb.set_trace()
            sum_of_pairs = input_array[i] * input_array[i + 1]
            if largest_pair > sum_of_pairs:
                largest_pair = sum_of_pairs

        return largest_pair


