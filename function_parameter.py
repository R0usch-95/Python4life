def vote():
    age=float(input("enter : "))
    is_age=18
    if age < is_age:
        print("you are not eligible for voting")
    else:
        print("you are eligible for voting ")
        party_name = input("enter your vote: ")
        election_party=["BJP","INC","SS","AAP"]
        for party in election_party:
            if party_name is party:
                count = 0
                count+=count
                BJP_total_vote = count
                #return BJP_total_vote
                print("total vote of BJP : ", BJP_total_vote)

            elif party_name is party:
                count = 0
                count+=count
                INC_total_vote = count
                #return INC_total_vote
                print("total vote of BJP : ",INC_total_vote)

            elif party_name is party:
                count = 0
                count += count
                SS_total_vote = count
                #return SS_total_vote
                print("total vote of BJP : ",SS_total_vote)

            elif party_name is party:
                count = 0
                count+=count
                AAP_total_vote = count
                #return AAP_total_vote
                print("total vote of BJP : ", AAP_total_vote)

            else:
                print("thank you for visiting")
vote()






