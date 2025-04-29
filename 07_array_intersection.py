class ArrayProcessor:
    def find_common_elements(self, array1, array2):
        # Use set intersection to find common elements and remove duplicates
        return list(set(array1) & set(array2))

# Example usage
processor = ArrayProcessor()
result = processor.find_common_elements([1, 2, 2, 3], [2, 3, 4])
print(result)  # Output: [2, 3]