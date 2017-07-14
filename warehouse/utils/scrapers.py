import acc_keys

def budget():
    def pull_budget(name):
        client = boto3.client("sts", aws_access_key_id=acc_keys.acc(), aws_secret_access_key=acc_keys.sec())
        account_id = client.get_caller_identity()["Account"]
        client = boto3.client('budgets', aws_access_key_id=acc_keys.acc(), aws_secret_access_key=acc_keys.sec())
        response = client.describe_budget(
            AccountId=str(account_id),
            BudgetName=str(name)
        )
        return response

    d = datetime.date.today()
    try:
        q = AWS_Budget.objects.get(date=d)
    except:
        budget = pull_budget('Yearly Boston')
        budget = budget['Budget']
        budgetl = budget['BudgetLimit']
        limit = budgetl['Amount']
        name = budget['BudgetName']
        budgetc = budget['CalculatedSpend']
        acctD = budgetc['ActualSpend']
        acct = acctD['Amount']
        forD = budgetc['ForecastedSpend']
        forc = forD['Amount']
        acct = round(float(acct),2)
        forc = round(float(forc),2)
        q = AWS_Budget(budget_name=name, actual_spend=acct, forcasted_spend=forc, limit=limit, date=d)
        q.save()
