PERCENTAGES = [5, 10, 20]  # Percentages for each bucket
BUCKETS = [[0, 10000], [10000, 20000], [20000, None]]  # Tax brackets
SALARY = 30000
def tax_collector(salary):
    tax = 0
    for i, (lower,upper) in enumerate(BUCKETS):
        rate = PERCENTAGES[i] / 100
        if upper is None:
            tax_collection = max(0, salary - lower)
        else:
            tax_collection = max(0, min(salary,upper) - lower)
        tax += tax_collection * rate

        if upper is not None and salary <= lower:
            break
    return tax

print(tax_collector(SALARY))
print(tax_collector(50000))
print(tax_collector(5000000))