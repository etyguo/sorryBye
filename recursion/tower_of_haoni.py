""" Problem
https://lei-d.gitbook.io/leetcode/recursion/tower-of-hanoi#solution-recursion

[Math, Recursion]
Tower of Hanoi is a mathematical puzzle where we have 3 rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.
Write a program which prints a sequence of operations that move n disks from one rod to another.
"""

"""Solution
so for n-1 we move from 1->2[0], then move N from 1->3[1], then we could repeated the n-1 from 2-3[2]
The boundary condition is n==1 we need to move from 1->3 [4]
"""
def tower_of_haoni_helper(n: int, from_rod: str, aux_rod: str, to_rod: str):
    """
    :param n: total number of plate n left
    :param from_rod: from rod number
    :param to_rod: to rod number
    :return: nothing
    """
    if n == 1:
        print("move", n, "from", from_rod, "to", to_rod) #[4]
        return
    tower_of_haoni_helper(n-1, from_rod, to_rod, aux_rod) #[0]
    print("move",n,"from",from_rod,"to",aux_rod) #[1]
    tower_of_haoni_helper(n-1, aux_rod, from_rod, to_rod) #[2]


def tower_of_haoni(n: int):
    """
    number of plate N

    :return: nothing but print out a shit load of step on how this could be done
    """
    tower_of_haoni_helper(n, "1", "2", "3")

tower_of_haoni(3)

