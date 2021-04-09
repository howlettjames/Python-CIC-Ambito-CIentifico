from rational import Rational

def testRational():
    r1 = Rational(3, 2)
    r2 = Rational(1, 2)

    print("NUMBERS")
    print(f"r1 = {r1} and r2 = {r2}\n")
    print("ARITHMETIC OPS")
    print(f"Sum: {r1 + r2}")
    print(f"Sub: {r1 - r2}")
    print(f"Mult: {r1 * r2}")
    print(f"Div: {r1 / r2}")
    print(f"Pow: {r1 ** 2}")
    print()
    print("LOGIC OPS")
    print(f"Is {r1} < {r2} ? {r1 < r2}")
    print(f"Is {r1} <= {r2} ? {r1 <= r2}")
    print(f"Is {r1} == {r2} ? {r1 == r2}")
    print(f"Is {r1} != {r2} ? {r1 != r2}")
    print(f"Is {r1} > {r2} ? {r1 > r2}")
    print(f"Is {r1} >= {r2} ? {r1 >= r2}")

if __name__ == '__main__':
    testRational()