from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    pass

    HOURLY_WAGE = 12.0

    def calculate_earnings(self):
        earnings = self.hours_worked * self.HOURLY_WAGE
        return earnings

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
