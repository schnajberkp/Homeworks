def find_first_and_last(lst):
# () kolem hodnot abych konvertoval do tuple
    return (lst[0], lst[-1])

a = find_first_and_last([1,2,3,4,5,6,7,8,9])
print(a)
# Kontrola jestli jsem opravdu vytvoril Tuple
if isinstance(a, tuple):
    print("Mas to spravne :-)")
#Double kontrola Tuple, nelze menit jeho hodnotu, takze neni pochyb ze mam Tuple
a[3] = 5
