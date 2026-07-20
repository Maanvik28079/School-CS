dice_dict = {}

for i in range(6, 0, -1):
    for j in range(6, 0, -1):
        sum = i + j
        
        if sum not in dice_dict:
            dice_dict[sum] = ((i, j),)
        else:
            dice_dict[sum] = dice_dict[sum] + ((i, j),)

print(dice_dict)
