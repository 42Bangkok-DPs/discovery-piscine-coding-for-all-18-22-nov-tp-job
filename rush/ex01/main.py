from up_checkmate import checkmate

# board
def main():
# 1
    board = """\
.......
.K..
....
....\
"""
    checkmate(board)

# 2
    board = """\
........
...Q....
........
...K....
........
........
........
.......R
\
"""
    checkmate(board)

# 3
    board = """\
..........
...Q....
........
........
........
........
........
.......R
\
"""
    checkmate(board)

# 3
    board = """\
........
...Q....
........
...K....
........
................
........
.......R
\
"""
    checkmate(board)


if __name__ == "__main__":
    main()