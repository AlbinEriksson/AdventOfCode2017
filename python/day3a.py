import math

with open('input/input3', 'r') as input_file:
    square = int(input_file.read().strip())

ring = math.ceil(math.sqrt(square)) // 2
ring_size = ring * 2 + 1

ring_side_length = ring_size - 1
first_in_ring = (ring_size - 2) ** 2 + 1
index_in_ring = square - first_in_ring
index_in_side = (square - 1) % ring_side_length
distance_to_center = abs(index_in_side - ring_side_length // 2)

print(ring + distance_to_center)
