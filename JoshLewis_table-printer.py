# INF322 Python
# Josh Lewis
# Week 6 – Whiskey Reference Table Printer

whiskies = [['Single Distilled', 'Bourbon', 'Rye', 'Blended'],
             ['Twice Distilled', 'Scotch', 'Japanese', 'Single Malt'],
             ['Triple Distilled', 'Irish', 'Single Pot Still', ' ']]

def printTable(tableData):
    print("\n")
    print(" whiskey types ".upper().center(60, '='))
    colWidths = [0] * len(tableData)
    for j in range(len(tableData[0])):
        # Find max length of 3 columns
        for i in range(len(tableData)):
            # Set column width to max length of list item
            colWidths[i] = len((max(tableData[i], key = len)))
            cell = tableData[i][j]
            print(cell.rjust(colWidths[i]), end = "    ")
        print("\n")
            
printTable(whiskies)

print("To learn more, visit: www.whisky.com/information/\nCheers!")
print("\n")

