# Rayan Miah - Project Work Diary

This is a diary of when I do work and what I did on those days.

## 13/10/2022:
Today I worked on a proof of concept program where I make a menu GUI that allows for the user to go to different pages and back to the main menu. There were a lot of examples and ways to 
do this online, so I just had to find an OOP approach on the problem. The code works by creating a single window with lots of different frames, these frames are then brought up to the top 
when needed. The frames are just the different menu pages which are created in their own classes. The menu is very bare bones at the moment in terms of aesthetics, 
I will make it look nicer next time.

## 20/10/2022:
Today I got an implementation of 2048 using a matrix and matrix functions for the moves, I took this example from the internet but I plan to try my own implementation for the game 
in the time frame that I have to complete the game. The implementation that I try myself will include the GUI for the game. There were a few problems with the code 
I took from the internet that I fixed, for example there was a problem where the code would get stuck in an infinite loop.

## 09/11/2022:
I have been very busy for a couple weeks and had to put the project back. I'm back to being able to work on it again now though. Today I realised that I had a problem with my game
where if you made a move that would not change the grid at all, the game would still add in an extra tile, this shouldn't be the case. I spent a lot of my time today revising
for another assignment but I managed to fix this problem quite quickly. I compared the matrix before the move and after, if they were not the same the code would continue
and if they were it would loop back to the move selection.

## 13/11/2022:
I have started reading up on and researching different AI algorithm methods for solving the game such as minimax and more preferably expectimax.

## 17/11/2022:
Carried on researching more into expectimax as this will be a focus of my interim review report. Also looked more into the practical side of things like how to implement it
into the game itself.

## 20/11/2022:
Started implementing the expectimax algorithm, I think I've got the base theory code down for it to work but I am running into problems with it actually running. I think it may
be because the implementation of the 2048 game that I have doesn't actually use OOP. If i can't fix it tomorrow I will probably re-write the major parts of the game to work
with OOP instead. I don't really want to have to do this but if I can't fix it I will have to, besides the code will be better off in OOP.

## 21/11/2022:
### Part 1:
Carried on working on my expectimax algorithm. I ended up having to re-write a lot of my code to change it to OOP. This change however was something I should have started
with. It made my code a lot easier to work with, and the problems I was having yesterday are not present anymore. I stubbornly tried to implement the algorithm without it
because my game didn't use it either. Right now, I only have one heuristic implemented which is the weight matrix and this alone isn't actually enough for the AI to reach
the 2048 tile, the highest it got in the few runs I did was 1024. I plan to implement more heuristics to improve the performance of the AI. I will add in a simple heuristic 
of getting bonuses for empty squares as that would be relatively easy to implement. Also the performance of the AI speed wise isn't the greatest at the moment.
If the depth of the search is less than 6 it runs decently fast and if lower than 5, it is incredibly fast. However I would like my AI to run at a depth search of
8 when close to losing and 6 default. I will need to find a way to optimise it if I want that.

### Part 2:
I added the open squares heuristic and I wasn't too sure how large of a bonus to add to it at the start. I started by multiplying the score by 1.5 for each empty square,
but this turned out to be too much as the AI wouldn't keep to the weighted matrix as much which is essential for high scores. I ended up just making it add a flat score
of 10 for each empty square, this however is still not enough for the AI to even win the game. I have either got the scoring wrong for the heuristics or I simply need 
to add more.

### Part 3:
I added another heuristic which was just a score add from the value of the highest tile, this makes it so moves where the highest tile gets merged are good moves for the AI.
I also changed the bonus for empty squares to just add to the score instead of penalising. I added weights to all of the heuristics so I can change how much they should be 
scoring in relation to each other as well. The AI managed to hit 2048 once in my most recent run but it still takes a long time for it to get there. I need to add some sort
of optimisation into the code as this will also allow me to up the depth of the search from 4 and 7. I was thinking of figuring out a way to implement a transposition table
so the search terminates if getting to a game state it has already seen.

## 22/11/2022:
Implemented the GUI for the game from a source online. This is just a temporary GUI since I wanted one in there at least so I didn't have to keep looking at the console 
representation of the game when I watched the AI play. Will replace this GUI with my own version and implement it into the menu system. Eventually I want the menu to have
options of whether you want to play yourself or if you want the AI to play the game. Also need to make the GUI work with arrow keys when on the player option. Would also like
to have options in the AI menu for changing the depth search etc. I will probably work on this after the interim review as it's not the most important thing right now. I need
to update the heuristics of my AI and it's optimisation to make reaching 2048 much more likely.

## 13/01/2023:
Started looking into ways to improve the optimisation of the algorithm including multithreading and did some small updates on the readme. Will start implementation of the optimisation and work on improving the heuristics so the AI can beat the game more often, eventually I would like the AI to be able to beat the game at 100% efficiency.

## 22/01/2023:
Haven't been working on the project as I've been busy getting into a rhythm with the new modules this term. The first thing I plan to do, is combine all of my proof of concept programs
into one program and make it work that way. This will require some changing around of certain things, for example, I will need to update the 'player plays' version of the game
so that it works with the GUI and uses events to wait for key presses rather than having to press enter. Incorporating both the GUIs into the menu program shouldn't be too 
difficult but I may run into problems with how my menu code is structured. After this, I will get to testing more heuristics and trying to add multithreading.

## 27/01/2023:
Spent a while joining up all my proof of concepts into one final program. This took longer than expected as I had to mess around with my menu program to make it work with the AI
GUI. There were problems with the buttons not working because the game loops until it loses and widgets appearing all over each other. These are all fixed now, I have yet to
complete the GUI for the 'player plays' version of the game but this shouldn't take long as it is nearly identical to the AI version with just a few changes.

## 04/02/2023:
Started implementing multithreading with the hopes of speeding up the game by a large magnitude, this would then let me increase the search depth of the game resulting in
higher scores. Had some trouble implementing it but I managed to get a version that doesn't output any errors. However, the multithreading that I have implemented is
much slower than the non-MT version. Clearly something has gone wrong, and I must've made a mistake somewhere. I will continue working on this and try to fix the problems
as it is my main priority for the project right now.

## 12/02/2023:
Carried on working on the multithreading. After further testing it seems that my implementation has actually worked when using searches deeper than 5. On the normal version
a depth of 6 takes around 30 seconds per move, while with the multithreading it takes around 7 seconds. This is a big improvement and shows that the multithreading is working but
I would like the each move to be under a second. I'm not sure if this is possible with multithreading anymore since I am using all 6 cores I have available. However, I still believe
there is improvement to be made on my implementation. Another option is to reduce the amount of game states that are searched through, for example if the program is
searching through duplicate game trees, these can be removed. I'm not sure if this is possible with expectimax but I will look into it. Also changed up the weight matrix
to create a more snake like pattern that the AI should aim for, this seems to have improved the general performance of the AI.

## 18/02/2023:
Cleaned up the final code and merged my multithreading branch back into the main branch. I changed up the GUI for the 'AI plays' game to make it so the user has an option to change 
between normal and fast mode. The normal mode takes advantage of the multithreading and searches at a depth of 5. The fast mode does not use multithreading and searches at a depth
of 4, the reason it does not use multithreading for this depth is because it is faster without it then with it, I think this may be because of the overhead that comes with the
multithreading so there isn't much point to it at lower depths. Both of the modes have a corresponding button and can be changed during the game, there is no need to wait
until the game is over. I also completed the 'player plays' version of the game and implemented it into the GUI. This was a little bit tricky since I had trouble figuring out
how to use events that wait for key presses inside of the class frame system I had used for my GUI. I eventually got it though and now the game is fully functioning for the player.
Both these modes can be played from the program now and it is even possible to switch to the 'player plays' version while the AI version runs in the background. The final thing
I feel like I need in my program is just to improve my heuristics now as the AI still makes dumb moves that gets itself to lose every now and then. If I can iron these problems
out the AI should succeed at getting a winning score 9/10 times.

## 10/03/2023:
Cleaned up the GUI even more and added an extra option for the user where they can select an 'optimal' mode, this mode changes the depth on the fly to speed through the easier
parts and then slow down when the game gets difficult for the AI. I also added in an extra heuristic that penalises the AI for game states that aren't very smooth (
neighbouring tiles aren't equal to each other). Also added in a very simple data file where the score and highest tile are written to when the game ends, I did this so I have
some data that I can use to show the performance of different modes and put them in my final report.

It is later in the day, and I have gathered more data on the AI. I tried 15 runs on the fast(depth of 4) setting for both the monotonic weight grid and the snake weight grid. 
The dataset is small but it seems pretty evident that the snake method seems to work better in my case with the AI beating the game 20% of time as opposed to the 0% with the 
other method. Later, I am going to try the same experiment but on both the optimal(depth changes accordingly) and the normal(depth of 5) modes. Hopefully, both modes should 
show better results for each grid type and the monotonic one may end up being better when the game tree search is 4 times as large.

## 13/03/2023:
Tried out some caching in hopes of speeding up the AI, it doesn't seem like it makes much difference though since identical game states don't occur very often. Also messed
around with the heuristic weightings hoping to get the scores that each provide in a much closer range. I still need to experiment more but I feel this will help make
the other heuristics have more impact because currently it seems only the weight matrix is being considered.

## 17/03/2023:
Messed around with the heuristic weighting to try and get better scores. Added a new heuristic that gives the AI either a bonus or a penalty for whenever the top tile
is in the correct spot. Made a version of this for the top 4 tiles and their corresponding spots but it is commented out since I felt that it wasn't performing very
well, maybe with some tweaks it may do better. Commented out the caching for now since I feel that it doesn't really make any impact on the AI since it doesn't occur
very often and when it does it seems to be for the worse not the better. Changed up the empty tiles heuristic to make it more prominent as the game goes on. I may do a few
more changes to the code but nothing major as the deadline is coming up and I have to focus on the report.

## 20/03/2023:
Fixed a small error that may have made some games end early. A lot of my game loops were made so that when there were no empty spaces left the game would end. After some
thinking I realised that this is not always the case, so I swapped them around to use the original loss definition.

## 21/03/2023:
Finalised the code. I cleaned up a lot of the comments in the code. The blocks of code that were techniques I tried to use and decided against have been added into my report. 
Updated the readme for the new code and created a tag release for version 1.0 of my code.

