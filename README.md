### Hexlet tests and linter status:
[![Actions Status](https://github.com/VitalRusinov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VitalRusinov/python-project-49/actions)

### SonarQube
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=VitalRusinov_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=VitalRusinov_python-project-49)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=VitalRusinov_python-project-49)](https://sonarcloud.io/summary/new_code?id=VitalRusinov_python-project-49)

[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-highlight.svg)](https://sonarcloud.io/summary/new_code?id=VitalRusinov_python-project-49)

### Описание.
___
***"Brain Games"*** - набор из 5-ти игр для прокачки мозгов. В каждой игре задаются вопросы, на которые необходимо верно ответить 3 раза. В случае провала, Вам предлагается сыграть снова и игра завершается.

### Игры:
#### ***Brain Even*** - Ответьте "да", если число четное, в противном случае ответьте "нет".
#### ***Brain Calc*** - Какой результат этого выражения?
#### ***Brain GCD*** - Найдите наибольший общий делитель заданных чисел?
#### ***Brain Progression*** - Какого числа не хватает в прогрессии?
#### ***Brain Prime*** - Ответьте "да", если данное число простое. В противном случае ответьте "нет".

#### Вы можете вызвать их с помощью простых команд:
```bash
>> brain-even
>> brain-calc
>> brain-gcd
>> brain-progression
>> brain-prime
```

### :game_die: ***Brain Even***
`brain-even`

Игроку предлагается определить четное число или нечетное, ответив 'yes' или 'no' соответственно.
#### Пример работы:
```bash
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
>> Your answer: no
Correct!

Answer "yes" if the number is even, otherwise answer "no".
Question: 15
>> Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
```

[![asciicast](https://asciinema.org/a/631981.svg)](https://asciinema.org/a/631981)

### :game_die: ***Brain Calc***
`brain-calc`

Игроку предлагается математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ.
#### Пример работы:
```bash
What is the result of the expression?
Question: 35 + 16
>> Your answer: 51
Correct!

Question: 25 * 7
Your answer: 145
>> '145' is wrong answer ;(. Correct answer was '175'.
Let's try again, Xequrt!
```

[![asciicast](https://asciinema.org/a/631980.svg)](https://asciinema.org/a/631980)

### :game_die: ***Brain GCD***
`brain-gcd`

Игроку показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
#### Пример работы:
```bash
Find the greatest common divisor of given numbers.
Question: 25 50
>> Your answer: 25
Correct!

Question: 37 3
>> Your answer: 2
'2' is wrong answer ;(. Correct answer was '1'.
Let's try again, Xequrt!
```

[![asciicast](https://asciinema.org/a/631972.svg)](https://asciinema.org/a/631972)

### :game_die: ***Brain Progression***
`brain-progression`

Игроку показывется ряд чисел, который образует арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.
#### Пример работы:
```bash
What number is missing in the progression?
Question: [23, 28, 33, 38, 43, 48, 53, 58, '..', 68]
>> Your answer: 63
Correct!

Question: ['..', 11, 14, 17, 20, 23, 26, 29, 32, 35]
>> Your answer: 9
'9' is wrong answer ;(. Correct answer was '8'.
Let's try again, Xequrt!
```

[![asciicast](https://asciinema.org/a/631086.svg)](https://asciinema.org/a/631086)

### :game_die: ***Brain Prime***
`brain-prime

Игроку предлагается определить простое число или нет, ответив 'yes' или 'no' соответственно.
#### Пример работы:
```bash
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 6
>> Your answer: no
Correct!

Question: 87
>> Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Xequrt!
```

[![asciicast](https://asciinema.org/a/631196.svg)](https://asciinema.org/a/631196)