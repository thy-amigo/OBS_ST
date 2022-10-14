# from typing import Container

def getCausevalue(file, call_id):
    cause_value=None
    call_id_found=False
    got_msg=False
    for id in call_id:
        for line in file:
            # if got_cause and got_call_id:
            #     return cause_value, call_id
            # contents.append(line)
            if line[:6].isnumeric():
                got_msg=False
                # if len(msg) > 0 :
                #     all_msgs.append(msg)
                # msg=""
            if  "SIP/Msg/ccsipDisplayMsg:" in line:
                got_msg=True
                cause_value=None
                call_id_found=False
                # contents=[]
            if got_msg:
                if  call_id_found and "cause=" in line:
                    i = line.find("cause=")
                    cause_value = line[i+6:]
                    return cause_value
                if id in line:
                    call_id_found=True

    return cause_value

def getCallAndCauseValue(file, cv_value, get_all_lines=False):
    # all_msgs = []
    # msg=""
    cause_value="Not Found"
    got_cause=False
    call_id=["Not Found",]
    # contents=[]
    # got_call_id=False
    got_msg=False
    for line in file:
        # if got_cause and got_call_id:
        #     return cause_value, call_id
        # contents.append(line)
        if line[:6].isnumeric():
            got_msg=False
            # if len(msg) > 0 :
            #     all_msgs.append(msg)
            # msg=""
        if cv_value in line and "SIP/Msg/ccsipDisplayMsg:" in line:
            got_msg=True
            # contents=[]
        if got_msg:
            if not got_cause and "cause=" in line:
                i = line.find("cause=")
                cause_value = line[i+6:]
                got_cause=True
            if "Call-ID:" in line:   
                if call_id[0] == "Not Found":
                    call_id.remove("Not Found")
                if line.split(" ")[-1] not in call_id:
                    call_id.append(line.split(" ")[-1])
                    # print(call_id)
                # got_call_id = True
    # for msg in all_msgs:
    cause = getCausevalue(file, call_id)
    if cause is not None:
        cause_value=cause

    return cause_value, call_id

def get_call_specific_details(call, file):
    find_step1 = ["RX <- SETUP",]
    call_ref = call["call_ref"]
    got_one=False
    content=[]
    for line in file:
        if not got_one and find_step1[0] in line and call_ref in line:
            got_one=True
            content.append(line)
            continue
        if got_one :
            if line[:6].isnumeric():
                got_one=False
                return content
            content.append(line)
            

def get_contents_with_keys(key, matchtext, file, get_all=False, contains=""):
    # print(key, contains)
    got_one=False
    contains_keyword=False
    search_for_keyword=False
    if len(contains)>0:
        search_for_keyword=True
    content=[]
    content_list=[]
    for line in file:
        if not got_one and (key in line) and (matchtext in line):
            got_one=True
            content.append(line)
            continue
        if got_one :
            if search_for_keyword:
                if contains in line:
                    contains_keyword=True
            if line[:6].isnumeric():
                got_one=False
                if not search_for_keyword and not get_all:
                    return content
                if contains_keyword:
                    contains_keyword=False
                    if not get_all:
                        return content
                    content_list.append(content)
                content=[]

            else:
                content.append(line)
    if search_for_keyword:
        return content_list
    return content
    # for line in file:
    #     if line[:6].isnumeric():
    #         if got_one:
    #             return content
    #         got_one=False
    #         if key in line and matchtext in line:
    #             got_one=True
        
    #     if got_one:
    #         content.append(line)
    # return content

def get_contents_with_multiple_keys(headingkey, file, get_all=True, contains=[]):
    got_one=False
    # print(len(contains))
    contains_keyword = []
    # contains_keyword = contains_keyword + [False]*(len(contains) - len(contains_keyword))
    # count=0
    
    search_for_keyword=False
    if len(contains)>0:
        search_for_keyword = True
        for id in range(len(contains)):
            # print(id)
            contains_keyword.append(False)
    content=[]
    content_list=[]
    for line in file:
        if not got_one and headingkey in line:
            got_one=True
            content.append(line)
            continue
        if got_one :
            if search_for_keyword:
                for id in range(len(contains)):
                    if contains[id] in line:
                        # print(" fount in line: ", line)
                        contains_keyword[id-1]=True
                        # print(contains_keyword)
            if line[:6].isnumeric():
                got_one=False
                if not get_all:
                    return content
                # append_to_list = True
                # for i in contains_keyword:
                #     append_to_list = append_to_list and i
                if not (False in contains_keyword) :     # [append_to_list and i for i in contains_keyword]
                    # contains_keyword = contains_keyword + [False]*(len(contains) - len(contains_keyword))
                    # print(contains_keyword)
                    for id in range(len(contains)):
                        contains_keyword[id] = False
                    
                    content_list.append(content)
                content=[]
                if  headingkey in line:
                    got_one=True
                    content.append(line)
                    continue

            else:
                content.append(line)
    if search_for_keyword:
        return content_list
    return content
    
def get_isdn_info(file, local_call):
    contents = []
    for line in file:
            line = line.strip()
            if "ISDN" in line and ("TX" in line or "RX" in line) and line[-3:]==local_call["call_ref"][-3:]:
                # print(line)
                contents.append(line)
    return contents


def findLogs(file):
    size_of_file = len(file)
    call_list_outgoing = []
    call_list_incoming = []
    call=[]
    received=False
    invite_sip=False
    userAgentCucm=False
    toWithoutTag=False
    got_one=False
    count_other_lines=0
    for line in file:
        if len(line)>0 and line[0].isnumeric():
            if got_one:
                if received and invite_sip and toWithoutTag:
                    if userAgentCucm:
                        call_list_outgoing.append(call)
                    else:
                        call_list_incoming.append(call)
                call=[]
                # print("-----New call-------")
                call.append(line)
            else:
                got_one=True
                call.append(line)
            received=False
            invite_sip=False
            userAgentCucm=False
            toWithoutTag=False
        elif got_one:
            call.append(line)
            if "Received:" in line:
                # print("Received found")
                received=True
            if received and "INVITE sip:" in line:
                invite_sip=True
                # print("invite_sip found")
            if "User-Agent:" in line and "CUCM" in line:
                userAgentCucm=True
                # print("userAgentCucm found")
            if "To:" in line and not "tag=" in line:
                toWithoutTag=True 
                # print("toWithoutTag found")
    if received and invite_sip and toWithoutTag:
        if userAgentCucm:
            call_list_outgoing.append(call)
        else:
            call_list_incoming.append(call)
    return call_list_outgoing, call_list_incoming


def get_rx_call_info(file, find_step1 = ["RX <- SETUP",]):
    # size_of_file = len(file)
    # find_step1 = ["RX <- SETUP",] # "TX -> SETUP"
    # find_step1 = find_item
    call_list = []
    call=[]
    got_one=False
    count_other_lines=0
    for line in file:
        if got_one:
            if len(line)>0 and line[0].isnumeric():
                count_other_lines += 1
            if len(line)>0 and line[0].isnumeric() and count_other_lines==2:
                # print("In if stmt")
                call.append(line)
                got_one=False
                count_other_lines=0
                call_list.append(call)
                call = []
            else:
                # print("In else stmt")
                call.append(line)
                # print(line)
        for step in find_step1:
            if line.find(step)>0:
                # print(line)
                got_one=True
                call=[]
                call.append(line)

    call_details={}
    index=0
    for call in call_list:
        # print(call)
        local_call={}
        for line in call:
            if line.find("Called Party Number")>0:
                local_call["called_number"]=line.split("'")[-2]
            if line.find("Calling Party Number")>0:
                local_call["calling_number"]=line.split("'")[-2]
            if line.find("Channel ID")>0:
                local_call["channel_id"] = line.split()[-1]
                 
        
        local_call["call_ref"]= call[0].rstrip().split(" ")[-1].strip()
        
        local_call["ccapi_value"]=call[-1].split("/")[3].strip()
        # call_time = call[0].split()
        # call_time.remove('')
        # print(temp)
        local_call["time"] = " ".join(call[0].split()[1:4])[1:-1] # call[0].split(" ")[1:4]
        local_call["cause"], local_call["call_id"] = getCallAndCauseValue(file, local_call["ccapi_value"])
        local_call["call_type"] = "incoming"
        
        call_details[index]=local_call
        index +=1
    # print(call_details)
    return call_details

def causeValueAnalysis(cause):
    caluseValueMapping={
        0: "This is usually given by the router when none of the other codes apply." ,

        1 : "Unallocated (unassigned) number." ,

        2 : "No route to specified transit network (national use).",

        3 : "No route to destination.",

        4 : "send special information tone.",

        5 : "misdialed trunk prefix (national use).",

        6 : "channel unacceptable.",

        7 : "call awarded. being delivered in an established channel.",

        8 : "preemption.",

        9 : "preemption : circuit reserved for reuse.",

        16 : "normal call clearing.",

        17 : "user busy.",

        18 : "no user responding.",

        19 : "no answer from user (user alerted).",

        20 : "subscriber absent.",

        21 : "call rejected.",

        22 : "number changed.",

        26 : "non:selected user clearing.",

        27 : "destination out of order.",

        28 : "invalid number format (address incomplete).",

        29 : "facilities rejected.",

        30 : "response to STATUS INQUIRY.",

        31 : "normal. unspecified.",

        34 : "no circuit/channel available.",

        35 : "Call Queued.",

        38 : "network out of order.",

        39 : "permanent frame mode connection out:of:service.",

        40 : "permanent frame mode connection operational.",

        41 : "temporary failure.",

        42 : "switching equipment congestion.",

        43 : "access information discarded.",

        44 : "requested circuit/channel not available.",

        46 : "precedence call blocked.",

        47 : "resource unavailable, unspecified.",

        49 : "Quality of Service not available.",

        50 : "requested facility not subscribed.",

        52 : "outgoing calls barred.",

        53 : "outgoing calls barred within CUG.",

        54 : "incoming calls barred",

        55 : "incoming calls barred within CUG.",

        57 : "bearer capability not authorized.",

        58 : "bearer capability not presently available.",

        62 : "inconsistency in outgoing information element.",

        63 : "service or option not available. unspecified.",

        65 : "bearer capability not implemented.",

        66 : "channel type not implemented.",

        69 : "requested facility not implemented.",

        70 : "only restricted digital information bearer capability is available.",

        79 : "service or option not implemented unspecified.",

        81 : "invalid call reference value.",

        82 : "identified channel does not exist.",

        83 : "a suspended call exists, but this call identify does not. This cause indicates that a call resume has been attempted with a call identity which differs from that in use for any presently suspended call(s).",

        84 : "call identity in use.",

        85 : "no call suspended.",

        86 : "call having the requested call identity has been cleared.",

        87 : "user not a member of CUG.",

        88 : "incompatible destination.",

        90 : "non:existent CUG.",

        91 : "invalid transit network selection (national use).",

        95 : "invalid message, unspecified.",

        96 : "mandatory information element is missing.",

        97 : "message type non:existent or not implemented.",

        98 : "message not compatible with call state or message type non:existent.",

        99 : "Information element / parameter non:existent or not implemented.",

        100 : "Invalid information element contents.",

        101 : "message not compatible with call state.",

        102 : "recovery on timer expiry.",

        103: "parameter non:existent or not implemented : passed on (national use).",

        110: "message with unrecognized parameter discarded.",

        111: "protocol error, unspecified.",

        127: "Intel:working, unspecified.",

    }
    if cause.isnumeric():
        cause=int(cause.strip())
        if cause in caluseValueMapping.keys():
            return caluseValueMapping[cause]
        else:
            return "Unknown cause value"
    else:
        return "Unknown cause value"


if __name__ == '__main__':

    file = open("log_file.txt", "r").read().split("\n") #log_file.txt # debugs.txt
    info = get_rx_call_info(file)
    for index, local_call in info.items():
        print("-------"+str(index+1)+" Of " + str(len(info))+"-------")
        for key, value in local_call.items():
            print(key + " : " , value)
        
    id = input("Enter a ccapi value value to see details: ")
    # print(info.values()[id])
    for index, local_call in info.items():
        # print(len(local_call["call_ref"].lower()))
        if local_call["ccapi_value"].lower() == id.lower().strip() :
            # print()
            details = get_call_specific_details(local_call, file)
            print("----------Details for ccapi value " + id +" ----------")
            print("\n------------Incoming ISDN set up from PTT: ---------------------\n")
            if len(details) <0 :
                print("Not found")
            else:
                for line in details:
                    print(line)
                
            print("\n-----------CCAPI call set up:-----------\n")
            result = get_contents_with_keys(local_call["ccapi_value"],"CCAPI/cc_api_display_ie_subfields", file)
            if len(result) <0:
                print("Not Found")
            else:
                for line in result:
                    print(line)
            result = get_contents_with_keys(local_call["ccapi_value"],"CCAPI/cc_api_call_setup_ind_common", file)
            print("\n-------------Incoming and outgoing dial-peers selected:-------------\n")
            if len(result) <0:
                print("Not Found")
            else:
                for line in result:
                    print(line)
            result = get_contents_with_keys(local_call["ccapi_value"],"SIP/Msg/ccsipDisplayMsg", file)
            print("\n---------------SIP INVITE sent to CUCM:--------------\n")
            if len(result) <0:
                print("Not Found")
            else:
                for line in result:
                    print(line)
            
            result = get_contents_with_keys(local_call["ccapi_value"],"SIP/Msg/ccsipDisplayMsg", file, get_all=True, contains="SIP/2.0 100 Trying")
            print("\n---------------SIP 100 Trying recieved from CUCM:--------------\n")
            if len(result) <0:
                print("Not Found")
            else:
                for r in result:
                    for line in r:
                        print(line)
            
            
            # print("\n---------------FOR call to:--------------\n") 
            print("--------------------- This call consists of ",len(local_call["call_id"]), " SIP dialog ---------")
            for id in local_call["call_id"]:
                result = get_contents_with_multiple_keys("SIP/Msg/ccsipDisplayMsg", file, contains=["To:", id])
                print("-------------------------For call id : " + id, "-------------------------\n")
                if len(result) == 0:
                    print("Not Found")
                else:
                    for item in result:
                        for line in item:
                            print(line)
                            # pass
                        print("\n ------------------------------------------------- \n")
            
            result = get_contents_with_keys(local_call["ccapi_value"],"CCAPI/cc_api_call_digit_begin", file)
            print("\n---------------DTMF digits pressed for this call :--------------\n")
            if len(result) == 0:
                print("Not Found")
            else:
                for line in result:
                    print(line) 
        
            print("\n-----------------ISDN LEG analysis--------------\n")
            result = get_isdn_info(file, local_call)
            if len(result)==0:
                print("Not Found")
            else:
                for line in result:
                    print(line)
            
            
            break
        