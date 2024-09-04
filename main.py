from typing import List

def findSmallest(array: list[int]) -> int:
    smallest_bits: int = f"{array[0]:b}".count("1")
    smallest_index: int = 0
    length_of_array: int = len(array)
    for i in range(1, length_of_array):
        current_bits: int = f"{array[i]:b}".count("1")
        if current_bits < smallest_bits:
            smallest_bits = current_bits
            smallest_index = i
        elif current_bits == smallest_bits:
            if array[i] < array[smallest_index]:
                smallest_index = i
    return smallest_index

def selectionBitsSort(array: List[int]) -> List[int]:
    new_array: list[int] = []
    length_of_array: int = len(array)
    for i in range(length_of_array):
        smallest: int = findSmallest(array)
        new_array.append(array.pop(smallest))
    return new_array

def sortByBits(arr: List[int]) -> List[int]:
    return selectionBitsSort(arr)

def main() -> None:
    print(sortByBits([0,1,2,3,4,5,6,7,8]))
    print(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))

if __name__ == "__main__":
    main()