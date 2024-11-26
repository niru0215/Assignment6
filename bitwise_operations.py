import sys

def validate_input(input_data):
    try:
        integers = list(map(int, input_data.split(',')))
        return integers
    except ValueError:
        print("Error: Input must only contain integers separated by commas.")
        sys.exit(1)

def perform_bitwise_operations(numbers):
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]

    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    return bitwise_and, bitwise_or, bitwise_xor

def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

if __name__ == "__main__":
    # Check if the required arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python3 bitwise_operations.py <integers> <threshold>")
        print("Example: python3 bitwise_operations.py '3,5,7,9' 4")
        sys.exit(1)

    input_data = sys.argv[1]
    threshold = int(sys.argv[2])

    # Validate input and perform operations
    numbers = validate_input(input_data)
    and_result, or_result, xor_result = perform_bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold)

    # Print results
    print(f"Bitwise AND: {and_result}")
    print(f"Bitwise OR: {or_result}")
    print(f"Bitwise XOR: {xor_result}")
    print(f"Numbers greater than threshold: {filtered_numbers}")
