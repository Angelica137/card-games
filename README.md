# Card Games

Card Games on Exercism's Python Track.


## Accessing elements

Items inside lists (_as well as items in other sequence types `str` & `tuple`_) can be accessed via `0-based index` and _bracket notation_.
 Indexes can be from **`left`** --> **`right`** (_starting at zero_) or **`right`** --> **`left`** (_starting at -1_).


<table>
<tr>
  <td style="vertical-align: top"> index from left ⟹<br><br><br><br><br><br><br></td><td style="vertical-align: middle">

|  0<br>👇🏾 	|  1<br>👇🏾 	|  2<br>👇🏾 	|  3<br>👇🏾 	|  4<br>👇🏾 	|  5<br>👇🏾 	|
|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
|     P    	|     y    	|     t    	|     h    	|     o    	|     n    	|
| 👆🏾<br>-6 	| 👆🏾<br>-5 	| 👆🏾<br>-4 	| 👆🏾<br>-3 	| 👆🏾<br>-2 	| 👆🏾<br>-1 	|
</td><td style="vertical-align: bottom"><br><br><br><br><br>⟸ index from right</td>
</tr>
</table>


```python
>>> breakfast_foods = ["Oatmeal", "Fruit Salad", "Eggs", "Toast"]

# Oatmeal is at index 0 or index -4.
>>> breakfast_foods[0]
'Oatmeal'

>>> breakfast_foods[-4]
'Oatmeal'

# Eggs are at index -2 or 2
>>> breakfast_foods[-2]
'Eggs'

>>> breakfast_foods[2]
'Eggs'

# Toast is at -1
>>> breakfast_foods[-1]
'Toast'
```

A section of the elements inside a `list` can be accessed via _slice notation_ (`<list>[start:stop]`).
 A _slice_ is defined as an element sequence at position `index`, such that `start <= index < stop`.
 _Slicing_ returns a copy of the "sliced" items and does not modify the original `list`.


A `step` parameter can also be used `[start:stop:step]` to "skip over" or filter the `list` elements (_for example, a `step` of 2 will select every other element in the range_):


```python
>>> colors = ["Red", "Purple", "Green", "Yellow", "Orange", "Pink", "Blue", "Grey"]

# If there is no step parameter, the step is assumed to be 1.
>>> middle_colors = colors[2:6]

>>> middle_colors
['Green', 'Yellow', 'Orange', 'Pink']

# If the start or stop parameters are omitted, the slice will
# start at index zero, and will stop at the end of the list.
>>> primary_colors = colors[::3]

>>> primary_colors
['Red', 'Yellow', 'Blue']
```

## Working with lists

The usage of the built-in `sum()` function on a list will return the sum of all the numbers in the list:

```python
>>> number_list = [1, 2, 3, 4]
>>> sum(number_list)
10
```

You can also get the _length_ of a list by using the `len()` function:

```python
>>> long_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
>>> len(long_list)
10
```

Lists can be also combined in various ways:

```python
# Using the plus + operator unpacks each list and creates a new list, but it is not efficient.
>>> new_via_concatenate = ["George", 5] + ["cat", "Tabby"]

>>> new_via_concatenate
['George', 5, 'cat', 'Tabby']

# Likewise, using the multiplication operator * is the equivalent of using + n times.
>>> first_group = ["cat", "dog", "elephant"]
>>> multiplied_group = first_group * 3

>>> multiplied_group
['cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant']
```

Lists supply an _iterator_, and can be looped through/over in the same manner as other _sequence types_.

```python
#  Looping through the list and printing out each element.
>>> colors = ["Orange", "Green", "Grey", "Blue"]

>>> for item in colors:
...     print(item)
...
Orange
Green
Grey
Blue
```

_For a more in-depth explanation, of `loops` and `iterators`, complete the `loops` concept._

[arraylist]: https://beginnersbook.com/2013/12/java-arraylist/
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[dynamic array]: https://en.wikipedia.org/wiki/Dynamic_array
[list]: https://docs.python.org/3/library/stdtypes.html#list
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[set]: https://docs.python.org/3/library/stdtypes.html#set
[slice notation]: https://docs.python.org/3/reference/expressions.html#slicings
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple

## Instructions

Elyse is really looking forward to playing some poker (and other card games) during her upcoming trip to Vegas.
 Being a big fan of "self-tracking" she wants to put together some small functions that will help her with tracking tasks and has asked for your help thinking them through.

## 1. Tracking Poker Rounds

Elyse is especially fond of poker, and wants to track how many rounds she plays - and _which rounds_ those are.
 Every round has its own number, and every table shows the round number currently being played.
 Elyse chooses a table and sits down to play her first round. She plans on playing three rounds.

Implement a function `get_rounds(<round_number>)` that takes the current round number and returns a single `list` with that round and the _next two_ that are coming up:

```python
>>> get_rounds(27)
[27, 28, 29]
```

## 2. Keeping all Rounds in the Same Place

Elyse played a few rounds at the first table, then took a break and played some more rounds at a second table ... but ended up with a different list for each table!
 She wants to put the two lists together, so she can track all of the poker rounds in the same place.

Implement a function `concatenate_rounds(<rounds_1>, <rounds_2>)` that takes two lists and returns a single `list` consisting of all the rounds in the first `list`, followed by all the rounds in the second `list`:

```python
>>> concatenate_rounds([27, 28, 29], [35, 36])
[27, 28, 29, 35, 36]
```

## 3. Finding Prior Rounds

Talking about some of the prior Poker rounds, another player remarks how similarly two of them played out.
 Elyse is not sure if she played those rounds or not.

Implement a function `list_contains_round(<rounds>, <round_number>)` that takes two arguments, a list of rounds played and a round number.
 The function will return `True` if the round is in the list of rounds played, `False` if not:

```python
>>> list_contains_round([27, 28, 29, 35, 36], 29)
True

>>> list_contains_round([27, 28, 29, 35, 36], 30)
False
```

## 4. Averaging Card Values

Elyse wants to try out a new game called Black Joe.
 It's similar to Black Jack - where your goal is to have the cards in your hand add up to a target value - but in Black Joe the goal is to get the _average_ of the card values to be 7.
 The average can be found by summing up all the card values and then dividing that sum by the number of cards in the hand.

Implement a function `card_average(<hand>)` that will return the average value of a hand of Black Joe.

```python
>>> card_average([5, 6, 7])
6.0
```

## 5. Alternate Averages

In Black Joe, speed is important. Elyse is going to try and find a faster way of finding the average.

She has thought of two ways of getting an _average-like_ number:

- Take the average of the _first_ and _last_ number in the hand.
- Using the median (middle card) of the hand.
  
Implement the function `approx_average_is_average(<hand>)`, given `hand`, a list containing the values of the cards in your hand.

Return `True` if either _one_ `or` _both_ of the, above named, strategies result in a number _equal_ to the _actual average_.

Note: _The length of all hands are odd, to make finding a median easier._

```python
>>> approx_average_is_average([1, 2, 3])
True

>>> approx_average_is_average([2, 3, 4, 8, 8])
True

>>> approx_average_is_average([1, 2, 3, 5, 9])
False
```

## 6. More Averaging Techniques

Intrigued by the results of her averaging experiment, Elyse is wondering if taking the average of the cards at the _even_ positions versus the average of the cards at the _odd_ positions would give the same results.
 Time for another test function!

Implement a function `average_even_is_average_odd(<hand>)` that returns a Boolean indicating if the average of the cards at even indexes is the same as the average of the cards at odd indexes.

```python
>>> average_even_is_average_odd([1, 2, 3])
True

>>> average_even_is_average_odd([1, 2, 3, 4])
False
```

## 7. Bonus Round Rules

Every 11th hand in Black Joe is a bonus hand with a bonus rule: if the last card you draw is a Jack, you double its value.

Implement a function `maybe_double_last(<hand>)` that takes a hand and checks if the last card is a Jack (11).
 If the the last card **is** a Jack (11), double its value before returning the hand.

```python
>>> hand = [5, 9, 11]
>>> maybe_double_last(hand)
[5, 9, 22]

>>> hand = [5, 9, 10]
>>> maybe_double_last(hand)
[5, 9, 10]
```

## Source

### Created by

- @itamargal
- @isaacg
- @bethanyg

### Contributed to by

- @valentin-p
- @pranasziaukas# card-games
