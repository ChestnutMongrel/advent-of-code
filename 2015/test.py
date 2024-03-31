for old_index in range(8):
    shift = 1 + old_index + int(old_index >= 4)
    print(old_index, shift, (old_index + shift) % 8)