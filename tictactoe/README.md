# TicTacToe
---
## Overview
Using Minimax, implement an AI to play Tic-Tac-Toe optimally.

## Algorithm
<a href="https://es.wikipedia.org/wiki/Minimax">Minimax</a> Algorithm in Tic Tac Toe

Knowing based on the state whose turn it is, the algorithm can know whether the current player, when playing optimally, will pick the action that leads to a state with a lower or a higher value. This way, alternating between minimizing and maximizing, the algorithm creates values for 
the state that would result from each possible action. To give a more concrete example, we can imagine that the maximizing player asks at every turn: “if I take this action, a new state will result. If the minimizing player plays optimally, what action can that player take to bring to the lowest value?” However, to answer this question, the maximizing player has to ask: “To know what the minimizing player will do, I need to simulate the same process in the minimizer’s mind: the minimizing player will try to ask: ‘if I take this action, what action can the maximizing player 
take to bring to the highest value?’” This is a recursive process, and it could be hard to wrap your head around it; looking at the pseudo code below can help. Eventually, through this recursive reasoning process, the maximizing player generates 
values for each state that could result from all the possible actions at the current state. After having these values, the maximizing player chooses the highest one.

### Diagram
![alt-text](https://github.com/LeoZorzoli/CS50-AI-2021/blob/main/tictactoe/minimax.png)

