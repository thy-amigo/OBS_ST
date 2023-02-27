
from .tx_logParser import *
from .rx_logParser import *
import streamlit as st
# getCallAndCauseValue , get_contents_with_keys, get_contents_with_multiple_keys


def tx_call(file, call_subtype):
    call_list_outgoing, call_list_incoming  = findtxLogs(file)
    if call_subtype=="1":
    
    # for call in call_list_outgoing:
    #     for line in call:
    #         print(line)

        call_details = extractBasicInfo(call_list_outgoing)
        if len(call_details)==0:
            print("No calls found!")
            return "No calls found!"
    
    elif call_subtype=="2":

        # call_details.update(extractBasicInfo(call_list_incoming, index=len(call_details)))
        call_details = extractBasicInfo(call_list_outgoing)
        if len(call_details)==0:
            print("No calls found!")
            return "No calls found!"

    if len(call_details) > 1:
        
        call_details_filtered={}
        index_i=0
    
        print("-----------------Details: ---------------------")
        for index, local_call in call_details.items():
            
            
            call_by_call_id = search_with_call_id(file, str(local_call["call_id"]))
            ccapi = get_ccapi_value(file, call_by_call_id)
            local_call["ccapi_value"]=ccapi
            for val in ccapi:
                local_call["call_id"]=[]
                local_call["cause"], local_call["call_id"] = getCallAndCauseValue(file, val)
                # print("call ids: ", local_call["call_id"])
            for val in local_call["ccapi_value"]:
                local_call["call_ref"] = get_call_ref(file, val)
                
    
            # call_details[index]= local_call
            # for key, value in local_call.items():
            #     print(key + " : " , value)
            
            # print("\n-----------CCAPI call set up:-----------\n")
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
            if local_call["call_ref"] is not None:
                # SIP-ISDN
                if call_subtype=="1":
                    call_details_filtered[index_i]=local_call
                    index_i+=1
            else:
                if call_subtype=="2":
                    # print("enter")
                    call_details_filtered[index_i]=local_call
                    index_i+=1
        
        call_details={}
        call_details = call_details_filtered
        
        if len(call_details)==0:
            print("No calls found!")
            return "No calls found!"
        
        else:
            return call_details
        
        '''
        for index, local_call in call_details.items():
            print("-------"+str(index+1)+" Of " + str(len(call_details))+"-------")
            for key, value in local_call.items():
                if key=="ccapi_value":
                        print(key,":",value[0])
                else:
                        print(key + " : " , value)
            
        
    
        # call_id = input("To see call analysis please enter call id: ")
        ccapi_value = input("To see call analysis please enter ccapi value: ").strip()
        '''
def tx_analyse(ccapi_value, call_details, file):
        
    print("-"*5, 'Analyzing Outgoing calls', 5*"-")
    ccapi_value = str(ccapi_value)
    print(ccapi_value)
    for index, local_call in call_details.items():
        # print(local_call["call_id"])
        # if  call_id in local_call["call_id"]
        
        code = []
        print(local_call["ccapi_value"])
        if ccapi_value in local_call["ccapi_value"]:
                       
            print("\n\n")
            print("--------------------- This call consists of ",len(local_call["call_id"]), " SIP dialog ---------")
            
            code.append("\n\n")
            code.append(f"--------------------- This call consists of {len(local_call['call_id'])} SIP dialog ---------")
            
            counter=0
            postfix=["st","nd","rd","th"]
            for id in local_call["call_id"]:
                counter += 1
                print("----------------SIP Analysis of "+str(counter)+postfix[counter-1]+" call id ----------------")
                code.append("----------------SIP Analysis of "+str(counter)+postfix[counter-1]+" call id ----------------")
                
                result = get_contents_with_multiple_keys("SIP/Msg/ccsipDisplayMsg", file, contains=["To:", id])
                print("-------------------------For call id : " + id, "-------------------------\n")
                code.append("-------------------------For call id : " + id+ "-------------------------\n")
                
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
            if len(local_call["call_id"])>1:
                pass
            else:
                print("----------------ISDN LEG Analysis---------------")
                code.append("----------------ISDN LEG Analysis---------------")
                for index, local_call in call_details.items():
                    if  local_call["call_id"]:
                        print("\n\n")
                        print("---------For call ref value: "+ local_call["call_ref"]+"-----------")
                        
                        code.append("\n\n")
                        code.append("---------For call ref value: "+ local_call["call_ref"]+"-----------")
                        
                        result = get_call_with_lastdigits_of_call_ref(file, local_call["call_ref"])
                        
                        for line in result:
                            print(line)
                            code.append(line)
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
                    
            print("\n-------------------------Cause Value Analysis-------------------\n")
            print(local_call["cause"],":",causeValueAnalysis(local_call["cause"]))
            
            code.append("\n-------------------------Cause Value Analysis-------------------\n")
            code.append(local_call["cause"]+":"+causeValueAnalysis(local_call["cause"]))

            return code

    '''
    # for index, local_call in call_details.items():
    #     for key, value in local_call.items():
    #         print(key + " : " , value)

    # call_id = input("Enter a call id to search : ")

    # for local_call in call_details:
    #     if local_call["call_id"] == call_id:
    # for call_id in call_details:
    #     call_by_call_id = search_with_call_id(file, str(call_id))
    #     ccapi = get_ccapi_value(file, call_by_call_id)
    #     print(len(ccapi), " ccapi values found")
    #     for value in ccapi:
    #         print("ccapi value found: ", value)
    #     index=1
    #     for call in call_by_call_id:
    #         print("------------------",index, " of ", len(call_by_call_id), "------------------")
    #         index +=1
    #         for line in call:
    #             print(line)

if __name__ == '__main__':
    file = open("D:\Lab-Customers\Tools\VGlogParser_v1.0.exe (1)\sip-sip call flow.txt", "r").read().split("\n")    # for outgoing calls.txt
    tx_call(file, '2')
    '''


