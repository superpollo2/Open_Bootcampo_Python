from datetime import datetime, time, timedelta


def go_home():
    time_now = datetime.now()
    print(time_now)
    current_time = time_now.time()
  
    time_to_go = time(19,00,00)

    
    if  current_time > time_to_go  : return ("tiempo de ir a casa")
    return (f'Oh no, aun faltan { timedelta(hours=19,minutes=00) - timedelta(hours = current_time.hour, minutes=current_time.minute)}')
    
def main ():
    print(go_home())
    

if __name__ == '__main__':
    main()