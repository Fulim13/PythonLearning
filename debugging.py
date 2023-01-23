# Debugging
# 1 go to debugging to create a luanch.json
# select python
# select a break point (f9)
# f5 to run the debugging (Continue)
# f 10 is next (Step over)
# step into the function is (f11)
# step out  the function is (shift + f11)
# restart (ctrl shift f5)
# stop (ctrl f5)

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))


# Short cut for Window
# end key , from start line to end line
# home key, from end line to start line
# ctrl end , from first line of the file to last line of the file
# ctrl home, from last of file to first of file
# alt up and down, to move
# duplicate ,shift alt  down
# ctrl / , comment
