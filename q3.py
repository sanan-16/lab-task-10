import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def construct_huffman_tree(frequencies):
    # Create a priority queue to store Huffman nodes
    heap = [(freq, HuffmanNode(char, freq)) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the Huffman tree using a priority queue
    while len(heap) > 1:
        freq1, node1 = heapq.heappop(heap)
        freq2, node2 = heapq.heappop(heap)

        merged_node = HuffmanNode(None, freq1 + freq2)
        merged_node.left, merged_node.right = node1, node2

        heapq.heappush(heap, (freq1 + freq2, merged_node))

    # The final node at the top of the heap is the root of the Huffman tree
    return heap[0][1]

def print_huffman_codes(root, code="", result=None):
    if result is None:
        result = {}

    if root is not None:
        if root.char is not None:
            result[root.char] = code
        print_huffman_codes(root.left, code + "0", result)
        print_huffman_codes(root.right, code + "1", result)

    return result

# Example usage
frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
huffman_tree_root = construct_huffman_tree(frequencies)

huffman_codes = print_huffman_codes(huffman_tree_root)
print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
