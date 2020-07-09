## Χρησιμοποιώντας συνάρτηση για να σχεδιάσεις μια νιφάδα χιονιού

Το παραλληλόγραμμό σου για τη νιφάδα χιονιού είναι ωραίο, αλλά δεν μοιάζει με νιφάδα χιονιού όσο θα μπορούσε. Ας το διορθώσουμε!

Για αυτό το σχέδιο, πρέπει να μετακινήσουμε τη χελώνα από το κέντρο του παραθύρου. The `penup()` and `pendown()` instructions let us do this without drawing a line, just like picking up a real pen from the paper and moving it somewhere else to start writing.

- Type the following instructions below the `colours` list:
    
    ```python
    elsa.penup()
    elsa.forward(90)
    elsa.left(45)
    elsa.pendown()
    ```

Ας γράψουμε τον κώδικα για να σχεδιάσουμε έναν κλάδο της νιφάδας χιονιού και να τον αποθηκεύσουμε μέσα σε μια **συνάρτηση**. Στη συνέχεια, μπορείς απλά να το επαναλάβεις ξανά και ξανά για να δημιουργήσεις μια πλήρη νιφάδα χιονιού.

![branch](images/branch.PNG)

- Define a function called `branch` by typing:
    
    ```python
    def branch():
    ```

- Αφαίρεσε τον κώδικα με τους βρόχους για τη νιφάδα χιονιού με σχήμα παραλληλογράμμου. Add the following code indented inside the `branch` function:
    
    ```python
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)
    ```
    
    ** Σημείωση **: Να θυμάσαι ότι η εσοχή είναι σημαντική. Φρόντισε να βεβαιωθείς ότι όλες οι εσοχές σου είναι σωστές, διαφορετικά ο κώδικάς σου δεν θα λειτουργήσει!

- Write a final section of code to **call** the `branch` function (which means to run it) eight times. You can use a loop again as for your last snowflake:
    
    ```python
    for i in range(8):
      branch()
      elsa.left(45)
    ```

- Put a `#` at the start of the `elsa.color(random.choice(colours))` instruction to turn it into a **comment**. Αυτό σημαίνει ότι ο υπολογιστής θα παραλείψει αυτήν τη γραμμή κώδικα. You could delete the line, but you might want to use it to add colour to your snowflake later on.

- Save and run your code, and a snowflake should appear before your eyes!

![](images/snowflake2.png)