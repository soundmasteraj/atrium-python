import json

class Account:
    apr = None
    apy = None
    available_balance = None
    available_credit = None
    balance = None
    created_at = None
    credit_limit = None
    day_payment_is_due = None
    guid = None
    institution_code = None
    interest_rate = None
    is_closed = None
    last_payment = None
    last_payment_at = None
    matures_on = None
    member_guid = None
    minimum_balance = None
    minimum_payment = None
    name = None
    original_balance = None
    payment_due_at = None
    payoff_balance = None
    started_on = None
    subtype = None
    total_account_value = None
    type = None
    updated_at = None
    user_guid = None

    def __init__(self, response):
        self.apr = response["apr"]
        self.apy = response["apy"]
        self.available_balance = response["available_balance"]
        self.available_credit = response["available_credit"]
        self.balance = response["balance"]
        self.created_at = response["created_at"]
        self.credit_limit = response["credit_limit"]
        self.day_payment_is_due = response["day_payment_is_due"]
        self.guid = response["guid"]
        self.institution_code = response["institution_code"]
        self.interest_rate = response["interest_rate"]
        self.is_closed = response["is_closed"]
        self.last_payment = response["last_payment"]
        self.last_payment_at = response["last_payment_at"]
        self.matures_on = response["matures_on"]
        self.member_guid = response["member_guid"]
        self.minimum_balance = response["minimum_balance"]
        self.minimum_payment = response["minimum_payment"]
        self.name = response["name"]
        self.original_balance = response["original_balance"]
        self.payment_due_at = response["payment_due_at"]
        self.payoff_balance = response["payoff_balance"]
        self.started_on = response["started_on"]
        self.subtype = response["subtype"]
        self.total_account_value = response["total_account_value"]
        self.type = response["type"]
        self.updated_at = response["updated_at"]
        self.user_guid = response["user_guid"]
