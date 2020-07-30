# Ask the user how many sobas are on the table
sobas_on_table = int(input("How many sobas are on the table?: "))
# Ask the user how many sobas can Ken eat
ken_capacity = int(input("How many sobas can Ken eat?: "))
# Sobas that Ken has already eaten
eaten_sobas = 0

# While the sobas Ken already ate are less than his
# capacity AND while there are still more than 0
# sobas on the table...
while eaten_sobas < ken_capacity and sobas_on_table > 0:
    print("Ken has eaten a soba.")
    eaten_sobas += 1
    sobas_on_table -= 1
    print("Until now Ken has eaten", eaten_sobas, "sobas. And there are", sobas_on_table, "sobas on the table left.")

# While loop completed
if eaten_sobas == ken_capacity and sobas_on_table == 0:
    print("Ken was able to perfectly eat all sobas on the table, and is now full!")
elif eaten_sobas < ken_capacity and sobas_on_table == 0:
    print("Ken ate all sobas on the table and could still eat", ken_capacity-eaten_sobas, "sobas.")
elif eaten_sobas == ken_capacity and sobas_on_table > 0:
    print("Ken wasn't able to eat all sobas. There are still", sobas_on_table, "sobas on the table.")
else:
    print("Not sure what happened.")
