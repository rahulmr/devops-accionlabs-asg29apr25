class ArrayIntersection:
    def find_common_elements(self, arr1, arr2):
        i = 0  # pointer for arr1
        j = 0  # pointer for arr2
        result = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                # Only add if the element is not already in result
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

        return result

# Example usage
if __name__ == "__main__":
    # Create an instance of the class
    solution = ArrayIntersection()

    # Test arrays
    array1 = [1, 2, 2, 3, 4, 5]
    array2 = [2, 2, 3, 5, 6]

    # Get common elements
    result = solution.find_common_elements(array1, array2)
    print(f"Common elements: {result}")  # Output: [2, 3, 5]