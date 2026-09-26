class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        seen = set()
        for i in range(len(board)):
            for num in board[i]:
                if num.isnumeric():
                    if num in seen:
                        print(f"seen two numbers in row {i}: {num}")
                        return False
                    seen.add(num)
            seen.clear()
            
        # check cols
        print(seen)
        seen.clear()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i].isnumeric():
                    if board[j][i] in seen:
                        print(f"seen two numbers in column {i}: {board[j][i]}")
                        print(seen)
                        return False
                    seen.add(board[j][i])
            seen.clear()

        # check boxes
        # have three sets and clear them three times when i is div by 3
        s1, s2, s3 = set(), set(), set()
        for i in range(len(board)):
            if i % 3 == 0: 
                s1.clear()
                s2.clear()
                s3.clear()

            for j in range(len(board)):
                num = board[i][j]
                if j < 3 and num.isnumeric():
                    if num in s1:
                        print(f"seen two numbers in {board[i][j]}")
                        return False
                    s1.add(num)
                elif j < 6 and num.isnumeric():
                    if num in s2:
                        print(f"seen two numbers in {board[i][j]}")
                        return False
                    s2.add(num)
                elif num.isnumeric():
                    if num in s3:
                        print(f"seen two numbers in {board[i][j]}")
                        return False
                    s3.add(num)
                print(s1, s2, s3)
        return True
        