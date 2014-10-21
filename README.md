rpsls
=====

Rock Paper Scissors Lizard Spock

An assignment from [An Introduction to Interactive Python](https://class.coursera.org/interactivepython-005) on Coursera. 

<div>
     <h2> Mini-project description — Rock-paper-scissors-lizard-Spock </h2>

    <p>Rock-paper-scissors is a hand game that is played by two people. The players
        count to three in unison and simultaneously "throw” one of three
        hand signals that correspond to rock, paper or scissors. The winner is
        determined by the rules:</p>
    <ul>
        <li>Rock smashes scissors</li>
        <li>Scissors cuts paper</li>
        <li>Paper covers rock</li>
    </ul>
    <p>Rock-paper-scissors is a surprisingly popular game that many people play
        seriously (see the <a href="http://en.wikipedia.org/wiki/Rock_paper_scissors" target="">Wikipedia article</a> for details). Due to the fact that a tie
        happens around 1/3 of the time, several variants of Rock-Paper-Scissors
        exist that include more choices to make ties less likely.</p>
    <p>Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors
        that allows five choices. Each choice wins against two other choices, loses
        against two other choices and ties against itself. Much of RPSLS's popularity
        is that it has been featured in 3 episodes of the TV series "The Big Bang
        Theory". The <a href="http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock" target="">Wikipedia entry</a> for RPSLS gives the complete description of
        the details of the game.</p>
    <p>In our first mini-project, we will build a Python function <code>rpsls(name)</code> that
        takes as input the string <code>name</code>, which is one of <code>"rock"</code>, <code>"paper"</code>, <code>"scissors"</code>, <code>"lizard"</code>,
        or <code>"Spock"</code>. The function then simulates playing a round of
        Rock-paper-scissors-lizard-Spock by generating its own random choice from
        these alternatives and then determining the winner using a simple rule
        that we will next describe.</p>
    <p>While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically
        determine who wins a round of RPSLS, coding up these rules would require
        a large number (5x5=25) of <code>if</code>/<code>elif</code>/<code>else</code> clauses
        in your mini-project code. A simpler method for determining the winner
        is to assign each of the five choices a number:</p>
    <ul>
        <li>0 — rock</li>
        <li>1 — Spock</li>
        <li>2 — paper</li>
        <li>3 — lizard</li>
        <li>4 — scissors</li>
    </ul>
    <p>In this expanded list, each choice wins against the preceding two choices
        and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).</p><p>In all of the mini-projects
        for this class, we will provide a walk through of the steps involved in
        building your project to aid its development. A template for your mini-project
        is <a href="http://www.codeskulptor.org/#examples-rpsls_template.py" target=""><b>available here</b></a>.
        Please work from this template.</p>
     <h3> Mini-project development process </h3>

    <ol>
        <li>Build a helper function <code>name_to_number(name)</code> that converts
            the string <code>name</code> into a number between 0 and 4 as described above.
            This function should use a sequence of <code>if</code>/<code>elif</code>/<code>else</code> clauses.
            You can use conditions of the form <code>name == 'paper'</code>, etc. to
            distinguish the cases. To make debugging your code easier, we suggest including
            a final <code>else</code> clause that catches cases when <code>name</code> does
            not match any of the five correct input strings and prints an appropriate
            error message.  You can test your implementation of <code>name_to_number()</code> using this
<a href="http://www.codeskulptor.org/#examples-name_to_number_template.py" target="">name_to_number testing template</a>. (Also available in the Code Clinic tips thread). </li>
        <li>Next, you should build a second helper function <code>number_to_name(number)</code> that
            converts a number in the range 0 to 4 into its corresponding name as a
            string. Again, we suggest including a final <code>else</code> clause that
            catches cases when <code>number</code> is not in the correct range.
You can test your implementation of <code>number_to_name()</code> using this
<a href="http://www.codeskulptor.org/#examples-number_to_name_template.py" target="">number_to_name testing template</a>.

</li>
        <li>Implement the first part of the main function <code>rpsls(player_choice)</code>.  Print out a blank line (to separate consecutive games) followed by a line with an appropriate message describing the player's choice.  Then compute the
             number <code>player_number</code> between
            0 and 4 corresponding to the player's choice by calling the helper function <code>name_to_number()</code>  using <code>player_choice</code>.</li>
        <li>Implement the second part of <code>rpsls()</code> that generates the computer's guess and prints out an appropriate message for that guess. In particular, compute a random number <code>comp_number</code> between 0 and 4 that corresponds to the computer's guess using the function <code>random.randrange()</code>.
            We suggest experimenting with <code>randrange</code> in a separate CodeSkulptor
            window before deciding on how to call it to make sure that you do not accidently
            generate numbers in the wrong range.  Then compute the name <code>comp_choice</code> corresponding to the computer's number using the function <code> number_to_name()</code> 
            and print an appropriate message with the computer's choice to the console. </li>
        <li>Implement the last part of <code>rpsls()</code> that determines and prints
            out the winner. Specifically, compute the difference between <code>comp_number</code> and <code>player_number</code> taken modulo five.  
            Then write an <code>if/elif/else</code> statement whose conditions test the various possible values of this difference and then prints an appropriate message concerning the winner.
            If you have trouble deriving the conditions for the clauses of this <code>if/elif/else</code> statement, we suggest reviewing the "RPSLS" video which describes a simple test for determine the winner of RPSLS.</li>

    </ol>
    <p>This will be the only mini-project in the class that is not an interactive
        game. Since we have not yet learned enough to allow you to play the game
        interactively, you will simply call your
<code>rpsls</code> function repeatedly
        in the program with different player choices. You will see that we have
        provided five such calls at the bottom of the template. Running your program
        repeatedly should generate different computer guesses and different winners
        each time. While you are testing, feel free to modify those calls, but
        make sure they are restored when you hand in your mini-project, as your
        peer assessors will expect them to be there.</p>
    <p>The output of running your program should have the following form:</p>
<pre>Player chooses rock
Computer chooses scissors
Player wins!

Player chooses Spock
Computer chooses lizard
Computer wins!

Player chooses paper
Computer chooses lizard
Computer wins!

Player chooses lizard
Computer chooses scissors
Computer wins!

Player chooses scissors
Computer chooses Spock
Computer wins!
</pre>

    <p>Note that, for this initial mini-project, we will focus only on testing
        whether your implementation of <code>rpsls()</code> works correctly on valid
        input.</p>
     <h3> Grading rubric — 18 pts total (scaled to 100 pts) </h3>

    <p>Your peers will assess your mini-project according to the rubric given
        below. To guide you in determining whether your project satisfies each
        item in the rubric, please consult the video that demonstrates our implementation
        of "Rock-paper-scissors-lizard-Spock". Small deviations from the textual
        output of our implementation are fine. You should avoid large deviations
        (such as using the Python function <code>input</code> to input your guesses).
        Whether moderate deviations satisfy an item of the grading rubric is at
        your peers' discretion during their assessment.</p>
    <p>Here is a break down of the scoring:</p>
    <ul>
        <li>2 pts — A valid CodeSkulptor URL was submitted. Give no credit if solution
            code was pasted into the submission field. Give 1 pt if an invalid CodeSkulptor
            URL was submitted.</li>
        <li>2 pts — Program implements the function <code>rpsls()</code> and the helper
            function&nbsp;<code>name_to_number()</code> with plausible code. Give partial
            credit of 1 pt if only the function <code>rpsls()</code> has plausible code.</li>
        <li>1 pt — Running program does not throw an error.</li>
        <li>1 pt — Program prints blank lines between games.</li>
        <li>2 pts — Program prints <code>"Player chooses player_choice"</code> where <code>player_choice</code> is
            a string of the form <code>"rock"</code>, <code>"paper"</code>, <code>"scissors"</code>, <code>"lizard"</code> or <code>"Spock"</code>.
            Give 1 pt if program prints out number instead of string.</li>
        <li>2 pts — Program prints <code>"Computer chooses comp_choice"</code> where <code>comp_choice</code> is
            a string of the form <code>"rock", "paper", "scissors", "lizard"</code> or <code>"Spock"</code>.
            Give 1 pt if program prints out number instead of string.</li>
        <li>1 pt — Computer's guesses vary between five calls to <code>rpsls()</code> in
            each run of the program.</li>
        <li>1 pt — Computer's guesses vary between runs of the program.</li>
        <li>3 pts — Program prints either <code>"Player and computer tie!"</code>, <code>"Player wins!"</code> or <code>"Computer wins!"</code> to
            report outcome. (1 pt for each message.)</li>
        <li>3 pts — Program chooses correct winner according to RPSLS rules. Please
            manually examine 5 cases for correctness. If all five cases are correct,
            award 3 pts; four cases correct award 2 pts; one to three cases correct
            award 1 pt; no cases correct award 0 pts.</li>
    </ul>
</div>
