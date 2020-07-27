house_capacity = 100
house_boxes = 0
boxes = 100

while house_boxes < house_capacity and boxes > 0:
    print("Moved a box")
    boxes -= 1
    house_boxes += 1
    print("There are now", boxes, "boxes that can be moved.")
    print("There are now", house_boxes, "in the house.")

# Reason for stopping
if boxes == 0 and house_boxes == house_capacity:
    print("Stopped. All boxes fit perfectly inside your house!")
elif boxes == 0:
    print("Stopped because you have no more boxes.")
else:
    print("Stopped because there is no more space in the house.")
