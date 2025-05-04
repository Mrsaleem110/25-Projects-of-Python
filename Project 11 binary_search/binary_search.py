# binary_search.py

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Checking middle index {mid}: {arr[mid]}")  # Debug line

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    print(f"[Recursion] Checking index {mid}: {arr[mid]}")

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def main():
    print("🔍 Binary Search Project - CMD Version")
    input_list = input("Enter sorted numbers (space-separated): ")
    arr = list(map(int, input_list.strip().split()))
    target = int(input("Enter the number to search: "))

    print("\n--- Iterative Binary Search ---")
    result_iter = binary_search_iterative(arr, target)
    if result_iter != -1:
        print(f"✅ Found at index {result_iter} (Iterative)")
    else:
        print("❌ Not found (Iterative)")

    print("\n--- Recursive Binary Search ---")
    result_rec = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result_rec != -1:
        print(f"✅ Found at index {result_rec} (Recursive)")
    else:
        print("❌ Not found (Recursive)")


if __name__ == "__main__":
    main()
