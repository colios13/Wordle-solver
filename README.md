# Wordle-solver
A simple script to help you to play wordle

### V1.0
This version permit you to have an help to play wordle, the aim is to be able to solve it in the fastest way possible (not in the minimum number of words).<br />
For that purpose I have chose my own strategy, which is based on three first default word, with the aim is to narrow as much as possible the number of possible word from our dictionnary.<br />
<br />
The first word is "salet" (if "salet" is not accepted there is "slate" as an alternative), I have chosen this word based on an [MIT study](https://news.mit.edu/news-clip/forbes-567) for the first best word to play wordle.<br />
The second word is "opium", I have chosen it myself helped by a precedent version of this script, I pick this one because it have no repeated letters, many vowels, it does not contain letter from our first word and it's a common word.<br />
The third word is chosen by the script at runtime based on a similar process to our second word (more details in comment of the code itself) if you don't change the first two word it will chose "chynd" (as an alternative you can use "angry").<br />
<br />
After that you should past the information you have in "l_know_pos", "l_unknow_pos", "user_chosen_word", according to the comment attached to each variables.<br />
As a result it will give you a list of possible word to chose from, with tips to help you make the best choice!<br />
If it's not the correct word go back to the step just above until you find it, enjoy! :) (do not use in online/offline competition with other players without their consent)

---

As it's the first version of this project, to use this tool you need to make direct modification inside the script, following the process given in this file with help of code comments.
