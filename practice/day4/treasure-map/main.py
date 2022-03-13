#Print out map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

#Ask user about the map position
position = input("Where do you want to put the treasure? ")

#Calculate the position
horizontal = int(position[0])
vertical = int(position[1])

map[horizontal - 1][vertical - 1] = "X"

#Treasure position
print(f"{row1}\n{row2}\n{row3}")