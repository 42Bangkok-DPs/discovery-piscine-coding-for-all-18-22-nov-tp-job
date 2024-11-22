from checkmate import checkmate

# board
def main():

# 1 cheak
    board = """\
....
.K..
.Q..
....\
"""
    checkmate(board)

# 2 no cheak
    board = """\
........
........
....K...
........
.......R
\
"""
    checkmate(board)

# 3 no cheak
    board = """\
....
...K
\
"""
    checkmate(board)

if __name__ == "__main__":
    main()