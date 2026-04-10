# COP4533 Programming Assignment 3: Highest Value Longest Common Sequence

## 1. Student Information
**Name:** Justin Lin  
**UFID:** 36425312  



## 2. How to Compile and Run

To run the program use the command from the following command from the project's root directory:
`python3 ./src/main.py ./tests/input/example.in`

"example.in" may be substituted with any of the provided test cases in the `./tests/input` directory
Some examples of commands that are valid could be:
- `python3 ./src/main.py ./tests/input/test1.in`
- `python3 ./src/main.py ./tests/input/test2.in`



## 3. Assumptions

The program assumes the following:

- All character values are **nonnegative integers**  
- The alphabet consists of **distinct characters**  
- Characters in strings `A` and `B` are always present in the given alphabet to value map
- Strings `A` and `B` contain only valid alphabet characters  
- Input format strictly follows the specification  
- Strings may be of different lengths  


## 4. Written Solutions

### Question 1:
![alt text](./data/graph.png)

Since all the test cases used were roughly identical in lengths of their respective A's and B's, this should show us a quadratic growth as the time complexity of the dynamic programming algorithm comes out to O(nm) 

### Question 2:
#### Base Cases:
OPT(0, j) = 0; OPT(i, 0) = 0

#### Recurrence Equation:
![alt text](./data/reccurence_equation.png)

The recurrence is correct because it considers all the possible optimal subsequences by either skipping a character from one of the strings or matching the last chacters if they're equal. Each case would reduce the larger problem into a smaller subproblem to then take the maximum for the maximized solution.


### Question 3:
The runtime of the algorithm is also going to be O(nm)

```
def length(String A, String B, Map v):
    n = length(A)
    m = length(B)

    create Val[0...n][0...m]
    create Len[0...n][0...m]

    for i = 0 to n:
        Val[i][0] = 0
        Len[i][0] = 0

    for j = 0 to m:
        Val[0][j] = 0
        Len[0][j] = 0

    for i = 1 to n:
        for j = 1 to m:

            bestValue = -1
            bestLength = -1

            if Val[i-1][j] > bestValue or (Val[i-1][j] == bestValue and Len[i-1][j] > bestLength):
                bestValue = Val[i-1][j]
                bestLength = Len[i-1][j]

            if Val[i][j-1] > bestValue or (Val[i][j-1] == bestValue and Len[i][j-1] > bestLength):
                bestValue = Val[i][j-1]
                bestLength = Len[i][j-1]

            if A[i] == B[j]:
                val = Val[i-1][j-1] + v(A[i])
                length = Len[i-1][j-1] + 1

                if val > bestValue or (val == bestValue and length > bestLength):
                    bestValue = val
                    bestLength = length

            Val[i][j] = bestValue
            Len[i][j] = bestLength

    return Len[n][m]
```