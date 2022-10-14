
def findtxLogs(file):
    size_of_file = len(file)
    call_list_outgoing = []
    call_list_incoming = []
    call=[]
    received=False
    invite_sip=False
    userAgentCucm=False
    useragentOther=False
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
                        if not useragentOther:
                            # print("Entered")
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
            useragentOther=False
            toWithoutTag=False
        elif got_one:
            call.append(line)
            if "Received:" in line:
                # print("Received found")
                received=True
            if received and "INVITE sip:" in line:
                invite_sip=True
                # print("invite_sip found")
            if "User-Agent:" in line:
                if "CUCM" in line:
                    userAgentCucm=True
                elif ("Cisco-SIPGateway" in line) or ("CVP" in line):
                    # print(line)
                    useragentOther=True
                # else:
                    # print(line)
                # print("userAgentCucm found")
            if "To:" in line and not "tag=" in line:
                toWithoutTag=True 
                # print("toWithoutTag found")
    if received and invite_sip and toWithoutTag:
        if userAgentCucm:
            call_list_outgoing.append(call)
        else:
            if not useragentOther:
                # print("added")
                call_list_incoming.append(call)
    return call_list_outgoing, call_list_incoming   

def extractBasicInfo(call_list, index=0, direction="outgoing"):
    call_details={}
    
    for call in call_list:
        # print(call)
        local_call={}
        for line in call:
            if "From:" in line:
                local_call["from"]=line.split(">")[0].split("<")[-1]
            if "To:" in line:
                local_call["to"]=line.split(">")[0].split("<")[-1]
            if line.find("Channel ID")>0:
                local_call["channel_id"] = line.split()[-1]
            if "Call-ID:" in line:
                local_call["call_id"] = line.strip().split(" ")[-1]
            if "Date:" in line:
                local_call["call_time"]= " ".join(line.strip().split(" ")[1:])

        # local_call["log_time"] = " ".join(call[0].split()[1:4])
        local_call["call_type"] = direction
        
        call_details[index]=local_call
        index +=1
    return call_details

def search_with_call_id(file, call_id):
    call_list = []
    call=[]
    call_id_found=False
    got_one=False
    count_other_lines=0
    for line in file:
        if len(line)>0 and line[0].isnumeric():
            if got_one:
                if call_id_found:
                    call_list.append(call)
                call=[]
                # print("-----New call-------")
                call.append(line)
            else:
                got_one=True
                call.append(line)
            call_id_found=False
        elif got_one:
            call.append(line)
            if "Call-ID:" in line and call_id in line:
                # print("Received found")
                call_id_found=True
            
    if call_id_found:
        call_list.append(call)
    return call_list

def get_ccapi_value(file, call_list):
    ccapi_values=[]
    for call in call_list:
        if len(call[0]) >0:
            try:
                if "xxxxxxxxxxxx" != call[0].split("/")[-4] and call[0].split("/")[-4] not in ccapi_values:
                    ccapi_values.append(call[0].split("/")[-4])
            except:
                pass
    return ccapi_values
def get_dial_peer(res, type="in"): # type = "in" or "out"
    for line in res:
        if "in" in type and "Incoming Dial-peer=" in line:
            # print(res)
            return line.split("=")[1].split(",")[0]
        elif "out" in type and "Outgoing Dial-peer" in line:
            return line.split("=")[-2].split(",")[0]
def get_calling_no(res):
    for line in res:
        if  "Calling Number=" in line:
            return line.split("=")[1].split(",")[0]
def get_disconnect_cause(res):
    for line in res:
        if  "Disconnect Cause" in line:
            return line.split("=")[1].split(",")[0]
def get_disconnect_reason(res):
    got_sent=False
    for line in res:
        if got_sent:
            if len(line)>0:
                return line
        if "Sent:" in line:
            got_sent=True

def getDisconnectMsg(file, call_id):
    # all_msgs = []
    # msg=""
    cause_value="Not Found"
    got_cause=False
    # call_id=["Not Found",]
    contents=[]
    # got_call_id=False
    sent200ok=False
    got_warning=False
    found_id=False
    got_msg=False
    for id in call_id:
        
        for line in file:
            contents.append(line)
            if line[:6].isnumeric():
                got_msg=False
                found_id=False
            if "SIP/Msg/ccsipDisplayMsg:" in line:
                got_msg=True
                contents=[]
            if "SIP/2.0 200 OK" in line:
                got_msg=False
                contents=[]

            if got_msg:
                
                if id in line:
                    found_id=True
                    continue
                if found_id and not got_cause and "cause=" in line:
                    i = line.find("cause=")
                    cause_value = line[i+6:]
                    #print(cause_value)
                    got_cause=True
                    
                    break
                elif found_id and "Warning:" in line:
                    # print("warning found")                
                    got_warning=True
                    found_recieved=False
                    for line in contents:
                        #print(line)
                        if "Received:" in line:
                            found_recieved=True
                            continue
                        if found_recieved and len(line.strip())>0:
                            #print(contents)
                            return line.strip()
                    break
                
        found_sent=False
        for line in contents:
            if "Sent:" in line:
                found_sent=True
                continue
            if "Received:" in line:
                found_sent=True
                continue
            if found_sent and got_cause and len(line.strip())>0:
                #print(contents)
                return line.strip()
    
    return "Not Found"

def get_call_ref(file, ccapi):
    got_one=False
    line_counter=0
    find_string = "callref = "
    # got_call_ref = False
    call_ref=""
    for line in file:
        line_counter += 1
        if ccapi in line and "/CCAPI/ccSaveDialpeerTag:" in line:
            got_one=True
            line_counter=0
        if got_one and line_counter<6:
            if find_string in line:
                loc = line.find(find_string)
                call_ref = line[loc+len(find_string) : ].split(" ")[0]
                # got_call_ref=True
                return call_ref

def get_call_with_lastdigits_of_call_ref(file, call_ref):
    # find_pattern=["TX", "RX"]
    call_ref = call_ref.strip()[-3:]
    # print(call_ref)
    tx_setup=False
    contents=[]
    for line in file:
        if tx_setup:
            if line[:5].isnumeric():
               tx_setup=False 
            else:
                contents.append(line)
        if ("TX" in line or "RX" in line) and "callref =" in line and (line.strip())[-3:] == str(call_ref):
            tx_setup=False
            # print((line.strip())[-3:])
            # print((line.strip())[-3:] == str(call_ref))
            contents.append(line)
            if "TX -> SETUP" in line or "RX <- DISCONNECT" in line:
                tx_setup=True
                # contents.append(line)
    
    return contents










        

            
    # for msg in all_msgs:
    # return call_id







if __name__ == '__main__':
    pass





