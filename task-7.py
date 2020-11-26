import json


def main():
    with open('task-7.txt') as fh:
        lines = fh.readlines()

    avg = []
    companies = {}
    for line in lines:
        name, law, income, outcome = [s.strip() for s in line.split()]
        income = int(income)
        outcome = int(outcome)

        profit = income - outcome
        if profit > 0:
            avg.append(profit)

        companies[name] = profit

    ret = [companies, {'average_profit': sum(avg) / len(avg)}]
    print(ret)

    with open('task-7.outout.json', 'w') as fh:
        json.dump(ret, fh, indent=4, ensure_ascii=False)




if __name__ == '__main__':
    main()
