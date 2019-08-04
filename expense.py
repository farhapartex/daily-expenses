import datetime
from initial import InitialComponent
from cost import CostFunction

# current_date = datetime.datetime.now()
# local_date_time = current_date.strftime("%c")
# print(local_date_time)
# f = open("demo.txt","a")
# dummy_text = input()
# dummy_text += '\n'
# f.write(dummy_text)
# f.close()

if __name__ == "__main__":
    initial = InitialComponent()
    if not initial.check_initial():
        initial.create_initial_setup()
    else:
        cost = CostFunction()
        cost.say_hello()

        while True:
            ask = input("again/done: ")
            if ask == "again":
                print("AGAIN")
            elif ask == "done":
                break  
        
