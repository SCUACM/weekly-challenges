#!/usr/bin/python
def array_multiply(array):
        """
        Given an array, replace the value at index i with the product of all
        other values in the array
        Return the new array
        """
        new_array = []
        for i in range(len(array)):
                # Remove the element at i and save it
                save = array.pop(i)
                # Work with the modified array
                sub = array
                # Place the multipled product in the new array
                new_array.append(reduce(lambda x, y: x*y, sub))
                # Place the element at i back inside the original array at the
                # correct index
                array.insert(i, save)

        return new_array


if __name__ == "__main__":
        print(array_multiply([1,2,3,4,5]))

