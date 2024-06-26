
# Time Complexity (TC) of Algorithms

| Algorithm  | TC best        | TC average     | TC worst       |
|------------|----------------|----------------|----------------|
| Insertion  | \( n \)        | \( n^2 \)      | \( n^2 \)      |
| Merge      | \( n log n \)  | \( n log n \)  | \( n log n \)  |
| TimSort    | \( n \)        | \( n log n \)  | \( n log n \)  |

## Порівняння алгоритмів сортування 
### Злиттям (Merge Sort), Вставками (Insertion Sort) та вбудованого методу (TimSort)

| List Type        | Number    | Merge Sort Time (seconds) | Insertion Sort Time (seconds) | TimSort Time (seconds) |
|------------------|-----------|---------------------------|-------------------------------|------------------------|
| sorted           | 1000      | 0.000741                  | 0.000099                      | 0.000007               |
| reverse_sorted   | 1000      | 0.000747                  | 0.029618                      | 0.000007               |
| partially_sorted | 1000      | 0.000843                  | 0.003545                      | 0.000057               |
| unsorted         | 1000      | 0.000942                  | 0.012332                      | 0.000108               |

| List Type        | Number    | Merge Sort Time (seconds) | Insertion Sort Time (seconds) | TimSort Time (seconds) |
|------------------|-----------|---------------------------|-------------------------------|------------------------|
| sorted           |  500      | 0.000336                  | 0.000027                      | 0.000004               |
| reverse_sorted   |  500      | 0.000364                  | 0.005126                      | 0.000004               |
| partially_sorted |  500      | 0.000394                  | 0.000865                      | 0.000025               |
| unsorted         |  500      | 0.000466                  | 0.002621                      | 0.000050               |

| List Type        | Number    | Merge Sort Time (seconds) | Insertion Sort Time (seconds) | TimSort Time (seconds) |
|------------------|-----------|---------------------------|-------------------------------|------------------------|
| sorted           |   10      | 0.000006                  | 0.000001                      | 0.000001               |
| reverse_sorted   |   10      | 0.000005                  | 0.000003                      | 0.000000               |
| partially_sorted |   10      | 0.000005                  | 0.000001                      | 0.000000               |
| unsorted         |   10      | 0.000005                  | 0.000002                      | 0.000001               |


### Висновки:
Алгоритм **Merge Sort** стабільно демонструє хороші показники при сортуванні списків незалежно від їхнього первісного стану, завдяки складності \(O(n log n)\). Водночас, **Insertion Sort** виявляється ефективним для вже відсортованих або невеликих масивів, де його лінійний час в найкращому випадку є значною перевагою. **TimSort**, вбудований у Python, демонструє найкращу часову ефективність у всіх тестових сценаріях, що робить його оптимальним вибором для більшості програмних застосувань. Це пояснює, чому програмісти зазвичай віддають перевагу використанню стандартних алгоритмів Python. 

