def oops():
    raise IndexError("Error")

def index_oops():
    try:
        oops()
    except IndexError as index:
        print("Index error: ", index)

index_oops()

# def oops():
#     raise KeyError("Key error")

# def key_oops():
#     try:
#         oops()
#     except IndexError as index:
#         print("Index error", index)

# key_oops()

#PROGRAM CRASHES, THEN KeyError EXECUTES