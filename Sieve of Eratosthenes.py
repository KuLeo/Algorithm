def sieve_of_eratos(limit: int):
    try:
        a = [True] * limit  # Initialize the primality list
        a[0] = a[1] = False

        for (i, j) in enumerate(a):
            if j:
                print(i)
                for n in range(i*i, limit, i):     # Mark factors non-prime
                    a[n] = False
    except Exception as e:
        print(e)


if __name__ == "__main__":
    sieve_of_eratos(20)
