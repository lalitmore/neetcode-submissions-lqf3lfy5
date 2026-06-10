class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_cache = defaultdict(list)
        res = True;
        col_cache = defaultdict(list)
        squares = defaultdict(set) # key = (r/3, c/3)

        for indexR, x in enumerate(board):
            for index, y in enumerate(x):
                if board[indexR][index] == ".":
                    continue
                # Checking every row
                if y in row_cache[indexR + 1]:
                    return False
                elif y != ".":
                    row_cache[indexR + 1].append(y)
                # Checking every column
                if y in col_cache[index + 1]:
                    return False
                elif y != ".":
                    col_cache[index + 1].append(y)
                # Checking square
                if board[indexR][index] in squares[( indexR // 3, index // 3)]:
                    return False
                squares[( indexR // 3, index // 3)].add(board[indexR][index])
                

        for key,value in row_cache.items():
            print(f"{key}: {value}")
        print("")
        for key,value in col_cache.items():
            print(f"{key}: {value}")
        return res


        