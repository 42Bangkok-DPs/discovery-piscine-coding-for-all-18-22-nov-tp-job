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
Q.......
........
........
...K....
.......R
\
"""
    checkmate(board)

if __name__ == "__main__":
    main()