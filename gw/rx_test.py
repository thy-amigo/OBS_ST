from .rx_logParser import *
from .tx_logParser import *




def rx_call(file, call_subtype):

    # code = []
    if call_subtype.strip() == "1":
    
        info = get_rx_call_info(file)
        if len(info)==0:
            print("No calls found!")
            
            return "No calls found!"
        
        else:
            
            call_details_filtered={}
            index_i=0
            
            for index, local_call in info.items():
                print("-------"+str(index+1)+" Of " + str(len(info))+"-------")
                # code.append(f"-------"+str(index+1)+" Of " + str(len(info))+"-------")
                result = get_contents_with_keys((local_call["ccapi_value"]),"/CCAPI/cc_api_call_setup_ind_common", file, contains="Incoming Dial-peer")
                # print(result)
                local_call["incoming_dial_peer"]= get_dial_peer(result , type="in")
                result = get_contents_with_keys((local_call["ccapi_value"]),"/CCAPI/ccIFCallSetupRequestPrivate", file, contains="Outgoing Dial-peer")
                local_call["outgoing_dial_peer"] = get_dial_peer(result , type="out")
                local_call["calling_no"] = get_calling_no(file)
                local_call["disconnect_reason"] = getDisconnectMsg(file, local_call["call_id"])
                
                call_details_filtered[index_i]=local_call
                index_i+=1
                # for key, value in local_call.items():
                #     print(key + " : " , value)
                
            return call_details_filtered
        
        

        # if len(info)>0:    
            # id_value = input("Enter a ccapi value value to see details: ")
        # print(info.values()[id])
        
    elif call_subtype.strip()=="2":
        call_list_outgoing, call_list_incoming = findtxLogs(file)
        # print(call_list_incoming)
        # for item in call_list_incoming:
        #     for line in item:
        #         print(line)
        if len(call_list_incoming)<1:
            print("No SIP -SIP call found")            
            # code.append("No SIP -SIP call found")

        # print(call_list_incoming)
        
        else:
            call_details_filtered={}
            index_i=0
            
            # code = []
            
            call_details = extractBasicInfo(call_list_incoming, direction="incoming")
            print("-----------------Details: ---------------------")
            
            for index, local_call in call_details.items():
                print("-------"+str(index+1)+" Of " + str(len(call_details))+"-------")
                # code.append("-------"+str(index+1)+" Of " + str(len(call_details))+"-------")
                                    
                call_by_call_id = search_with_call_id(file, str(local_call["call_id"]))
                ccapi = get_ccapi_value(file, call_by_call_id)
                local_call["ccapi_value"]=ccapi
                for val in ccapi:
                    local_call["call_id"]=[]
                    local_call["cause"], local_call["call_id"] = getCallAndCauseValue(file, val)
                    # print("call ids: ", local_call["call_id"])
                # print(local_call["call_id"])
                call_id_lower=[]
                call_id_upper=[]
                lower=False
                for call in local_call["call_id"]:
                    for c in call:
                        if c.islower():
                            call_id_lower.append(call)
                            lower=True
                            break
                    if not lower:
                        call_id_upper.append(call)
                local_call["call_id"] = call_id_lower + call_id_upper
    
                for val in local_call["ccapi_value"]:
                    local_call["call_ref"] = get_call_ref(file, val)
                # call_details[index]= local_call
                # for key, value in local_call.items():
                #     print(key + " : " , value)
                
                print("\n-----------CCAPI call set up:-----------\n")
                
                # code.append("\n-----------CCAPI call set up:-----------\n")
                
                result = get_contents_with_keys((local_call["ccapi_value"])[0],"/CCAPI/cc_api_call_setup_ind_common", file, contains="Incoming Dial-peer")
                # if len(result) <0:
                #     print("Not Found")
                # else:
                #     for line in result:
                #         print(line)
                local_call["incoming_dial_peer"]= get_dial_peer(result , type="in")
                result = get_contents_with_keys((local_call["ccapi_value"])[0],"/CCAPI/ccIFCallSetupRequestPrivate", file, contains="Outgoing Dial-peer")
                local_call["outgoing_dial_peer"] = get_dial_peer(result , type="out")
                local_call["calling_no"] = get_calling_no(file)
                
                local_call["disconnect_reason"] = getDisconnectMsg(file, local_call["call_id"])
                # result= get_contents_with_keys((local_call["ccapi_value"])[0],"CCAPI/cc_api_call_disconnect_done", file, contains="Outgoing Dial-peer")
                # local_call["disconnect_cause"]= get_disconnect_cause(result)
                # local_call["disconnect_reason"] = get_disconnect_reason(result)
                for key, value in local_call.items():
                    call_details_filtered[index_i]=local_call
                    index_i+=1
                    
                    # if key=="ccapi_value":
                    #     print(key,":",value[0])
                    #     code.append(key,":",value[0])
                        
                    # else:
                    #     call_details_filtered[index_i]=local_call
                    #     index_i+=1
                    #     # print(key + " : " , value)
                        
            return call_details_filtered
                    
def rx_analyse_1(id_value, info, file):
    
    code =[]
    for index, local_call in info.items():
        # print(len(local_call["call_ref"].lower()))
        if local_call["ccapi_value"].lower() == id_value.lower().strip() :
            # # print()
            details = get_call_specific_details(local_call, file)
            print("\n----------Details for ccapi value " + id_value +" ----------")
            print("\n------------Incoming ISDN set up from PTT: ---------------------\n")
            
            code.append("----------Details for ccapi value " + id_value +" ----------")
            code.append("\n------------Incoming ISDN set up from PTT: ---------------------\n")
            
            if len(details) <0 :
                print("Not found")
                code.append("Not found")
                
            else:
                for line in details:
                    print(line)
                    code.append(line)
                
            print("\n-----------CCAPI call set up:-----------\n")
            code.append("\n-----------CCAPI call set up:-----------\n")
            result = get_contents_with_keys(local_call["ccapi_value"],"CCAPI/cc_api_display_ie_subfields", file)
            if len(result) <0:
                print("Not Found")
                code.append("Not found")
            else:
                for line in result:
                    print(line)
                    code.append(line)
                    
            result = get_contents_with_keys(local_call["ccapi_value"],"CCAPI/cc_api_call_setup_ind_common", file)
            print("\n-------------Incoming and outgoing dial-peers selected:-------------\n")
            code.append("\n-------------Incoming and outgoing dial-peers selected:-------------\n")
            
            
            if len(result) <0:
                print("Not Found")
                code.append("Not found")              
                
            else:
                for line in result:
                    print(line)
                    code.append(line)
                    
            print("\n")
            code.append("\n")
            result = get_contents_with_keys(local_call["ccapi_value"],"CCAPI/ccIFCallSetupRequestPrivate:", file,contains="Outgoing Dial-peer=")
            if len(result) <0:
                print("Not Found")
                code.append("Not found")   
                
            else:
                for line in result:
                    print(line)
                    code.append(line)
                    
            # result = get_contents_with_keys(local_call["ccapi_value"],"SIP/Msg/ccsipDisplayMsg", file)
            # print("\n---------------SIP INVITE sent :--------------\n")
            # if len(result) <0:
            #     print("Not Found")
            # else:
            #     for line in result:
            #         print(line)
            
            # result = get_contents_with_keys(local_call["ccapi_value"],"SIP/Msg/ccsipDisplayMsg", file, get_all=True, contains="SIP/2.0 100 Trying")
            # print("\n---------------SIP 100 Trying recieved:--------------\n")
            # if len(result) <0:
            #     print("Not Found")
            # else:
            #     for r in result:
            #         for line in r:
            #             print(line)
            
            
            # print("\n---------------FOR call to:--------------\n") 
            print("\n\n--------------------- This call consists of ",len(local_call["call_id"]), " SIP dialog ---------")
            code.append(f"\n\n--------------------- This call consists of {len(local_call['call_id'])} SIP dialog ---------")
            
            
            for id in local_call["call_id"]:
                result = get_contents_with_multiple_keys("SIP/Msg/ccsipDisplayMsg", file, contains=["To:", id])
                print("\n-------------------------For call id : " + id, "-------------------------\n")
                code.append(f"\n-------------------------For call id :  {id} -------------------------\n")
                
                if len(result) == 0:
                    print("Not Found")
                    code.append("Not found")
                else:
                    for item in result:
                        for line in item:
                            print(line)
                            code.append(line)
                            # pass
                        print("\n ------------------------------------------------- \n")
                        code.append("\n ------------------------------------------------- \n")
            
            result = get_contents_with_keys(local_call["ccapi_value"],"CCAPI/cc_api_call_digit_begin", file)
            print("\n---------------DTMF digits pressed for this call :--------------\n")
            code.append("\n---------------DTMF digits pressed for this call :--------------\n")
            
            if len(result) == 0:
                print("Not Found")
                code.append("Not found")
            else:
                for line in result:
                    print(line) 
                    code.append(line)
        
            print("\n-----------------ISDN LEG analysis--------------\n")
            code.append("\n-----------------ISDN LEG analysis--------------\n")
            
            result = get_isdn_info(file, local_call)
            if len(result)==0:
                print("Not Found")
                code.append("Not found")
                
            else:
                for line in result:
                    if "RX <- DISCONNECT" in line:
                        res=get_contents_with_keys(line, "", file)
                        for l in res:
                            print(l)
                            code.append(l)
                    else:
                        print(line)
                        code.append(line)
                        
            
            print("\n-------------------------Cause Value Analysis-------------------\n")
            print(f'{local_call["cause"]}',":",causeValueAnalysis(local_call["cause"]))
            
            # print(type(local_call["cause"]))
            code.append("\n-------------------------Cause Value Analysis-------------------\n")
            code.append(f'\n{local_call["cause"]} : {causeValueAnalysis(local_call["cause"])}')
            
            break
        
    return code

    ###################################################
            
        

        # call_id = input("To see call analysis please enter call id: ")
        # ccapi_value = input("To see call analysis please enter ccapi value: ").strip()
        
def rx_analyse_2(ccapi_value, call_details, file):
    
    code =[]
    for index, local_call in call_details.items():
        # print(local_call["call_id"])
        if  ccapi_value in local_call["ccapi_value"]:
            call_id=local_call["call_id"][0]
            print("\n\n")
            print("--------------------- This call consists of ",len(local_call["call_id"]), " SIP dialog ---------")
            
            code.append("\n\n")
            code.append(f"\n--------------------- This call consists of {len(local_call['call_id'])} SIP dialog ---------")
            
            counter=0
            postfix=["st","nd","rd","th"]
            
            for id in local_call["call_id"]:
                counter += 1
                print("----------------SIP Analysis of "+str(counter)+postfix[counter-1]+" call id ----------------")
                
                code.append("\n----------------SIP Analysis of "+str(counter)+postfix[counter-1]+" call id ----------------")
                
                result = get_contents_with_multiple_keys("SIP/Msg/ccsipDisplayMsg", file, contains=["To:", id])
                print("-------------------------For call id : " + id, "-------------------------\n")
                code.append("\n-------------------------For call id : " + id, "-------------------------\n")
                
                
                if len(result) == 0:
                    print("Not Found")
                    code.append("Not Found")
                        
                else:
                    for item in result:
                        for line in item:
                            print(line)
                            code.append(line)
                                # pass
                        print("\n ------------------------------------------------- \n")
                        code.append("\n ------------------------------------------------- \n")
        ## ------------------------
            if len(local_call["call_id"])>1:
                pass
            else:
                print("----------------ISDN LEG Analysis---------------")
                code.append("\n----------------ISDN LEG Analysis---------------")
                for index, local_call in call_details.items():
                    if  call_id in local_call["call_id"]:
                        print("\n\n")
                        print("---------For call ref value: "+ local_call["call_ref"]+"-----------")
                        
                        code.append("\n\n")
                        code.append("\n---------For call ref value: "+ local_call["call_ref"]+"-----------")
                        
                        result = get_call_with_lastdigits_of_call_ref(file, local_call["call_ref"])
                        for line in result:
                            print(line)
                            code.append(line)
                            
            print("\n-------------------------Cause Value Analysis-------------------\n")
            print(local_call["cause"],":",causeValueAnalysis(local_call["cause"]))
            
            code.append("\n-------------------------Cause Value Analysis-------------------\n")
            code.append(f"\n{local_call['cause']} : {causeValueAnalysis(local_call['cause'])}")

            result = get_contents_with_keys(local_call["ccapi_value"][0],"CCAPI/cc_api_call_digit_begin", file)
            print("\n---------------DTMF digits pressed for this call :--------------\n")
            code.append("\n---------------DTMF digits pressed for this call :--------------\n")
            
            
            if len(result) == 0:
                print("Not Found")
                code.append("Not Found")
            else:
                for line in result:
                    print(line)
                    code.append(line)

    return code

if __name__ == '__main__':
    file = open("log_file.txt", "r").read().split("\n") #log_file.txt # debugs.txt
    rx_call(file)






