import argparse

from flitton_fib_py.fib_calcs.fib_number import recurring_fibonacci_number


def fib_numb() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--number",
        action="store",
        type=int,
        required=True,
    )

    args = parser.parse_args()

    print("num:", args.number, "result:", recurring_fibonacci_number(args.number))
