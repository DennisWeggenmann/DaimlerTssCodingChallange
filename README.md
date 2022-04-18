# DaimlerTssCodingChallange

## Annahmen
Integer Zahlen

## Lösung
Idee: https://www.geeksforgeeks.org/merging-intervals/#:~:text=A%20simple%20approach%20is%20to,for%20remaining%20intervals%20after%20first.

Sortiert das Input-Array nach dem ersten Index des Intervalls.
Die Intervalle werden eins nach dem anderen zusammengeführt. Wenn sich das aktuelle Intervall in der Eingabeliste und das letzte Intervall der Ergebnissesliste nicht überschneiden, dann wird das aktuelle Intervall von der Eingabe zum Ergebnis hinzugefügt. Andernfalls wird das aktuelle Intervall in das letzte Intervall des Ergebnisses eingefügt.


## Time complexity
Die Sortiermethode braucht O(nlogn) und die for Schleife O(n) also O(nlogn)


## Space Complexity
Im schlimmsten Fall ist die result Liste gleich lang wie die Eingabeliste . Die space complexity ist O(n), wobei n die Länge der Eingabeliste ist.