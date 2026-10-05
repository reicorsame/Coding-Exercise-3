1. What error occurred when trying to access `atm.__pin` directly?

It gave an `AttributeError` because `__pin` uses name mangling. Python changes its name internally to `_ATM__pin`, so it cannot be accessed directly using `atm.__pin`.


2. How did `@property` help?

`@property` lets us use `account.balance` while keeping `_balance` protected. We can also add validation without changing how the balance is accessed.


3. How did the ATM demonstrate abstraction?

The ATM hides the complicated account operations. Users only need simple methods like `check_balance()`, `perform_deposit()`, and `perform_withdrawal()` without dealing with the actual transaction logic.
