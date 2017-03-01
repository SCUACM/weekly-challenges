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

def array_multiply_efficient(array):
        # [ a,     b,   c,    d,    e  ]

        # We want an answer like
        # [ bcde, a cde, ab de, abc e, abcd ]

        # We can split the prefixes above into a second array
        # Multiply the element of each together for the answer

        # STEP 1
        # partial = [bcde,  cde,  de,   e,    1  ]
        # prefixes = [  1 ,  a,    ab,   abc, abcd]

        # STEP 2
        # result = [bcde*1, cde*a, de*ab, e*abc, 1*abcd]

        partial = []
        prefixes = []

        # Make an array of lists of numbers to be multiplied together
        for i in range(len(array)):
                # Append a 1 at the end
                if not array[i+1:]:
                        partial.append([1])
                        break
                partial.append(array[i + 1:])

        for i in range(len(array)):
                # Append a 1 at the start
                if not array[:i]:
                        prefixes.append([1])
                        continue
                prefixes.append(array[:i])


        # Multiply the elements together, as each element is a list of the
        # numbers to multiply at this point
        partial = [reduce(lambda x, y: x*y, r) for r in partial]
        prefixes = [reduce(lambda x, y: x*y, r) for r in prefixes]

        # Now multiply each element in the partials list by its corresponding
        # element in the partials list
        result = [x * y for x, y in zip(partial, prefixes)]

        return result


if __name__ == "__main__":
        print(array_multiply([1,2,3,4,5]))
        print(array_multiply_efficient([1,2,3,4,5]))



