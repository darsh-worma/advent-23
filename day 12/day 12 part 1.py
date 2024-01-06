def main():
    condition_records = []
    accounts = []
    file = open("data.txt", 'r')
    lines = file.readlines()
    for line in lines:
        condition_records.append(line.split(' ')[0])
        account = []
        i = 0
        while (i < len(line.split(' ')[1].strip('\n'))):
            account.append(((line.split(' ')[1].strip('\n'))).split(',')[i])
            i += 2
        accounts.append(account)
        

    print(condition_records, accounts)

if __name__ == "__main__":
    main()