
class LargestPair:
    def adjacent_elements_product(input_array):
        largest_pair = -999
        for i in range(len(input_array)-1):
            sum_of_pairs = input_array[i] * input_array[i + 1]
            print(sum_of_pairs)
            import pdb; pdb.set_trace()
            if sum_of_pairs > largest_pair:
                largest_pair = sum_of_pairs

        return largest_pair


