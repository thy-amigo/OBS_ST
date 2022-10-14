import sys
# import os

from rx_test import rx_call
from tx_test import tx_call

# total arguments
file=""
n = len(sys.argv)
# print(n)
filename=""
operation_type=""
help=False

def usage():
    print('''
    Below debugs are mandatory for parser to analyze the calls:
    -debug isdn q931
    -debug voice ccapi inout
    -debug ccsip messages

    Also make sure to collect the debugs in buffer ("service sequence-numbers" is must else parser will not work).
    Copy paste below commands on router in global configuration mode (conf t) and then collect debugs for analysis.

    service timestamps debug datetime msec
    service timestamps log datetime msec
    service sequence-numbers
    logging buffered 5000000
    logging rate-limit 10000
    logging queue-limit 100000
    no logging console
    no logging monitor

    Program Usage: \n
    run "logParser" \n
    Parameters:
    -f  filepath
    -c  Select operation type:
            "o" for Outgoing call
            "i" for incoming call
    ''')

def analyze(moreThanOne=False):
    global filename
    global operation_type
    global file
    if (operation_type !="o" and operation_type !="i") or moreThanOne:
        # print(operation_type)
        operation_type = input("Please enter 'o' for outgoing calls and 'i' for incoming calls:")
    if len(file)>0:
        if operation_type=="o":
            call_type = input("Enter 1 for sip-isdn and 2 for sip-sip: ")
            tx_call(file, call_type)


        elif operation_type=="i":
            call_type = input("Enter 1 for isdn-sip and 2 for sip-sip: ")
            rx_call(file, call_type)
        else:
            print("Unknown operation type!!!")
    print("\n\n")




# if n<2:
#     usage()
for i in range(1, n):
    if sys.argv[i] == "-h" or sys.argv[i] == "--h" or sys.argv[i] == "-help" or sys.argv[i] == "--help":
        usage()
        help=True
        break
    if sys.argv[i] == "-c":
        operation_type= sys.argv[i+1].lower()
    if sys.argv[i] == "-f":
        # filename = sys.argv[i+1]
        i+=1
        while(i< n and sys.argv[i][0]!="-"):
            filename = filename + " "+ sys.argv[i]
            # print(filename)
            # print(i)
            i += 1
        i-=2
        filename = filename.strip()
    
if not help:
    print('''
    #######################################################################
                     Cisco Voice Gateway/CUBE Log Parser
    #######################################################################
    ''')
    prereq = input("Press p to see mandatory pre-requisite to run the program or press any other key to continue: ")
    if prereq.strip()=="p":
        usage()
    if len(filename)<1:
        filename = input("Please enter log file path: ")
    

    try:
        if (filename[0]=="'" and filename[-1]=="'") or (filename[0]=='"' and filename[-1]=='"'):
            filename = filename[1:-1]
        # print(filename)
        file = open(filename, "r").read().split("\n")
    except:
        print("Error reading file. Please check if correct filepath is provided!!!")
        filename=""
        try:
            filename = input("Please enter log file path: ")
            if (filename[0]=="'" and filename[-1]=="'") or (filename[0]=='"' and filename[-1]=='"'):
                filename = filename[1:-1]
            # print(filename)
            file = open(filename, "r").read().split("\n")
        except:
            print("Error reading file. Please check if correct filepath is provided!!!")
            filename=""
    

    if len(filename)>0:

        analyze()
        while(1):
            userInput = input("Enter 1 to run analysis for this file again or press any other key to exit: ")
            if userInput.strip()=="1":
                analyze(moreThanOne=True)
            else:
                break
        
    
    # os.system("pause")