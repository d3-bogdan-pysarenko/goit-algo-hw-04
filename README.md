# goit-algo-hw-04
Homework 4

## Висновок:

Для виконання цього практичного завдання я створював масиви різної величини (від 10 до 10000) у 3х різних варіаціях, а саме:
- масив з рандомним розсташуванням чисел;
- масив, де числа вже відсортовані по зростанню;
- масив, де числа відсортовані по спаданню (обернений відсортований);

Після цього здійснювалося вимірювання СЕРЕДНЬОГО часу (базуючись на основі 3х запусків), необхідного для виконання операції сортування наступними методами:
- вставками (insertion);
- злиттям (merge);
- Timsort (дефолтним sorted(arr) )

### Отримавши результати, можу зазначити наступне:

- Сортування вставками працює добре лише на дуже маленьких масивах. На масивах, що більші за 5000 елементів сортування вставками працює занадто повільно у вападках, коли масив не є відсортованим до цього.
Приклади замірів часу для методу вставки(Insertion):
```bash
=== n = 10 ===

-- dataset: random --
Insertion sort: 0.000005 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000002 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.000006 s (avg per run)

=== n = 5000 ===

-- dataset: random --
Insertion sort: 0.445827 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000472 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.856307 s (avg per run)

```

- Сортування злиттям має стабільну складність O(n log n), але потребує додаткової пам’яті та повільніше за Timsort на реальних даних.

- Timsort — це гібрид, який поєднує сортування вставками для малих фрагментів і злиття впорядкованих блоків, що дозволяє використовувати вже існуючі впорядковані ділянки масиву та робить його надзвичайно ефективним.

## Фінальний висновок:

Емпіричні вимірювання показують, що вбудований Timsort у Python значно швидший за реалізації “з нуля”. 
Тому вважаю, що вже "готові і популярні" рішення стандартного стартування скоріш за все будуть ефективніші за власнонаписані, а також не потребуватимуть витрат часу на їх реалізацію.

### Повна таблиця результатів порівняння типів сортування: 

```bash
=== n = 10 ===

-- dataset: random --
Insertion sort: 0.000005 s (avg per run)
Merge sort:     0.000015 s (avg per run)
Timsort:        0.000001 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000002 s (avg per run)
Merge sort:     0.000010 s (avg per run)
Timsort:        0.000001 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.000006 s (avg per run)
Merge sort:     0.000010 s (avg per run)
Timsort:        0.000001 s (avg per run)

=== n = 100 ===

-- dataset: random --
Insertion sort: 0.000239 s (avg per run)
Merge sort:     0.000128 s (avg per run)
Timsort:        0.000005 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000010 s (avg per run)
Merge sort:     0.000148 s (avg per run)
Timsort:        0.000003 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.000554 s (avg per run)
Merge sort:     0.000208 s (avg per run)
Timsort:        0.000006 s (avg per run)

=== n = 500 ===

-- dataset: random --
Insertion sort: 0.010076 s (avg per run)
Merge sort:     0.000629 s (avg per run)
Timsort:        0.000040 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000058 s (avg per run)
Merge sort:     0.001726 s (avg per run)
Timsort:        0.000016 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.014287 s (avg per run)
Merge sort:     0.001329 s (avg per run)
Timsort:        0.000030 s (avg per run)

=== n = 1000 ===

-- dataset: random --
Insertion sort: 0.022890 s (avg per run)
Merge sort:     0.001429 s (avg per run)
Timsort:        0.000078 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000087 s (avg per run)
Merge sort:     0.001052 s (avg per run)
Timsort:        0.000009 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.042461 s (avg per run)
Merge sort:     0.000960 s (avg per run)
Timsort:        0.000008 s (avg per run)

=== n = 2000 ===

-- dataset: random --
Insertion sort: 0.100501 s (avg per run)
Merge sort:     0.003137 s (avg per run)
Timsort:        0.000197 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000165 s (avg per run)
Merge sort:     0.009152 s (avg per run)
Timsort:        0.000060 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.180581 s (avg per run)
Merge sort:     0.002028 s (avg per run)
Timsort:        0.000018 s (avg per run)

=== n = 5000 ===

-- dataset: random --
Insertion sort: 0.445827 s (avg per run)
Merge sort:     0.008508 s (avg per run)
Timsort:        0.000548 s (avg per run)

-- dataset: sorted --
Insertion sort: 0.000472 s (avg per run)
Merge sort:     0.007195 s (avg per run)
Timsort:        0.000061 s (avg per run)

-- dataset: reversed --
Insertion sort: 0.856307 s (avg per run)
Merge sort:     0.008669 s (avg per run)
Timsort:        0.000062 s (avg per run)

=== n = 10000 ===

-- dataset: random --
Insertion sort: skipped (n too large)
Merge sort:     0.022108 s (avg per run)
Timsort:        0.001198 s (avg per run)

-- dataset: sorted --
Insertion sort: skipped (n too large)
Merge sort:     0.013117 s (avg per run)
Timsort:        0.000085 s (avg per run)

-- dataset: reversed --
Insertion sort: skipped (n too large)
Merge sort:     0.012929 s (avg per run)
Timsort:        0.000088 s (avg per run)
```