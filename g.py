class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        if deposit_cents >= 100:
            self.dollars += deposit_dollars + deposit_cents // 100
            if self.cents + deposit_cents % 100 >= 100:
                self.dollars += 1
                self.cents += deposit_cents % 100 - 100
            else:
                self.cents += deposit_cents % 100
        else:
            if self.cents + deposit_cents >= 100:
                self.dollars += deposit_dollars + 1
                self.cents += deposit_cents - 100
            else:
                self.cents += deposit_cents
                self.dollars += deposit_dollars
