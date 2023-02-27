# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:52:54 2022

@author: WGTS4494
"""

import streamlit as st
from gw.rx_test import rx_call, rx_analyse_1, rx_analyse_2
from gw.tx_test import tx_call, tx_analyse

from io import StringIO

# REMOVE HEADER FOOTER, MAIN MENU AND TOP SPACE
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            div.block-container {padding-top:1rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

col1, col2 = st.columns([1,1])

with col1:  
    col1 = st.markdown("<h1 style='text-align: Right; color: red;'>JARVIS</h1>", unsafe_allow_html=True)

    # col1 = st.write('')

with col2:
    st.write('')
    st.write('')
    st.write('')
    col2 = st.text('-By Saurabh')

def gen(info_dic):
       
    template = []
    
    for k, v in info_dic.items():
        
        template.append(k)
        template.append('='*5)
        template.append(v)
        template.append('')
    _= '''    
    template.append('Problem Description')
    template.append('='*5)
    template.append(info_dic['Problem Description'])
    template.append('')
    
    template.append('Call Flow')
    template.append('='*5)
    template.append(info_dic['Call Flow'])
    template.append('')
    
    template.append('User Details')
    template.append('='*5)
    template.append(info_dic['User Details'])
    template.append('')
    
    template.append('Site & Device Details')
    template.append('='*5)
    template.append(info_dic['Site & Device Details'])
    template.append('')
    
    template.append('Business Impact')
    template.append('='*5)
    template.append(info_dic['Business Impact'])
    template.append('')
    
    template.append('Troubleshooting Done / Case History')
    template.append('='*5)
    template.append(info_dic['Troubleshooting Done / Case History'])
    template.append('')
    
    template.append('Trace / Logs collected')
    template.append('='*5)
    template.append(info_dic['Trace / Logs collected'])
    template.append('')
    
    template.append('Trace / Logs Location')
    template.append('='*5)
    template.append(info_dic['Trace / Logs Location'])
    template.append('')
    
    template.append('TAC / Vendor Ticket')
    template.append('='*5)
    template.append(info_dic['TAC / Vendor Ticket'])
    template.append('')
    
    template.append('Previous Oceane Ticket (if Any)')
    template.append('='*5)
    template.append(info_dic['Previous Oceane Ticket (if Any)'])
    template.append('')
    
    template.append('Proposed Acton by CTS2 (if Any)')
    template.append('='*5)
    template.append(info_dic['Proposed Acton by CTS2 (if Any)'])
    template.append('')
    
    template.append('Support required from CTS3')
    template.append('='*5)
    template.append(info_dic['Support required from CTS3'])
    template.append('')
    '''
    
    return template
        
def nice_print(data):
    s = ''
    
    for i in data:
        s += i+'\n'      
    return s

def call_type_option():
    
    if st.session_state['operation_type'] =="Incoming":
        call_type_choice = st.selectbox('Choose Call Type', options = ['isdn-sip', 'sip-sip'])
        
    elif st.session_state['operation_type'] =="Outgoing":
        call_type_choice = st.selectbox('Choose Call Type', options = ['sip-isdn', 'sip-sip'])
    
    
    return call_type_choice



# def trace_lookup(device):
    
#     trace_lookup_dic = {}
    
# ADD SIDEBAR OPTIONS
with st.sidebar:
    mode = st.selectbox('SELECT OPTION',
                        ('CTS3 Template', 'Trace Lookup', 'GW Debug'))

if mode == 'CTS3 Template':
  
    st.header('CTS3 TEMPLATE')
    st.text('          -script by Sunil')
    pd = st.text_area(label='Problem Description', height = 100)
    
    cf = st.text_area(label='Call Flow', height = 100)
    
    ud = st.text_area(label='User Details', height = 100)
    
    dd = st.text_area(label='Site & Device Details', height = 100)
    
    bi = st.selectbox(label='Business Impact', options = ['High', 'Medium', 'Low'])
    
    td = st.text_area(label='Troubleshooting Done / Case History', height = 100)
    
    tl_c = st.text_area(label='Trace / Logs collected', height = 100)
    
    tl_l = st.text_area(label='Trace / Logs Location', height = 100)
    
    tckt = st.text_input(label='TAC / Vendor Ticket')
    
    ocn_tckt = st.text_input(label='Previous Oceane Ticket (if Any)')
    
    pp_ap_cts2 = st.text_area(label='Proposed Acton by CTS2 (if Any)', height = 100)
    
    pp_ap_cts3 = st.text_area(label='Support required from CTS3', height = 100)
    
    cur_status = st.text_area(label='Current Status', height = 100)
    
    
    info_dic = {'Problem Description': pd,
                'Call Flow': cf,
                'User Details': ud,
                'Site & Device Details': dd,
                'Business Impact': bi,                
                'Troubleshooting Done / Case History': td,
                'Trace / Logs collected': tl_c,
                'Trace / Logs Location': tl_l,
                'TAC / Vendor Ticket': tckt,
                'Previous Oceane Ticket (if Any)': ocn_tckt,
                'Proposed Acton by CTS2 (if Any)': pp_ap_cts2,
                'Support required from CTS3': pp_ap_cts3,
                'Current Status': cur_status
                }
    
    # st.button(label='GENERATE')
    
    if st.button(label='GENERATE'):
        
        
        temp = gen(info_dic)
        
        s = ''
        
        for i in temp:
            
            s += i+'\n'
            
        # st.text_area(label ="",value=s, height=1000)
        st.code(s)

elif mode == 'Trace Lookup':
    st.header('TRACE LOOKUP')
    st.text('          -script by Navneet')
    trace_lookup = {'CUCM': {'CUCM trace Lookup': {'CALL RELATED ISSUES': ['''
                                                                           a. Call manager and CTI Manager logs
                                                                           b. Event Viewer - Application and Event Viewer - System logs.
                                                                           c. Timestamps of call failures, Calling and Called numbers.
                                                                           d. Detailed Call Flow (Devices involved in the call flow & Protocols'''],
                                                   'HIGH CPU/MEMORY UTILIZATION': ['''
                                                                                   Please collect all of the below traces for a particular  time period before the problem began till after the problem went away.  For instance, if we started observing high CPU or memory usage at 4 P.M.  and the problem went away by 5 P.M., then we would collect traces for a time interval of 3:30 P.M. to 5:30 P.M. This time interval can vary  from one issue to another, and also based on the customer set up.
                                                                                     a. Detailed Cisco Call Manager traces.                                                                
                                                                                     b. Event Viewer - Application and Event Viewer - System logs.                                                                
                                                                                     c. Cisco RISDC and Perfmon logs.                                                                
                                                                                     d. Cisco AMC service.                                                                
                                                                                     e. Cisco Tomcat and Tomcat Security logs.                                                                
                                                                                     f. Outputs from CLI: 'show status', 'show process using-most cpu/memory', 'show process load'.                                                                
                                                                                     g. Output of 'utils diagnose test'.
                                                                                     '''],
                                                   'EXTENSION MOBILITY LOGINS': ['''
                                                                                 a. Detailed Cisco Call Manager traces.                                                                                 
                                                                                 b. Cisco Extension Mobility.                                                            
                                                                                 c. Cisco Extension Mobility Application.                                                            
                                                                                 d. Cisco Tomcat and Tomcat Security logs.
                                                                                 '''],
                                                   'AGENT LOGINS - UCCX': ['''
                                                                            a. Detailed Cisco Call Manager traces.                                                                           
                                                                            b. Cisco Extension Mobility.                                                        
                                                                            c. Cisco Extension Mobility Application.                                                        
                                                                            d. Cisco Tomcat and Tomcat Security logs.                                                        
                                                                            e. Cisco AXL Web Service.                                                        
                                                                            f. Detailed Cisco CTI Manager logs.
                                                                            '''],
                                                   'LDAP SYNCHRONIZATION/AUTHENTICATION': ['''
                                                                                            a. Cisco Dirsync logs.
                                                                                            b. Cisco Tomcat and Tomcat Security logs.
                                                                                            c. Packet Captures on the call manager server when the sync is initialized also help.
                                                                                            '''],
                                                   'DRF BACKUP': ['''
                                                                  a. Cisco DRF Master.
                                                                  b. Cisco DRF Local.
                                                                  c. Failure logs from the DRF 'Current Status' page.
                                                                  '''],
                                                   'PHONE REGISTRATION': ['''
                                                                          a. Detailed Cisco Call Manager traces.
                                                                          b. Packet captures from both sides - CUCM server and IP Phone or the switch port to which the IP Phone is connected.
                                                                          c. Event Viewer - Application and Event Viewer - System logs.
                                                                          d. Phone Status Messages.
                                                                          e. Phone Console Logs.
                                                                          '''],
                                                   'IPMA': ['''
                                                            a. Detailed Cisco Call Manager traces.                                                            
                                                            b. Detailed Cisco CTI Manager traces.                                        
                                                            c. Cisco IP Manager Assistant.
                                                            d. JTAPI logs from the client side - PC
                                                            '''],
                                                   'CAR/CDR': ['''
                                                                a. Cisco CAR Scheduler.
                                                                b. Cisco CAR Web Agent.
                                                                c. Cisco CDR Agent.
                                                                d. Cisco CDR Repository Manager
                                                                '''],
                                                   'SECURITY - Such as IP Phone rejected due to security errors/ TLS Connections not setting up': ['''
                                                                                                                                                    a. Detailed Cisco Call Manager traces.
                                                                                                                                                    b. Cisco CTL Provider.
                                                                                                                                                    c. Cisco Trust Verification Service.
                                                                                                                                                    d. Cisco Certificate Authority Proxy Function.
                                                                                                                                                    '''],
                                                   'MEDIA RESOURCES - MOH not working/ DTMF issues/ No Ringback/ Conference drops/ MTP or XCoder Allocation failures': [''' 
                                                                                                                                                                        a. Detailed Cisco Call Manager traces.
                                                                                                                                                                        b. Cisco IP Voice Media Streaming App.
                                                                                                                                                                        c. Event Viewer - Application and Event Viewer - System logs.
                                                                                                                                                                        '''],
                                                   'COREDUMP': ['''
                                                                a. utils core active list.
                                                                b. utils core active analyze <coredump name>.
                                                                c. Detailed Cisco Call Manager traces for a particular period of time before the core was created.
                                                                d. Event Viewer - Application and Event Viewer - System logs.
                                                                e. Cisco RISDC and Perfmon Logs for a particular period of time before the core was created.
                                                                f. Outputs of 'show status', 'utils diagnose test', 'show process load', 'show process using-most memory/cpu'
                                                                '''],
                                                   'GUI DISPLAYS WRONG STATUS INFORMATION':['''
                                                                                            a. Cisco CCMAdmin Web Service.                                                                                            
                                                                                            b. Cisco Common User Interface.
                                                                                            c. Cisco Database Layer Monitor.
                                                                                            d. Cisco Database Notification Service.
                                                                                            e. Cisco RisBean Library.
                                                                                            f. Cisco Tomcat.
                                                                                            '''],
                                                   'TOMCAT ISSUES':['''
                                                                     a. Cisco Tomcat and Tomcat Security logs.
                                                                     b. Output of 'utils diagnose test'. This may generate a heap dump, which you can then collect using 'file get activelog tomcat/logs/*'
                                                                     c. Detailed Cisco Call Manager traces.
                                                                     '''],
                                                   'BANDWIDTH ISSUES':['''
                                                                         a. LBM logs
                                                                         b. CUCM logs
                                                                         c. Event Viewer - Application and Event Viewer - System logs.
                                                                         ''']
                                                                         },
                             'CUCM CLI commands':['''
                                                    show registry
                                                    show date
                                                    show status
                                                    show hardware
                                                    show workingdir
                                                    show tlstrace
                                                    show tlsresumptiontimeout
                                                    show web-security
                                                    show smtp
                                                    show accountlocking
                                                    show myself
                                                    show account
                                                    show itl
                                                    show ctl
                                                    show trace
                                                    show session maxlimit
                                                    show logins successful
                                                    show logins unsuccessful
                                                    show diskusage activelog
                                                    show diskusage common
                                                    show diskusage inactivelog
                                                    show diskusage install
                                                    show diskusage tftp
                                                    show diskusage tmp
                                                    show ups status
                                                    show environment temperatures
                                                    show environment fans
                                                    show environment power-supply
                                                    show memory size
                                                    show memory count
                                                    show memory modules
                                                    show open files all
                                                    show open files process
                                                    show open files regexp
                                                    show open ports all
                                                    show open ports regexp
                                                    show timezone config
                                                    show timezone list
                                                    show webapp session timeout
                                                    show Login Grace Timeout
                                                    show cert own name
                                                    show cert trust name
                                                    show cert list type
                                                    show csr own name
                                                    show csr list type
                                                    show password age
                                                    show password inactivity
                                                    show password history 
                                                    show password expiry maximum-age
                                                    show password expiry minimum-age
                                                    show password expiry user maximum-age userid
                                                    show password expiry user minimum-age userid
                                                    show password expiry user list
                                                    show password complexity character
                                                    show password complexity length
                                                    show password change-at-login userid
                                                    show version active
                                                    show version inactive
                                                    show packages active
                                                    show packages inactive
                                                    show cli pagination
                                                    show cli session timeout
                                                    show stats io
                                                    show process load
                                                    show process list
                                                    show process using-most cpu
                                                    show process using-most memory
                                                    show process open
                                                    show process name process-name 
                                                    show process user user-name
                                                    show process pid pid
                                                    show process search
                                                    show tech all
                                                    show tech system host
                                                    show tech system software
                                                    show tech system hardware
                                                    show tech system tools
                                                    show tech system kernel modules
                                                    show tech system bus
                                                    show tech system all
                                                    show tech runtime env
                                                    show tech runtime disk
                                                    show tech runtime memory
                                                    show tech runtime cpu
                                                    show tech runtime all
                                                    show tech network interfaces
                                                    show tech network routes
                                                    show tech network hosts
                                                    show tech network resolv
                                                    show tech network sockets
                                                    show tech network all
                                                    show tech network all
                                                    show tech dumpCSVandXML
                                                    show tech sqlhistory
                                                    show tech dbinuse
                                                    show tech dbschema
                                                    show tech dbstateinfo
                                                    show tech activesql
                                                    show tech dberrcode
                                                    show tech devdefaults
                                                    show tech gateway
                                                    show tech locales
                                                    show tech notify
                                                    show tech repltimeout
                                                    show tech dbhighcputasks
                                                    show tech procedures
                                                    show tech prefs
                                                    show tech routepatterns
                                                    show tech routeplan
                                                    show tech systables
                                                    show tech table table_name
                                                    show tech triggers
                                                    show tech version
                                                    show tech dbintegrity
                                                    show tech database dump
                                                    show tech database sessions
                                                    show tech params enterprise
                                                    show tech params service
                                                    show tech params all
                                                    show media streams
                                                    show network eth0 
                                                    show network dhcp eth0
                                                    show network route
                                                    show network status
                                                    show network all
                                                    show network ip_conntrack
                                                    show network max_ip_conntrack
                                                    show network ipprefs all
                                                    show network ipprefs enabled
                                                    show network ipprefs public
                                                    show network ipv6 settings
                                                    show network ipv6 route
                                                    show network ntp option
                                                    show network failover
                                                    show network name-service attributes
                                                    show network name-service hosts cache-stats
                                                    show network name-service hosts attributes
                                                    show network name-service services cache-stats
                                                    show network name-service services attributes
                                                    show network cluster
                                                    show dscp marking
                                                    show dscp status
                                                    show dscp defaults
                                                    show dscp all
                                                    show ipsec policy_group
                                                    show ipsec policy_name
                                                    show ipsec information
                                                    show ipsec status
                                                    show risdb list
                                                    show risdb query
                                                    show perf counterhelp
                                                    show perf list categories
                                                    show perf list classes
                                                    show perf list counters class-name
                                                    show perf list instances class-name
                                                    show perf query path
                                                    show perf query class
                                                    show perf query counter
                                                    show perf query instance
                                                    show samltrace level
                                                    show trace
                                                    set timezone
                                                    set webapp session timeout
                                                    set tlsresumptiontimeout
                                                    set Login Grace Timeout
                                                    set tlstrace enable
                                                    set tlstrace disable
                                                    set web-security
                                                    set smtp
                                                    set session maxlimit
                                                    set date
                                                    set account name
                                                    set account enable
                                                    set commandcount enable
                                                    set commandcount disable 
                                                    set accountlocking enable
                                                    set accountlocking disable
                                                    set accountlocking unlocktime 
                                                    set accountlocking count
                                                    set logging enable
                                                    set logging disable
                                                    set workingdir activelog
                                                    set workingdir inactivelog
                                                    set workingdir tftp
                                                    set cli pagination
                                                    set cli session timeout
                                                    set password history
                                                    set password user admin
                                                    set password user security
                                                    set password inactivity enable
                                                    set password inactivity disable
                                                    set password inactivity period
                                                    set password system bootloader encryptHash
                                                    set password complexity character enable
                                                    set password complexity character disable
                                                    set password complexity character difference
                                                    set password complexity character max-repeat
                                                    set password complexity minimum-length
                                                    set password age maximum 
                                                    set password age minimum
                                                    set password expiry maximum-age enable 
                                                    set password expiry maximum-age disable
                                                    set password expiry user maximum-age configure
                                                    set password expiry user maximum-age disable
                                                    set password expiry user minimum-age enable
                                                    set password expiry minimum-age enable
                                                    set password expiry minimum-age disable
                                                    set password change-at-login enable 
                                                    set password change-at-login disable
                                                    set csr gen
                                                    set cert regen
                                                    set cert import
                                                    set cert delete
                                                    set cert bulk sftp
                                                    set cert bulk export
                                                    set cert bulk consolidate
                                                    set cert bulk import
                                                    set registry
                                                    set network restore
                                                    set network status eth0 
                                                    set network ip eth0 
                                                    set network dhcp eth0 enable
                                                    set network dhcp eth0 disable
                                                    set network nic eth0
                                                    set network gateway
                                                    set network mtu
                                                    set network pmtud
                                                    set network domain
                                                    set network max_ip_conntrack
                                                    set network dns primary
                                                    set network dns secondary
                                                    set network dns options
                                                    set network ipv6 service
                                                    set network ipv6 dhcp
                                                    set network ipv6 static_address 
                                                    set network ipv6 gateway
                                                    set network ntp option
                                                    set network failover
                                                    set network name-service debug-level
                                                    set network name-service restart-interval
                                                    set network name-service paranoia
                                                    set network name-service reload-count
                                                    set network name-service hosts suggested-size
                                                    set network name-service hosts persistent
                                                    set network name-service hosts max-db-size
                                                    set network name-service hosts cache-enable
                                                    set network name-service hosts positive-time-to-live
                                                    set network name-service hosts negative-time-to-live
                                                    set network name-service services suggested-size
                                                    set network name-service services persistent
                                                    set network name-service services max-db-size
                                                    set network name-service services cache-enable
                                                    set network name-service services positive-time-to-live
                                                    set network name-service services negative-time-to-live
                                                    set network cluster publisher hostname
                                                    set network cluster publisher ip
                                                    set network cluster subscriber details
                                                    set network cluster subscriber dynamic-cluster-configuration
                                                    set dscp marking
                                                    set dscp enable
                                                    set dscp disable
                                                    set dscp defaults
                                                    set ipsec policy_group
                                                    set ipsec policy_name
                                                    set samltrace level
                                                    set trace enable Error
                                                    set trace enable Special
                                                    set trace enable State_Transition
                                                    set trace enable Significant
                                                    set trace enable Entry_exit
                                                    set trace enable Arbitrary
                                                    set trace enable Detailed
                                                    set trace disable 
                                                    delete smtp
                                                    delete process
                                                    delete account 
                                                    delete dns
                                                    delete dscp
                                                    delete ipsec policy_group 
                                                    delete ipsec policy_name 
                                                    file check
                                                    file list activelog 
                                                    file list inactivelog
                                                    file list install
                                                    file list salog
                                                    file list partBsalog
                                                    file list tftp
                                                    file view system-management-log
                                                    file view activelog
                                                    file view inactivelog
                                                    file view install
                                                    file view tftp
                                                    file search activelog
                                                    file search inactivelog
                                                    file search install
                                                    file search tftp
                                                    file get activelog
                                                    file get inactivelog
                                                    file get install
                                                    file get salog
                                                    file get partBsalog
                                                    file get tftp
                                                    file dump sftpdetails
                                                    file dump activelog
                                                    file dump inactivelog
                                                    file dump install 
                                                    file dump tftp
                                                    file tail activelog 
                                                    file tail inactivelog
                                                    file tail install
                                                    file tail tftp 
                                                    file delete activelog
                                                    file delete inactivelog 
                                                    file delete install
                                                    file delete tftp
                                                    file delete dir tftp
                                                    file fragmentation sdl file 
                                                    file fragmentation sdl all
                                                    file fragmentation sdl most recent
                                                    file fragmentation sdl most fragmented
                                                    file fragmentation sdi file
                                                    file fragmentation sdi all
                                                    file fragmentation sdi most recent number
                                                    file fragmentation sdi most fragmented number
                                                    utils ldap config ipaddr
                                                    utils ldap config fqdn
                                                    utils ldap config status
                                                    utils iostat
                                                    utils PlatformWebAccess enable
                                                    utils PlatformWebAccess disable
                                                    utils PlatformWebAccess status
                                                    utils netdump status
                                                    utils netdump enable
                                                    utils netdump disable
                                                    utils process core dumps status
                                                    utilsprocess core dumps enable
                                                    utils process core dumps disable
                                                    utils diagnose version
                                                    utils diagnose list
                                                    utils diagnose test
                                                    utils diagnose fix
                                                    utils diagnose module 
                                                    utils firewall ipv4 status
                                                    utils firewall ipv4 list
                                                    utils firewall ipv4 enable
                                                    utils firewall ipv4 disable
                                                    utils firewall ipv4 debug
                                                    utils firewall ipv6 status
                                                    utils firewall ipv6 list
                                                    utils firewall ipv6 enable
                                                    utils firewall ipv6 disable 
                                                    utils firewall ipv6 debug 
                                                    utils iothrottle enable
                                                    utils iothrottle disable
                                                    utils iothrottle status
                                                    utils service list 
                                                    utils service start 
                                                    utils service stop
                                                    utils service restart
                                                    utils service activate
                                                    utils service deactivate
                                                    utils service  auto-restart enable 
                                                    utils service  auto-restart disable
                                                    utils service  auto-restart show
                                                    utils system restart
                                                    utils system shutdown
                                                    utils system switch-version
                                                    utils system boot console
                                                    utils system boot serial
                                                    utils system boot status
                                                    utils system upgrade initiate
                                                    utils system upgrade cancel
                                                    utils system upgrade status
                                                    utils create report hardware
                                                    utils create report platform
                                                    utils create report security 
                                                    utils create report database
                                                    utils remote_account status
                                                    utils remote_account enable
                                                    utils remote_account disable
                                                    utils remote_account create
                                                    utils filebeat enable
                                                    utils filebeat disable
                                                    utils filebeat status
                                                    utils filebeat config
                                                    utils os secure status
                                                    utils os secure enforce
                                                    utils os secure permissive
                                                    utils os kerneldump status
                                                    utils os kerneldump enable
                                                    utils os kerneldump disable
                                                    utils os kerneldump ssh enable 
                                                    utils os kerneldump ssh disable 
                                                    utils os kerneldump ssh status
                                                    utils auditd enable
                                                    utils auditd disable
                                                    utils auditd status
                                                    utils core active list
                                                    utils core active analyze
                                                    utils core inactive list
                                                    utils core inactive analyze
                                                    utils fior status
                                                    utils fior enable
                                                    utils fior disable
                                                    utils fior start
                                                    utils fior stop
                                                    utils fior list 
                                                    utils fior top 
                                                    utils snmp get 3
                                                    utils snmp get 1
                                                    utils snmp get 2c
                                                    utils snmp walk 3
                                                    utils snmp walk 1
                                                    utils snmp walk 2c
                                                    utils snmp hardware-agents status
                                                    utils snmp hardware-agents start
                                                    utils snmp hardware-agents stop
                                                    utils snmp hardware-agents restart
                                                    utils snmp test
                                                    utils snmp config user 3 add
                                                    utils snmp config user 3 update
                                                    utils snmp config user 3 delete
                                                    utils snmp config user 3 list
                                                    utils snmp config trap 3 add
                                                    utils snmp config trap 3 update
                                                    utils snmp config trap 3 delete
                                                    utils snmp config trap 3 list
                                                    utils snmp config inform 3 add
                                                    utils snmp config inform 3 update
                                                    utils snmp config inform 3 delete
                                                    utils snmp config inform 3 list
                                                    utils snmp config mib2 add 
                                                    utils snmp config mib2 update
                                                    utils snmp config mib2 delete
                                                    utils snmp config mib2 list
                                                    utils snmp config 1/2c community-string add 
                                                    utils snmp config 1/2c community-string update
                                                    utils snmp config 1/2c community-string delete 
                                                    utils snmp config 1/2c community-string list
                                                    utils snmp config 1/2c trap add
                                                    utils snmp config 1/2c trap update
                                                    utils snmp config 1/2c trap delete
                                                    utils snmp config 1/2c trap list
                                                    utils snmp config 1/2c inform add
                                                    utils snmp config 1/2c inform update
                                                    utils snmp config 1/2c inform delete
                                                    utils snmp config 1/2c inform list
                                                    utils set urlpattern enable
                                                    utils set urlpattern disable
                                                    utils password generate 
                                                    utils reset_application_ui_administrator_password
                                                    utils reset_application_ui_administrator_name
                                                    utils restore_application_ui_administrator_account
                                                    utils ctl set-cluster mixed-mode
                                                    utils ctl set-cluster non-secure-mode
                                                    utils ctl update
                                                    utils ctl reset localkey
                                                    utils ils showpeerinfo 
                                                    utils itl reset localkey
                                                    utils itl reset remotekey  
                                                    utils dbreplication status 
                                                    utils dbreplication repair 
                                                    utils dbreplication repairtable
                                                    utils dbreplication repairreplicate replicatename 
                                                    utils dbreplication setrepltimeout
                                                    utils dbreplication setprocess
                                                    utils dbreplication stop 
                                                    utils dbreplication clusterreset
                                                    utils dbreplication forcedatasyncsub 
                                                    utils dbreplication quickaudit
                                                    utils dbreplication runtimestate 
                                                    utils dbreplication dropadmindb 
                                                    utils dbreplication dropadmindbforce 
                                                    utils dbreplication rebuild 
                                                    utils dbreplication reset 
                                                    util capf csr dump
                                                    util capf csr count
                                                    util capf csr delete
                                                    utils capf cert import
                                                    utils fips enable
                                                    utils fips disable
                                                    utils fips status
                                                    utils fedRAMP enable
                                                    utils fedRAMP disable
                                                    utils fedRAMP status
                                                    utils ha status 
                                                    utils ha failover 
                                                    utils ha fallback 
                                                    utils ha recover 
                                                    utils contactsearchauthentication enable
                                                    utils contactsearchauthentication disable
                                                    utils contactsearchauthentication status
                                                    utils network ping
                                                    utils network traceroute
                                                    utils network host name 
                                                    utils network arp list 
                                                    utils network arp set
                                                    utils network arp delete
                                                    utils network capture 
                                                    utils network capture-rotate 
                                                    utils network connectivity  
                                                    utils network name-service hosts cache invalidate
                                                    utils network name-service services cache invalidate
                                                    utils network ipv6 ping 
                                                    utils network ipv6 traceroute
                                                    utils network ipv6 host
                                                    utils sso status
                                                    utils sso enable
                                                    utils sso disable
                                                    utils sso recovery-url enable
                                                    utils sso recovery-url disable
                                                    utils vmtools refresh
                                                    utils trace collect ccm
                                                    utils ntp status
                                                    utils ntp config
                                                    utils ntp start
                                                    utils ntp restart
                                                    utils ntp server add
                                                    utils ntp server delete
                                                    utils ntp server list 
                                                    utils soap  realtimeservice  test
                                                    utils remotesyslog set protocol tcp
                                                    utils remotesyslog set protocol udp
                                                    utils remotesyslog show protocol
                                                    utils import config
                                                    utils disaster_recovery status
                                                    utils disaster_recovery history operation
                                                    utils disaster_recovery jschLogs operation
                                                    utils disaster_recovery cancel_backup confirm
                                                    utils disaster_recovery show_backupfiles 
                                                    utils disaster_recovery schedule list
                                                    utils disaster_recovery schedule add
                                                    utils disaster_recovery schedule enable
                                                    utils disaster_recovery schedule disable
                                                    utils disaster_recovery schedule delete
                                                    utils disaster_recovery backup network
                                                    utils disaster_recovery restore network
                                                    utils disaster_recovery show_registration
                                                    utils disaster_recovery device list
                                                    utils disaster_recovery device add network
                                                    utils disaster_recovery device delete
                                                    utils disaster_recovery prepare restore pub_from_sub
                                                    utils disaster_recovery estimate_tar_size 
                                                    utils update dst
                                                    utils scheduled-task list
                                                    utils scheduled-task enable 
                                                    utils scheduled-task disable
                                                    run sql 
                                                    run loadxml
                                                    run loadcsv
                                                    unset network domain
                                                    unset network dns options 
                                                    unset network ipv6 static_address 
                                                    unset network ipv6 gateway
                                                    unset network ntp options
                                                    unset network cluster subscriber dynamic-cluster-configuration
                                                    unset network cluster subscriber details
                                                    unset ipsec policy_group
                                                    unset ipsec policy_name
                                                    license management reset registration
                                                    license management reset identity
                                                    license management reset user password
                                                    license management security update
                                                    license management show system
                                                    license management show log level core_services 
                                                    license management show log level product_instances 
                                                    license management service activate 
                                                    license management service deactivate 
                                                    license management system remove
                                                    license management product re-register all
                                                    license management set log level core_services 
                                                    license management set log level product_instances 
                                                    license management unlock admin
                                                    license management list users
                                                    license management change user name
                                                    license file diagnose 
                                                    license file get 
                                                    license client reset registration
                                                    ''']
                                                    },
                                                    
               'Voice Gateway': {'Debug Lookup': ['''
                                                   For SIP-SIP call flow:
                                                    =========================== 
                                                    debug ccsip messages
                                                    debug ccsip info
                                                    debug ccsip feature <feature-name>
                                                    debug ccsip non-call
                                                    debug ccsip error
                                                    
                                                    Note: Debug "ccsip all" to be only run in off-business hours, in business hours you can use "debug ccsip messages"
                                    
                                                    For SIP-ISDN call flow:
                                                    ===========================
                                                    debug voice ccapi inout
                                                    debug isdn q931
                                                    debug ccsip messages
                                                    debug ccsip error
                                                    debug ccsip info
                                    
                                                    For H.323-ISDN call flow:
                                                    ===========================
                                                    debug voice ccapi inout
                                                    debug isdn q931
                                                    debug h225 asn1
                                                    debug h245 asn1
                                                    debug ip tcp transactions
                                    
                                                    For FXO/FXS, Digital E1R2:
                                                    ===========================
                                                    debug voice ccapi inout
                                                    debug voice vtsp all
                                                    debug vpm signal
                                                    
                                                    Show commands-All calls:
                                                    ===========================
                                                    show dial-peer voice summary
                                                    show dial-peer voice <dial-peer-id>
                                                    show dialplan number <number>
                                                    show call active voice compact
                                                    show call active voice brief
                                                    show call history voice brief
                                                    show call history stats cps
                                                    show voip rtp connection
                                                    show run dial-peer sort
                                                    
                                                    Show commands-SIP:
                                                    ===========================
                                                    show cube status
                                                    show sip-ua status
                                                    show sip-ua calls brief
                                                    show sip-ua register status
                                                    show sip-ua connections tcp detail
                                                    show sip-ua connections udp detail
                                                    show sip-ua statistics
                                                    
                                                    Show commands-ISDN:
                                                    ===========================
                                                    show isdn q931
                                                    show isdn service
                                                    show controller t1
                                                    show controller e1
                                                    show voice dsp group all
                                                    
                                                    Show commands-MGCP:
                                                    ===========================
                                                    show mgcp
                                                    show mgcp endpoint
                                                    show ccm-manager
                                                    show tcp brief
                                                    
                                                    Show commands-FXO/FXS & E1R2:
                                                    ===========================               
                                                    show voice port summary
                                                    show voice call summary
                                                    show voice dsp group all
                                                    
                                                    '''],
                                 'Advance Gateway debugs': ['''
                                                            # Advance Gateway debugs
                                                            ===========================
                                                            AFW (application)
                                                            
                                                            debug voip application accounting             AFW accounting debug
                                                            
                                                            debug voip application all                    all application messages
                                                            debug voip application callfeature            call feature debug
                                                            debug voip application callindependss         call-independent supplserv debug
                                                            debug voip application callsetup              call setup debug
                                                            debug voip application core                   AFW core library debug
                                                            debug voip application datastruct             AFW data structures debug
                                                            debug voip application digitcollect           call digit collect debug
                                                            debug voip application error                  application errors
                                                            debug voip application linking                script linking debug
                                                            debug voip application lpcor                  lpcor app debug
                                                            debug voip application media                  application media debug
                                                            debug voip application mlpp                   mlpp debug
                                                            debug voip application mwi                    mwi debug
                                                            debug voip application oodrefer               oodrefer app debug
                                                            debug voip application park-pickup            park & pickup app debug
                                                            debug voip application redirect               call redirection debug
                                                            debug voip application script                 application script debug
                                                            debug voip application session                default session app debug
                                                            debug voip application settlement             application settlement activities
                                                            debug voip application states                 application states
                                                            debug voip application stcapp                 SCCP Telephony Control Application
                                                            debug voip application supplementary-service  supplementary service
                                                            debug voip application tclcommands            application tclcommands debug
                                                            debug voip application vxml                   vxml debugging
                                                            debug voip application <cr>                   Application Framework library debugging
                                                    
                                                            ISDN
                                                            debug isdn all       ISDN debug messages
                                                            debug isdn api       ISDN Application Program Interface(s)
                                                            debug isdn cc        ISDN Call Control
                                                            debug isdn error     ISDN error messages
                                                            debug isdn events    ISDN events
                                                            debug isdn mgmnt     ISDN management
                                                            debug isdn q921      ISDN Q921 frames
                                                            debug isdn q931      ISDN Q931 packets
                                                            debug isdn standard  Standard ISDN debugging messages
                                                            debug isdn tgrm      ISDN TGRM events
                                                            debug ccm-manager backhaul events   Call Manager backhaul events
                                                            debug ccm-manager backhaul packets  Call Manager backhaul packets
                                                            debug voip tsp rose
                                                    
                                                            CDAPI
                                                            debug cdapi detail  CDAPI detail call activity
                                                            debug cdapi events  CDAPI events
                                                    
                                                            TSP
                                                             debug tsp all         Enable All TSP debugging (except stats)
                                                             debug tsp call        Call Debugging
                                                             debug tsp error       Enable tsp error debugging
                                                             debug tsp port        Port Debugging
                                                             debug tsp redundancy  Redundancy Debugging
                                                    
                                                            HTSP
                                                            The HTSP stack has been deprecated in 12.4 code.  Functions are now performed by VTSP or VPM.
                                                            debug htsp all
                                                    
                                                            VPM
                                                            debug vpm  all       Enable All VPM debugging
                                                            debug vpm  dsp       Enable dsp message trace (Warning: driver level trace)
                                                            debug vpm  error     Enable dsp error trace
                                                            debug vpm  overlay   Enable DSPware overlay debugging
                                                            debug vpm  port      Debug only on port specified
                                                            debug vpm  signal    Debug signaling services
                                                            debug vpm  spi       Enable session debugging trace
                                                            debug vpm  tgrm      Enable tgrm debugging
                                                            debug vpm  trunk-sc  trunk conditioning
                                                            debug vpm  voaal2    Debug Voice over AAL2
                                                    
                                                            DSPRM
                                                            debug dsp-resource-manager flex   ack       Flexdsprm GIGE Ack Debug
                                                            debug dsp-resource-manager flex   all       All Flexdsprm Debug
                                                            debug dsp-resource-manager flex   detail    Flexdsprm Detail Data Debug
                                                            debug dsp-resource-manager flex   download  Flexdsprm Firmware Download Debug
                                                            debug dsp-resource-manager flex   dspfarm   Flexdsprm Conferencing/Xcoding Debug
                                                            debug dsp-resource-manager flex   dspstats  Flexdsprm DSP Mips/credit/channel allocation Stats Debug
                                                            debug dsp-resource-manager flex   error     Flexdsprm Error Debug
                                                            debug dsp-resource-manager flex   function  Flexdsprm Function Debug
                                                            debug dsp-resource-manager flex   gige      Flexdsprm GIGE Debug
                                                    
                                                            HPI
                                                            debug voice hpi all           Turn ON all HPI debugging
                                                            debug voice hpi capture       HPI logger debugging
                                                            debug voice hpi checker       HPI Checker
                                                            debug voice hpi command       Debug commands sent to the DSP
                                                            debug voice hpi default       Turn ON inout and error debugging
                                                            debug voice hpi detail        Turn ON detailed debugging
                                                            debug voice hpi error         HPI error debugging
                                                            debug voice hpi function      Turn ON function tracing in HPI
                                                            debug voice hpi inout         Debug entry and exit from HPI subsystem - command, response, notification and stats
                                                            debug voice hpi nack          Debug NACK's received by HPI
                                                            debug voice hpi notification  Debug notifications received from DSP
                                                            debug voice hpi response      Debug responses received from DSP
                                                            debug voice hpi stats         HPI stats debugging
                                                            debug voice hpi               HPI (54x) DSP messages <----This does PVDM2 and PVDM3 too.
                                                            If enabling debug voice hpi all you may wish to disable debug voice hpi stat to cut down on noise.
                                                    
                                                            c5510
                                                            The closest we can get to the commands sent to the DSP are with:
                                                            debug vpm dsp     Enable dsp message trace (Warning: driver level trace)
                                                    
                                                            DSPAPI
                                                            debug voice dspapi all           Turn ON all DSP API debugging
                                                            debug voice dspapi command       Debug commands sent to the DSP
                                                            debug voice dspapi default       Turn ON inout and error debugging
                                                            debug voice dspapi detail        Turn ON detailed DSP API debugging
                                                            debug voice dspapi error         DSP API error debugging
                                                            debug voice dspapi function      Turn ON DSP API function tracing
                                                            debug voice dspapi inout         Debug entry and exit from the DSP API subsystem - Turns ON command, notification,
                                                                                              and response debugs
                                                            debug voice dspapi notification  Debug notifications from the DSP
                                                            debug voice dspapi response      Debug responses received from DSP
                                                            debug voice dspapi               Generic DSP API
                                                    
                                                            DSMP
                                                            debug voice dsmp  all         Enable All DSMP debugging (except stats)
                                                            debug voice dsmp  default     Activates inout, error, and event debugs
                                                            debug voice dsmp  error       Enabled DSMP error debugging
                                                            debug voice dsmp  event       State machine debugging
                                                            debug voice dsmp  function    Procedure tracing
                                                            debug voice dsmp  individual  Activation of individual DSMP debugs
                                                            debug voice dsmp  inout       Subsystem inout debugging
                                                            debug voice dsmp  rtp         Enable RTP debugging on DSM
                                                            debug voice dsmp  session     Session debugging
                                                            debug voice dsmp  stats       Stats debugging
                                                            debug voice dsmp  tone        Tone debugging
                                                            debug voice dsmp  udp         Enable UDP debugging on DSMP
                                                            debug voice dsmp  vofr        Enable VoFR debugging
                                                            debug voice dsmp              Distributed Streams Media Processor
                                                    
                                                            VTSP
                                                            debug voice vtsp   all         Enable All VTSP debugging
                                                            debug voice vtsp   default     Activates inout, error, and event debugs
                                                            debug voice vtsp   error       Enable VTSP error debugging
                                                            debug voice vtsp   event       State machine debugging
                                                            debug voice vtsp   function    Procedure tracing
                                                            debug voice vtsp   individual  Activation of individual VTSP debugs
                                                            debug voice vtsp   inout       Subsystem inout debugging
                                                            debug voice vtsp   session     Session debugging
                                                            debug voice vtsp   tone        Tone debugging
                                                            debug voice vtsp               Voice Telephony Call Control information
                                                    
                                                            CCAPI
                                                            debug voip ccapi all           Enable all debugs
                                                            debug voip ccapi default       Enable default debugs
                                                            debug voip ccapi detail        detail debug
                                                            debug voip ccapi error         major call and software errors debug
                                                            debug voip ccapi function      function debug
                                                            debug voip ccapi individual    individual CCAPI debug
                                                            debug voip ccapi inout         CCAPI Function in (enter) and out (exit)
                                                            debug voip ccapi protoheaders  CCAPI protocol headers/bodies passing info
                                                            debug voip ccapi service       service debug
                                                            debug voip ccapi               Call Control API
                                                    
                                                            MGCPAPP
                                                            debug mgcp all                 Enable all MGCP debug trace
                                                            debug mgcp endpoint            MGCP end point debugging
                                                            debug mgcp endptdb             MGCP endpoint database
                                                            debug mgcp errors              MGCP errors
                                                            debug mgcp events              MGCP events
                                                            debug mgcp gcfm                MGCP GCFM related debugs
                                                            debug mgcp inout               MGCP function entry/exit points
                                                            debug mgcp media               MGCP media
                                                            debug mgcp nas                 MGCP nas (data) events
                                                            debug mgcp packets             MGCP packets
                                                            debug mgcp parser              MGCP parser and builder
                                                            debug mgcp src                 MGCP System Resource Check CAC
                                                            debug mgcp state               MGCP state transitions
                                                            debug mgcp tracelevel-default  Default trace level for subsequent MGCP debug commands
                                                            debug mgcp voipcac             MGCP VOIP CAC
                                                    
                                                            STCAPP
                                                            debug voip application stcapp  all             All Debugs (except buffer-history)
                                                            debug voip application stcapp  buffer-history  Enable logging the history of debug info
                                                            debug voip application stcapp  error           Errors
                                                            debug voip application stcapp  events          Events
                                                            debug voip application stcapp  functions       Functions
                                                            debug voip application stcapp  port            Debug a specific voice-port
                                                    
                                                            SCCP
                                                            debug sccp all        Enable all SCCP debug trace
                                                            debug sccp config     SCCP auto-config/download
                                                            debug sccp errors     SCCP errors
                                                            debug sccp events     SCCP events
                                                            debug sccp keepalive  SCCP keepalive messages
                                                            debug sccp messages   SCCP signal messages
                                                            debug sccp packets    SCCP packets (very detailed)
                                                            debug sccp parser     SCCP parser and builder
                                                            debug sccp tls        SCCP client TLS connection establishment
                                                    
                                                            Dial peer (DPM)
                                                            debug voip dialpeer all       Enable all debugs
                                                            debug voip dialpeer default   Enable default debugs
                                                            debug voip dialpeer detail    detail debug
                                                            debug voip dialpeer error     major call and software errors debug
                                                            debug voip dialpeer function  function debug
                                                            debug voip dialpeer inout     inout debug
                                                            debug voip dialpeer           dialpeer debugging
                                                    
                                                            RTP
                                                            debug voip rtp error       Enable VOIP RTP Error debugging trace
                                                            debug voip rtp packet      Enable VOIP RTP Packet debugging trace
                                                            debug voip rtp session     Enable VOIP RTP Session debugging trace
                                                            debug voip rtp statistics  Enable VOIP RTP Statistics debugging trace
                                                            debug voip rtp             Enable VOIP RTP debugging trace
                                                    
                                                            CEF
                                                            debug ip cef accounting  Accounting events
                                                            debug ip cef drops       Packets dropped by CEF
                                                            debug ip cef events      IP CEF table events
                                                            debug ip cef ipc         IP CEF IPC events
                                                            debug ip cef local       Locally generated CEF switched packets
                                                            debug ip cef packet      Packets seen by IP CEF
                                                            debug ip cef receive     Packets received by IP CEF
                                                            debug ip cef subblock    IP CEF subblock events
                                                            Packet Interface
                                                            Work with a memeber of RP or CATS to troubleshoot at the interface driver level.
                                                    
                                                            TCP
                                                            debug ip tcp  CEF                 TCP CEF events
                                                            debug ip tcp  Winscale            Window-Scale
                                                            debug ip tcp  congestion          TCP Congestion events
                                                            debug ip tcp  driver              TCP driver events
                                                            debug ip tcp  driver-pak          TCP driver verbose
                                                            debug ip tcp  ecn                 Explicit Congestion Notification
                                                            debug ip tcp  header-compression  Header compression statistics
                                                            debug ip tcp  packet              TCP packets
                                                            debug ip tcp  rcmd                Rcmd transactions
                                                            debug ip tcp  sack                Selective-ACK
                                                            debug ip tcp  transactions        Significant TCP events
                                                    
                                                            UDP
                                                            debug ip udp        UDP based transactions
                                                    
                                                            SIP 
                                                            debug ccsip all        Enable all SIP debugging traces
                                                            debug ccsip calls      Enable CCSIP SPI calls debugging trace
                                                            debug ccsip dhcp       Enable SIP-DHCP debugging trace
                                                            debug ccsip error      Enable SIP error debugging trace
                                                            debug ccsip events     Enable SIP events debugging trace
                                                            debug ccsip function   Enable SIP function debugging trace
                                                            debug ccsip info       Enable SIP info debugging trace
                                                            debug ccsip media      Enable SIP media debugging trace
                                                            debug ccsip messages   Enable CCSIP SPI messages debugging trace
                                                            debug ccsip preauth    Enable SIP preauth debugging traces
                                                            debug ccsip states     Enable CCSIP SPI states debugging trace
                                                            debug ccsip transport  Enable SIP transport debugging traces
                                                    
                                                            H.323
                                                            debug cch323  CAPACITY  Enable Call Capacity debugging trace
                                                            debug cch323  NXE       Enable NXE transport debugging trace
                                                            debug cch323  RAS       Enable RAS State Machine debugging trace
                                                            debug cch323  all       Enable all CCH323 debugging traces
                                                            debug cch323  error     Enable CCH323 SPI debugging trace
                                                            debug cch323  function  Enable all CCH323 function traces
                                                            debug cch323  h225      Enable H225 State Machine debugging trace
                                                            debug cch323  h245      Enable H245 State Machine debugging trace
                                                            debug cch323  preauth   Enable CCH323 preauth debugging trace
                                                            debug cch323  rawmsg    Enable CCH323 RAWMSG debugging trace
                                                            debug cch323  session   Enable Session debugging trace
                                                            debug cch323  video     Enable CCH323 video debugging trace
                                                            debug h225 asn1    H.225 ASN1 Library
                                                            debug h225 events  H.225 Events
                                                            debug h225 q931    H.225 Q931 IE Details
                                                            debug h245 asn1    H.245 ASN1 Library
                                                            debug h245 events  H.245 Events
                                                            debug h245 srtp    H.245 SRTP Messages
                                                            debug h323-annexg  asn1    AnnexG ASN1 
                                                            debug h323-annexg  cache   AnnexG Cache
                                                            debug h323-annexg  errors  AnnexG Error Messages
                                                            debug h323-annexg  events  AnnexG Events
                                                            debug h323-annexg  inout   AnnexG Function in (enter) and out (exit)
                                                    
                                                            RTPSPI
                                                            debug rtpspi all      Enable all debug trace for RTP SPI.
                                                            debug rtpspi error    Enable RTP SPI error trace.
                                                            debug rtpspi inout    Enable RTP SPI function in/out trace.
                                                            debug rtpspi session  Enable RTP SPI Session debug trace.
                                                            debug rtpspi voipcac  Enable voipcac debug trace for RTP SPI.
                                                    
                                                            Sockets
                                                            Verify that the gateway is listening on the proper voice sockets:
                                                            2821-pod3#sh tcp br all | i 2000|1720|5060|2428|TCB
                                                            TCB       Local Address               Foreign Address             (state)
                                                            479A4428  14.50.211.11.2000           14.0.70.38.52450            ESTAB
                                                            4BA49950  14.50.211.11.11001          14.50.211.80.2000           ESTAB
                                                            49DD77D4  *.2000                      *.*                         LISTEN
                                                            48BA013C  *.5060                      *.*                         LISTEN
                                                            4BA0F004  *.1720                      *.*                         LISTEN
                                                            2821-pod3#sh udp | i 5060|2427|Proto
                                                            Proto        Remote      Port      Local       Port  In Out  Stat TTY OutputIF
                                                    
                                                            17     0.0.0.0             0 14.50.211.11     5060   0   0    11   0 
                                                            17     14.50.211.80     2427 14.50.211.11     2427   0   0   241   0
                                                            
                                                            '''],
                                 'Gateway Show commands':['''
                                                            show cdp – It will show CDP Timer and Holdtime Frequency                                                            
                                                            show cdp neighbors detail – It will show details of neighbor with an IP Address and IOS version                            
                                                            show cdp neighbors – It will show details of Device ID, Local Interface, Holdtime, Capability, Platform and Port ID                                                            
                                                            show cdp interface – It will show details of the interface if it is Up physically, Line protocol is up, Encapsulation and Holdtime.                                                            
                                                            show cdp traffic – It will show details of the CDP counters (CDP packets sent and received)                                                            
                                                            show voice call summary – It will show all the active calls on the Gateway, Ports, Codec, VAD (enabled or not), VTSP state and VPM state                                                            
                                                            show voice call status – It will show only the active calls, not all the ports. It includes Port, Called Number, and Dial Peer
                                                            show call history voice record – It will show information about calls made to and from the voice router
                                                            show voice port summary – It will show a detailed information on Ports, Channel, Signalling Type, Port Status, In Operation Status, Out Status and EC. It basically shows FXO/FXS/PRI ports in use.
                                                            show gateway – It will show the state and version is H.323
                                                            show dialplan number 1000 – It will show you what happens when the specified number is dialed
                                                            show dial-peer voice summary – It will show you what all dial-peers that are currently working. Summary of dial-peers/destination.
                                                            show voip rtp connections  – It will show all the current RTP connections which will have Local and Remote IP Address, Port Numbers, Call IDs.
                                                            show controllers T1    or   show controllers E1 – It will show the status of a controller if it is up or down
                                                            show call active voice brief – It will show the active call information which includes Call ID, Peer IP Address and Codecs
                                                            show mgcp  – It will show mgcp settings on the gateway
                                                            show dial-peer voice – It will show how voice dial peers are configured.
                                                            show mgcp statistics  – It will show mgcp statistics relationship between the devices which will have stats for CRCX, DLCX, MDCX and RSIP,  IP addresses of Call Agents etc
                                                            show mgcp endpoint –  It will show information related to MGCP endpoints
                                                            show mgcp connection  – It will show information about the current mgcp connections
                                                            show sip-ua register status – It will show SIP Registration information
                                                            show voice dsp – It will show the status of all the DSPs on the Gateway
                                                            show ccm-manager  – It will show information about the active and redundant configured Cisco Unified Communications Manager. This command also indicates if the gateway is currently registered with Cisco Unified Communications Manager.
                                                            show isdn active – It will show if a call is in progress and which number is being dialed.
                                                            show isdn status – It will show statistics of an ISDN connection and show if your PRI is up/established correctly
                                                            show ccm-manager fallback – It will show whether MGCP fallback is enabled or disabled, if enabled, whether it is currently active or not.
                                                            show sip service – It will help to display the status of SIP call service in a SIP gateway
                                                            show sip-ua status – It will help to display status for the SIP user agent (UA), including whether call redirection is enabled or disabled
                                                            cdp enable – It will enabled CDP on an interface                                                            
                                                            no cdp enable – It will disable CDP on an interface                                                            
                                                            test voice translation-rule – It will allow you to test a translation rule configured on the gateway.                                                            
                                                            Csim start XXXXX – It is a hidden command which helps to generate calls 
                                                            '''],
                                                               
                                 'Other issues': {'Router High CPU': ['''
                                                                        Please collect the following information collected on a periodic (hourly) basis:
                                                                        --------------------------------------------------------------------------------
                                                                        Show log
                                                                        Show proc cpu sorted  | e 0.00%
                                                                        show proc cpu history
                                                                        Show proc <process ID (or) PID> (For each process exhibiting High CPU)
                                                                        Show interface        (Two outputs of this command for every sample)
                                                                        Show interface stat   (Two outputs of this command for every sample)
                                                                        Show interface switching
                                                                        Show ip traffic
                                                                        Show ip interface
                                                                        Show alignment
                                                                        Show stacks
                                                                        Show context
                                                                        Show call active voice compact
                                                                        Show call active voice brief
                                                                        Show voip rtp connection
                                                                        Show ip rtp header-compression
                                                                        Show call history voice compact
                                                                        Show call history voice brief
                                                                        T1 PRI in All Platforms
                                                                        -----------------------
                                                                        Show isdn call-rate
                                                                        Show isdn call-rate table
                                                                        show isdn active
                                                                        show isdn history
                                                                        T1 CAS in AS5350 / AS5400 / AS5850 Platforms
                                                                        --------------------------------------------
                                                                        show csm call rate
                                                                        show csm call failed
                                                                        show csm call total
                                                                        If CEF is enabled,
                                                                        ------------------
                                                                        Show ip cef
                                                                        Show ip cef summary
                                                                        Show cef not-switched
                                                                        Show cef drop
                                                                        Show cef interface
                                                                        
                                                                        '''],
                                                  'Router Memory leak':['''
                                                                        Please collect the following information collected on a periodic (hourly) basis:
                                                                        --------------------------------------------------------------------------------
                                                                        Show buffers
                                                                        Show interface
                                                                        Show proc memory sorted
                                                                        Show proc memory <process ID (or) PID> (For each process consuming/holding
                                                                        large amount of memory)
                                                                        Show proc cpu
                                                                        Show log
                                                                        Show call active voice brief
                                                                        Advanced Show commands:
                                                                        -----------------------
                                                                        Show memory summary
                                                                        Show memory allocating-process totals
                                                                        Show memory io allocating-process totals
                                                                        Collect Core Dump, refer the following URL in regard:
                                                                        http://www.cisco.com/en/US/customer/products/sw/iosswrel/ps1835/products_tech_note09186a00800c7d59.shtml
                                                                        '''],
                                                  'Voice quality issues':['''
                                                                            VOIP-one way audio/no way audio/choppy voice:
                                                            
                                                                            Show version
                                                                            Show run
                                                                            Make a call and recreate the problem
                                                                            Collect the following Show commands when the call is active
                                                                            -----------------------------------------------------------
                                                                            Show ip socket
                                                                            Show voip rtp connection
                                                                            Show voice port summ
                                                                            Show voice call summ
                                                                            When the call is active, take "multiple" outputs of the following commands
                                                                            --------------------------------------------------------------------------
                                                                            Show voice dsp
                                                                            Show call active voice
                                                                            Show call active voice brief
                                                                            Show voice call <voice-port number>
                                                                            Show call active voice echo-canceller summary
                                                                            Show call active voice echo-canceller port <voice-port number>
                                                                            Note: Voice-port number is obtained from the "PORT" field of "show voice call summ"
                                                                            Disconnect the call and take the output of the following commands
                                                                            -----------------------------------------------------------------
                                                                            Show call history voice brief
                                                                            Show call history voice
                                                                            Basic Debugs
                                                                            ------------
                                                                            debug voip ccapi inout
                                                                            debug hpi all
                                                                            debug vtsp all
                                                                            Enable appropriate H.323/MGCP/SIP debugs.
                                                                            AS5350 / AS5400 / AS5850 Specific Commands
                                                                            ------------------------------------------
                                                                            Show spe
                                                                            Show spe voice active <spe slot number>
                                                                            Show port operational-status <spe slot number>
                                                                            Show port config <spe slot number>
                                                                            Show voice call stat
                                                                            Capture PCM Capture and Packet Sniffer Traces
                                                                            '''],
                                                  'SCCP: VG224 registration issues': ['''
                                                                                        Show version
                                                                                        Show run
                                                                                        Show stcapp device summary
                                                                                        Basic Debugs
                                                                                        ------------
                                                                                        debug voip application stcapp port [voice-port number]
                                                                                        debug sccp event
                                                                                        debug sccp config
                                                                                        Advanced Debugs
                                                                                        ---------------
                                                                                        debug voip application stcapp all
                                                                                        debug sccp message
                                                                                        
                                                                                        '''],
                                                  'SCCP: Call feature/set up issues': ['''
                                                                                        Show version
                                                                                        Show run
                                                                                        Show stcapp device summary
                                                                                        Show stcapp feature codes
                                                                                        Basic Debugs
                                                                                        ------------
                                                                                        debug voip application stcapp port [voice-port number]
                                                                                        debug vpm signal
                                                                                        debug sccp event
                                                                                        debug voip vtsp all
                                                                                        debug voip ccapi inout
                                                                                        Advanced Debugs
                                                                                        ---------------
                                                                                        debug voip application stcapp all
                                                                                        debug sccp message
                                                                                        '''],
                                                  'SIP : RTP NTE DTMF issues': ['''
                                                                                SIP : RTP NTE DTMF issues:
                                                                
                                                                                Show version
                                                                                Show run
                                                                                Show sip-ua
                                                                                show sip-ua register status
                                                                                Basic Debugs
                                                                                ------------
                                                                                debug ccsip messages
                                                                                debug voip rtp session named-events
                                                                                debug voip rtp error
                                                                                debug voip ccapi inout
                                                                                
                                                                                '''],
                                                  'SIP: TCL app (subscribe & notify) issues': ['''
                                                                                                SIP: TCL app (subscribe & notify) issues:
                                                                                                
                                                                                                Show version
                                                                                                Show run
                                                                                                Show sip-ua
                                                                                                show sip-ua register status
                                                                                                Basic Debugs
                                                                                                ------------
                                                                                                debug ccsip all
                                                                                                debug asnl events
                                                                                                debug voip ccapi inout
                                                                                                debug voip ccapi protoheaders
                                                                                                debug voip ivr script
                                                                                                
                                                                                                Note: Debug "ccsip all" to be only run in off-business hours, in business hours you can use "debug ccsip messages"
                                                                                                '''],
                                                  'SIP : NAT issues':['''
                                                                        SIP : NAT issues
                                                        
                                                                        Show version
                                                                        Show run
                                                                        Show sip-ua
                                                                        show sip-ua register status
                                                                        Show ip nat translation
                                                                        Basic Debugs
                                                                        ------------
                                                                        debug ip nat sip
                                                                        Enable appropriate debugs in the IOS Gateway.
                                                                        Advanced Debugs
                                                                        ---------------
                                                                        debug ip nat detailed
                                                                        debug ip nat fragment
                                                                        Capture Sniffer traces
                                                                    
                                                                        '''],
                                                  'MGCP : Call setup/signaling/routing issues':['''
                                                                                                MGCP : Call setup/signaling/routing issues:
                                                                                
                                                                                                Show version
                                                                                                Show run
                                                                                                Show ccm-manager
                                                                                                Show mgcp endpoint
                                                                                                Basic Debugs
                                                                                                ------------
                                                                                                debug mgcp events
                                                                                                debug mgcp packet
                                                                                                debug mgcp errors
                                                                                                debug mgcp state
                                                                                                debug vtsp events
                                                                                                debug vtsp session
                                                                                                debug voip ccapi inout
                                                                                                Enable appropriate ISDN/CAS/FXS/FXO debugs
                                                                                                Advanced Debugs
                                                                                                ----------------
                                                                                                debug mgcp all
                                                                                                debug vtsp all
                                                                                                debug hpi all
                                                                                                debug dspapi all
                                                                                                debug rtpspi all
                                                                                                debug voip ccapi error
                                                                                                Provide the following information:
                                                                                                ----------------------------------
                                                                                                CallManager Detailed Traces
                                                                                                Time of Problem Occurence
                                                                                                IP addresses of the IP Phones/devices used in recreating the problem
                                                                                            
                                                                                                '''],
                                                  'MGCP: CCM registration issues': ['''
                                                                                    MGCP: CCM registration issues:
                                                                    
                                                                                    Show version
                                                                                    Show run
                                                                                    Show ccm-manager
                                                                                    Show mgcp endpoint
                                                                                    Basic Debugs
                                                                                    ------------
                                                                                    debug ccm-manager config-download
                                                                                    debug ccm-manager errors
                                                                                    debug ccm-manager events
                                                                                    debug mgcp packet
                                                                                    debug mgcp events
                                                                                    debug mgcp errors
                                                                                    debug mgcp state
                                                                                    
                                                                                    '''],
                                                  'ISDN: call processing issues': ['''
                                                                                    ISDN: call processing issues:
                                                                    
                                                                                    Show version
                                                                                    Show run
                                                                                    Show diag
                                                                                    Show controller
                                                                                    Show isdn status
                                                                                    Show isdn service
                                                                                    Basic Debugs
                                                                                    ------------
                                                                                    debug isdn q931
                                                                                    debug isdn events
                                                                                    debug isdn standard
                                                                                    Advanced Debugs
                                                                                    ----------------
                                                                                    debug bri-interface (for BRI interfaces only)
                                                                                    debug isdn events detail
                                                                                    debug isdn cc detail (call control)
                                                                                    debug cdapi events
                                                                    
                                                                                    '''],
                                                  'H323: NAT issues': ['''
                                                                        H323: NAT issues:
                                                        
                                                                        Show version
                                                                        Show run
                                                                        Show ip nat translation
                                                                        Basic Debugs
                                                                        ------------
                                                                        debug ip nat h323
                                                                        Enable appropriate debugs in the IOS Gateway.
                                                                        Advanced Debugs
                                                                        ---------------
                                                                        debug ip nat detailed
                                                                        debug ip nat fragment
                                                                        Capture Sniffer traces
                                                        
                                                                        '''],
                                                  'FXO/FXS signaling issues': ['''
                                                                                FXO/FXS signaling issues:
                                                                
                                                                                Show version
                                                                                Show run
                                                                                Show vtsp call fsm
                                                                                Show voice trace <FXS/FXO voice port number>
                                                                                Basic Debugs
                                                                                ------------
                                                                                debug voip ccapi inout
                                                                                debug vpm signal
                                                                                debug vtsp events
                                                                                debug vtsp session
                                                                                Advanced Debugs
                                                                                ----------------
                                                                                debug dspapi all
                                                                                debug hpi all
                                                                                debug vtsp all
                                                                                debug dsprm all
                                                                
                                                                                '''],
                                                  'DSP: hung calls/hung dsp/missing digits/one way /no audio issues': ['''
                                                                                                                        DSP: hung calls/hung dsp/missing digits/one way /no audio issues:
                                                                                                        
                                                                                                                        Show version
                                                                                                                        Show run
                                                                                                                        Show diag
                                                                                                                        Show voice dsp
                                                                                                                        Show call active voice brief
                                                                                                                        Show vtsp call fsm
                                                                                                                        Show voice trace <FXS/FXO/T1/E1 voice port number>
                                                                                                                        Example(s):
                                                                                                                        Show voice trace 1/0/0
                                                                                                                        Show voice trace 1/0:23
                                                                                                                        Show voice trace 1/0:D
                                                                                                                        For AS5300, please also collect the following Show command:
                                                                                                                        -----------------------------------------------------------
                                                                                                                        Router#test dsp
                                                                                                                        dsprm_1> Show dangling
                                                                                                                        Basic Debugs
                                                                                                                        ------------
                                                                                                                        debug vtsp events
                                                                                                                        debug vtsp session
                                                                                                                        debug voip ccapi inout
                                                                                                                        debug dspapi all
                                                                                                                        Enable appropriate H.323/SIP/MGCP debugs.
                                                                                                                        Advanced Debugs
                                                                                                                        ---------------
                                                                                                                        debug vtsp all
                                                                                                                        debug dspapi all
                                                                                                                        debug hpi all
                                                                                                                        '''],
                                                  'Cisco IOS gateway: Authentication, Authorization & Accounting  AAA': ['''
                                                                                                                            Cisco IOS gateway: Authentication
                                                                                                            
                                                                                                                            Show version
                                                                                                                            Show run
                                                                                                                            debug aaa authentication
                                                                                                                            debug aaa id
                                                                                                                            debug tacacs
                                                                                                                            debug radius
                                                                                                                            debug condition user <username>
                                                                                                                            debug voip ccapi inout
                                                                                                                            debug voip aaa
                                                                                                                            
                                                                                                                            Cisco IOS gateway: Authorization
                                                                                                            
                                                                                                                            Show version
                                                                                                                            Show run
                                                                                                                            debug aaa authorization
                                                                                                                            debug aaa id
                                                                                                                            debug tacacs
                                                                                                                            debug radius
                                                                                                                            debug condition user <username>
                                                                                                                            debug voip ccapi inout
                                                                                                                            debug voip aaa
                                                                                                                            
                                                                                                                            Cisco IOS gateway: Accounting  AAA
                                                                                                            
                                                                                                                            Show version
                                                                                                                            Show run
                                                                                                                            debug aaa accounting
                                                                                                                            debug aaa id
                                                                                                                            debug tacacs
                                                                                                                            debug radius
                                                                                                                            debug condition user <username>
                                                                                                                            debug voip ccapi inout
                                                                                                                            debug voip aaa
                                                                                                                            ''']
                                                                                                                            }
                                                                                                                         },
               'Unity Connection': ['''
                                    Problem Area:
                                    --------------
                                    Audio Issues
                                    Playing an attachment via the TUI
                            
                                    Micro Traces to Set
                            
                                    CML (all levels)
                                    ConvSub (all levels)
                            
                                    RTMT Service to Select while taking logs
                            
                                    Connection Conversation Manager
                                    Connection Notifier
                                    Connection Tomcat Application
                                    Connection Conversation Manager
                                    
                                    ========================
                                    
                                    Problem Area:
                                    --------------
                                    
                                    Calendar Integration Issues
                                    Calendar integration
                            
                                    Micro Traces to Set
                            
                                    CCL (levels 10, 11, 12, 13)
                                    CsWebDav (levels 10, 11, 12, 13)
                            
                                    RTMT Service to Select while taking logs
                            
                                    Connection Conversation Manager
                                    Connection Tomcat Application
                                    Connection Conversation Manager
                                    Connection Tomcat Application
                            
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    Call Issues: Routing rules
                            
                                    Micro Traces to Set
                            
                                    Arbiter (levels 14, 15, 16)
                                    RoutingRules (level 11)
                            
                                    RTMT Service to Select while taking logs
                            
                                    Connection Conversation Manager
                                    
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    
                                    Unity Connection Cluster Issues: Unity Connection clusters (except file replication)
                                    Micro Traces to Set
                                    SRM (all levels)
                                    RTMT Service to Select while taking logs
                                    Connection Server Role Manager
                            
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    Unity Connection Cluster Issues: Unity Connection cluster file replication
                            
                                    Micro Traces to Set
                                    CuFileSync (all levels)
                                    RTMT Service to Select while taking logs
                                    Connection File Syncer
                                    
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    External Message Store Issues: Accessing emails in an external message store                            
                            
                                    Micro Traces to Set
                                    CML (all levels)
                                    RTMT Service to Select while taking logs
                                    Connection Conversation Manager
                                    Connection Tomcat Application
                            
                                    =====================
                                    
                                    Problem Area:
                            
                                    LDAP Issues: LDAP synchronization
                            
                                    Micro Traces to Set
                                    CuCmDbEventListener
                                    RTMT Service to Select while taking logs
                                    Connection CM Database Event Listener
                            
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    
                                    Message Issues
                            
                                    Micro Traces to Set
                                    MTA (all levels)
                                    RTMT Service to Select while taking logs
                                    Connection Message Transfer Agent
                       
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    Message Relay Issues
                             
                                    Micro Traces to Set
                                    MTA (all levels)
                                    SMTP (all levels)
                                    RTMT Service to Select while taking logs
                                    Connection Message Transfer Agent
                                    Connection SMTP Server
                                    
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    Notifications not sent
                            
                                    Micro Traces to Set
                                    CuCsMgr (all levels)
                                    Notifier (all levels except 6 and 7)
                                    RTMT Service to Select while taking logs
                                    Connection Conversation Manager
                                    Connection Notifier
                            
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    Jabber VoiceMail Issue
                            
                                    Micro Traces to Set
                                    Notifier (level 18 and 21)
                                    Cuca
                                    VMREST
                                    RTMT Service to Select while taking logs
                                    Cisco Tomcat
                                    Connection Jetty
                                    Connection Notifier
                                    Connection Tomcat Application
                            
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    Visual VoiceMail Issue
                            
                                    Micro Traces to Set
                                    TRAP - (all levels)
                                    VMREST (all levels)
                                    Arbiter - (level 12 to17)
                                    CDE-04 - <13-17>
                                    MiuCall - (all levels)
                                    MiuGeneral - (all levels)
                                    MiuIO - <11-15>
                                    MiuMethod - (all levels)
                                    MiuSIP - (all levels)
                                    MiuSIPStack - (all levels)
                                    Mixer - (all levels)
                            
                            
                                    RTMT Service to Select while taking logs
                            
                                    Cisco Tomcat
                                    Connection Jetty
                                    Connection Notifier
                                    Connection Tomcat Application
                                    Connection Conversation Manager
                                    Connection Mixer
                                    
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    SAML SSO Issues
                            
                                    Traces to Set
                            
                                    CLI Command to activate SAML SSO logs:
                                    admin: set samltrace level <trace-level> where trace-level can be BEBUG, INFO, WARNING, ERROR, or FATAL
                                    
                                    CLI Command to check trace level:
                                    admin: show samltrace level
                                    
                                    RTMT Service to Select while taking logs
                            
                                    Cisco Tomcat
                                    Cisco Tomcat Security
                                    Cisco SSO
                            
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    
                                    Audio Issues
                            
                                    Macro Traces to Set
                                    Media (Wave) Traces
                                    
                                    RTMT Service to Select while taking logs
                            
                                    Connection Conversation Manager
                                    Connection Mixer
                            
                                    =====================
                                    
                                    Problem Area:
                                    --------------
                                    Call Issues
                            
                                    Macro Traces to Set
                                    Call Control (Miu) Traces (expand the macro trace to select SIP or SCCP)
                                    Call Flow Diagnostics
                            
                                    RTMT Service to Select while taking logs
                            
                                    Connection Conversation Manager
                                    
                                    '''],
               'UCCX': ['''
                        Go to this link for UCCX trace lookup:
            
                        https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/210888-Tech-Note-on-UCCX-Tracing-Levels.html
                        '''],
               'UCCE': ['''
                        Go to this link for UCCE trace lookup:
            
                        https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise-1151/212635-how-to-set-traces-and-collect-ucce-logs.html
                        '''],
               'IM&P': {'Traces Used to Investigate Login and Authentication Issues Service': ['''
                                                                                                ## Traces Used to Investigate Login and Authentication Issues Service:
                                                                                
                                                                                                Cisco Client Profile Agent (CPA)
                                                                                                Cisco XCP Connection Manager
                                                                                                Cisco XCP Router
                                                                                                Cisco XCP Authentication Service
                                                                                                Cisco Tomcat Security Logs
                                                                                                '''],
                                                                                                
                        'Recommended Traces for Availability, IM, Contact List, and Group Chat Issues': ['''
                                                                                                        ## Recommended Traces for Availability, IM, Contact List, and Group Chat Issues:
                                                                                        
                                                                                                        -End user has no availability status displayed or incorrect availability status for some or all of their contacts.
                                                                                        
                                                                                                        Perform traces for the listed services on the IM and Presence Service node on which the end users and contacts are provisioned.
                                                                                        
                                                                                                        Cisco XCP Connection Manager
                                                                                                        Cisco XCP Router
                                                                                                        Cisco Presence Engine
                                                                                        
                                                                                                        -End user has issues with their self availability status, including on-the-phone or meeting status.
                                                                                        
                                                                                                        Perform traces for the listed services on the IM and Presence Service node on which the end user is provisioned.
                                                                                        
                                                                                                        Cisco XCP Connection Manager
                                                                                                        Cisco XCP Router
                                                                                                        Cisco Presence Engine
                                                                                        
                                                                                                        -End user has issues sending or receiving instant messages.
                                                                                        
                                                                                                        Perform traces for the listed services on the IM and Presence Service nodes on which the sender and recipient are provisioned.
                                                                                                        Cisco XCP Connection Manager
                                                                                                        Cisco XCP Router 
                                                                                                        '''],
                        'End user is experiencing issues': ['''
                                                            ## End user is experiencing any of the following issues:
                                            
                                                            Difficulty creating or joining a chat room.
                                                            Chat room messages are not being delivered to all members.
                                                            Any other issues with the chat room.
                                                            Perform traces for the listed services on the IM and Presence Service node on which the chat room members are provisioned.
                                            
                                                            Cisco XCP Connection Manager
                                                            Cisco XCP Router
                                                            Cisco XCP Text Conferencing Manager
                                            
                                                            -The node on which the chat room that is experiencing difficulties is hosted and the node on which the creator is provisioned are not the same.
                                            
                                                            Perform an initial trace analysis to determine which node hosted the chat room. Then perform traces for the following services on the IM and Presence Service node that hosted the chat room.
                                                            Cisco XCP Text Conferencing Manager
                                                            Cisco XCP Router
                                                            '''],
                        'Traces Used to Investigate Intercluster Sycnronization Issues Between Nodes': ['''
                                                                                                        ## Traces Used to Investigate Intercluster Sycnronization Issues Between Nodes:
                                                                                        
                                                                                                        Cisco Intercluster Sync Agent
                                                                                        
                                                                                                        Cisco AXL Web Service
                                                                                        
                                                                                                        Cisco Tomcat Security Log
                                                                                        
                                                                                                        Cisco Syslog Agent
                                                                                                        '''],
                        'Traces Used to Investigate XMPP Federation Issues': ['''
                                                                                ## Traces Used to Investigate XMPP Federation Issues:
                                                                
                                                                                Cisco XCP Router
                                                                                Cisco XCP XMPP Federation Connection Manager
                                                                            '''],
                        'SIP Federation Traces': ['''
                                                    ## SIP Federation Traces:
                                    
                                                    Cisco SIP Proxy
                                                    Cisco XCP Router
                                                    Cisco XCP SIP Federation Connection Manager
                                                '''],
                        'CLI Commands Used to Investigate High CPU and Low VM Alerts': ['''
                                                                                        ## CLI Commands Used to Investigate High CPU and Low VM Alerts:
                                                                        
                                                                                        Use the CLI to run the following commands on the node.
                                                                        
                                                                                        show process using-most cpu
                                                                                        show process using-most memory
                                                                                        utils dbreplication runtimestate
                                                                                        utils service list
                                                                                        
                                                                                        Use the CLI to collect all RIS (Real-time Information Service) performance logs for the node. Use only SFTP servers for file transfers using file get.
                                                                        
                                                                                        file get activelog cm/log/ris/csv
                                                                                        '''],
                        'Traces Used to Investigate High CPU and Low VM Alerts': ['''
                                                                                    ## Traces Used to Investigate High CPU and Low VM Alerts:
                                                                    
                                                                                    Cisco XCP Router
                                                                                    Cisco XCP SIP Federation Connection Manager
                                                                                    Cisco SIP Proxy
                                                                                    Cisco Presence Engine
                                                                                    Cisco Tomcat Security Log
                                                                                    Cisco Syslog Agent
                                                                                ''']
                                                                                },
               'Expressway C & E': ['''
                                    Go to this link for Expressway C & E diagnostic logs lookup:
                        
                                    https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/213360-collect-expressway-vcs-diagnostic-log-fo.html
                                    '''],
               'Packet capture procedure': {'Packet capture from GW (ISR G2 Only) interface': ['''
                                                                                                ## Packet capture from GW (ISR G2 Only) interface.
                                                                                        
                                                                                                ip traffic-export profile TACCAPTURE mode capture
                                                                                                  bidirectional
                                                                                                   no length
                                                                                        
                                                                                                // Identify the right interface and configure packet capture as below
                                                                                                !
                                                                                                interface GigabitEthernet0/0
                                                                                                  ip traffic-export apply TACCAPTURE size 10000000
                                                                                                !
                                                                                                !
                                                                                                enable:
                                                                                                traffic-export interface GigabitEthernet0/0 clear
                                                                                                traffic-export interface GigabitEthernet0/0 start
                                                                                        
                                                                                        
                                                                                                //Now make test call//
                                                                                        
                                                                                                traffic-export interface GigabitEthernet0/0 stop
                                                                                                traffic-export interface GigabitEthernet0/0 copy flash:
                                                                                                '''],
                                            'Packet capture from ISR G3 Gateway': ['''
                                                                                    ## Packet capture from ISR G3 Gateway:
                                                                            
                                                                                    monitor capture TAC interface gig0/0
                                                                                    monitor capture TAC buffer 10 ( in MB)
                                                                                    monitor capture TAC match ipv4 protocol udp any any
                                                                                    monitor capture TAC start

                                                                                    make a test call
                                                                            
                                                                                    monitor capture TAC stop
                                                                                    monitor capture TAC export flash:dtmf.pcap 
                                                                            
                                                                                    no monitor capture TAC ( To Remove the captures ) 
                                                                                    '''],
                                            'Procedure to collect packet captures from VG224': ['''
                                                                                                ## Procedure to collect packet captures from VG224:
                                                                                        
                                                                                                Embedded Packet Capture
                                                                                                • This command reference captures the interface GigabitEthernet 0/1 bidirectional.
                                                                                                • The capture buffer name in this scenario is capture-buff and the interface reference is capture-pt. !
                                                                                                • MS-2901#monitor capture buffer capture-buff size 4000 max-size 1500 linear
                                                                                                • MS-2901#monitor capture point ip cef capture-pt gigabitEthernet 0/1 both
                                                                                                • MS-2901#monitor capture point associate capture-pt capture-buff
                                                                                                • MS-2901#monitor capture point start all
                                                                                                • MS-2901#monitor capture point stop all
                                                                                                • MS-2901#monitor capture buffer capture-buff export tftp://10.10.101.10/capture.pcap  
                                                                                                '''],
                                            'Packet capture from Phone': ['''
                                                                            ## Packet capture on Phone:
                                                                            
                                                                            https://supportforums.cisco.com/document/44741/collecting-packet-capture-cisco-ip-phone
                                                                        '''],
                                            'Packet capture from CUCM': ['''
                                                                        ## Packet capture on CUCM:
                                                                
                                                                        utils network capture eth0 file packets count 100000 size all host ip <<IP of device>>
                                                                
                                                                        To stop the captures, press CTRL + C
                                                                
                                                                        Login to RTMT and select packet captures to download the captures.
                                                                
                                                                        https://supportforums.cisco.com/document/44376/packet-capture-cucm-appliance-model
                                                                        '''],
                                            'Packet capture settings for mirroring on switch': ['''
                                                                                                ## Packet capture settings for mirroring on switch:
                                                                                        
                                                                                                4507R#configure terminal
                                                                                                Enter configuration commands, one per line. End with CNTL/Z.
                                                                                        
                                                                                                4507R(config)#monitor session 1 source interface fastethernet 4/2
                                                                                        
                                                                                                !--- This configures interface Fast Ethernet 4/2 as source port.
                                                                                        
                                                                                                4507R(config)#monitor session 1 destination interface fastethernet 4/3
                                                                                        
                                                                                                !--- The configures interface Fast Ethernet 0/3 as destination port.
                                                                                        
                                                                                                4507R#show monitor session 1
                                                                                        
                                                                                                Session 1---------
                                                                                                Type : Local Session
                                                                                                Source Ports :
                                                                                                Both : Fa4/2
                                                                                                Destination Ports : Fa4/3
                                                                                        
                                                                                                4507R#
                                                                                                ******
                                                                                                '''],
                                            'PCM Capture from Voice Gateway': ['''
                                                                                ## PCM Capture:
                                                                        
                                                                                voice pcm capture buffer 200000
                                                                                voice pcm capture destination flash:pcm.dat << You can set the filename of your choice >>
                                                                                sh voice call status - to check the port it is hitting to use below
                                                                        
                                                                                test voice port 0/1/0:15.30 pcm-dump caplog 7 duration 255
                                                                                '''],
                                            'Triggered PCM captures from Gateway': ['''
                                                                                    ## Triggered PCM Capture on Cisco IOS Gateway
                                                                        
                                                                                    The triggered Cisco IOS PCM capture is a feature only available in Cisco IOS Release 15.2(2)T1 and later.
                                                                                    This feature, when enabled on a voice gateway, starts a PCM capture when the DTMF key *** (star, star, star) on a Cisco registered phone is pressed. Ensure the phone call from this phone traverses the gateway in question.
                                                                                    The PCM capture stops after the digits ### are entered on the captured phone.
                                                                                    This will not work for H323 call flows. It only works for SIP call flows.
                                                                                    There is an optional duration parameter that can be used to specify a specific capture duration after the triggered PCM capture is started. If this parameter is set to 0, the capture is infinite until stopped.
                                                                                    !
                                                                                    
                                                                                    voice pcm capture buffer 200000
                                                                                    
                                                                                    voice pcm capture destination tftp://x.x.x.x/
                                                                                    
                                                                                    voice pcm capture on-demand-trigger
                                                                                    
                                                                                    voice pcm capture user-trigger-string *** ### stream 7 duration 0
                                                                                    
                                                                                    press *** on the IP phone to start the capture
                                                                                    
                                                                                    press ### on the IP phone to Stop the capture
                                                                                    '''],
                                            'DSO dumps from Voice gateway': ['''
                                                                                ## DSO dumps:
                                                                        
                                                                                conf t
                                                                                monitor pcm-tracer
                                                                                monitor pcm-tracer profile 1
                                                                                capture-tdm E1 0/0/0 ds0 31
                                                                                exit
                                                                        
                                                                                monitor pcm-tracer capture-duration 2
                                                                                monitor pcm-tracer capture-destination flash0:pcmdata
                                                                                monitor pcm-tracer delayed-start 2
                                                                                exit
                                                                            '''],
                                            },
               'CUEAC': ['''      
                        1) Detailed CUCM CCM and CTI Logs
                        2) CUEAC TSP logs in location -- > C:/temp
                        3) CUEAC server logs in the below location %ALLUSERSPROFILE%\Cisco\CUACA
                        
                        On Server Side:
                        ==================
                        Set server logs to detail
                        - Go "Navigation" > go
                        - Click "Engineering"
                        - Click Logging Management
                        - Check all the options under "Cisco Unified Attendant Server"
                        - Change the Logging Level to "Full" on each option ir required, else Detailed(default) logging should also do.
                        
                        4) Operator logs
                        
                        On Client Side:
                        ===================
                        - Go to "Options"
                        - Click "Preferences"
                        - Click "Logging"
                        - Mark all check marks
                        ''']
                }
    
    options = ('CUCM',
               'Voice Gateway',
               'Unity Connection',
               'UCCX',
               'UCCE',
               'IM&P',
               'Expressway C & E',
               'Packet capture procedure',
               'CUEAC')
    st.subheader('Select Server/Device:')
    device = st.selectbox('',options = options)
    
    if device:
        
        trace_levels = trace_lookup[device]
        
        if type(trace_levels) == list:
            
            # st.code(trace_levels)
            info = nice_print(trace_levels)
            st.text(info)
        
        else:                    
            option_1 = st.selectbox('',options = trace_levels.keys())
    
            if type(trace_levels[option_1]) == list:
                
                # st.markdown(trace_levels[option_1])
                info = nice_print(trace_levels[option_1])
                st.text(info)
                
            else:
                option_2 = st.selectbox('',options = trace_levels[option_1].keys())
                
                if type(trace_levels[option_1][option_2]) == list:
                    
                    info = nice_print(trace_levels[option_1][option_2])
                    # st.code(info)
                    st.text(info)


elif mode == 'GW Debug':
    
    st.header('GW Log Parser')
    
    if 'info_button' not in st.session_state:
        st.session_state['info_button'] = 0
        
    if st.button('Info', help = 'Click to know pre-requisites'):
        
        if st.session_state['info_button'] == 0:
            st.session_state['info_button'] = 1
            st.text('''
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
            ''')
            
        elif st.session_state['info_button'] == 1:
            st.session_state['info_button'] = 0
            st.write('')
            
    log_file = st.file_uploader('Select GW Log file', type=['txt', 'log'])
    # file = []
    # for line in log_file:
    #     file.append(line.decode("utf-8"))
    if log_file is not None:
      
        # stringio = StringIO(log_file.getvalue().decode("utf-8"))
        
        file = str(log_file.read(),"utf-8").split("\n")
        # To read file as string:
        # file = stringio.read().split("\n")

        op_type, ca_type = st.columns([1,1])
        
        with op_type:
            st.session_state['operation_type'] = st.radio('Choose Call Flow', options = ['Incoming', 'Outgoing'], index= 0)
        
        with ca_type:
            
            if st.session_state['operation_type']:
                call_type_opt = call_type_option()
            
            if (call_type_opt == 'sip-isdn'
                or call_type_opt == 'isdn-sip'):
                call_type = '1'
            else:
                call_type = '2'
            
        # To read file
        if st.session_state['operation_type']=="Incoming":
            print('Processing Incoming call!')
            call_details = rx_call(file, call_type)    


        elif st.session_state['operation_type']=="Outgoing":
            print('Processing Outgoing call!')
            call_details = tx_call(file, call_type)
            
        # SHOW CALL DETAILS
        
        ccapi_list = []
        
        if (type(call_details) == str
            or call_details == None):
            st.code(call_details)
            
        else:
            
            for index, local_call in call_details.items():
                # st.text("-------"+str(index+1)+" Of " + str(len(call_details))+"-------")
                
                # st.text(index)
                # st.code(call_details)
                code = []
                code.append("-------"+str(index+1)+" Of " + str(len(call_details))+"-------")
                
                # st.text(local_call.items())
                for key, value in local_call.items():                    
                    # st.text(key)
                    # st.text(value)
                    if key=="ccapi_value":
                        if type(value) == list:
                            
                            st.text(key + " : " + value[0])
                            code.append(key + " : " + value[0])
                            
                            ccapi_list.append(str(index+1) + ' : ' + str(value[0]))
                        
                        else:
                            st.text(key + " : " + value)
                            code.append(key + " : " + value)
                            
                            ccapi_list.append(str(index+1) + ' : ' + str(value))
                        
                    else:
                        # st.text(key + " : " + str(value))
                        code.append(key + " : " + str(value))
                
                # if 'info' not in st.session_state:
                #     info = nice_print(code)
                #     st.session_state['info'] = info
                
                # st.code(st.session_state['info'])
                
                info = nice_print(code)
                st.code(info)
                        
            call_id = st.selectbox("Enter a CCAPI value  to see details: ", options = ccapi_list)
           
            ccapi_value = call_id.split(":")[1].strip()
            
            if (call_id
                and st.session_state['operation_type']=="Outgoing"):
                
                # st.text(ccapi_value)
                tx_analysis = tx_analyse(ccapi_value, call_details, file)
                tx_info = nice_print(tx_analysis)
                st.code(tx_info)
                
            elif (call_id
                  and st.session_state['operation_type']=="Incoming"
                  and call_type == '1'):
                rx_analysis_isdn = rx_analyse_1(ccapi_value, call_details, file)
                rx_info_isdn = nice_print(rx_analysis_isdn)
                st.code(rx_info_isdn)
            
            elif (call_id
                  and st.session_state['operation_type']=="Incoming"
                  and call_type == '2'):
                rx_analysis_sip = rx_analyse_2(ccapi_value, call_details, file)
                rx_info_sip = nice_print(rx_analysis_sip)
                st.code(rx_info_sip)
            
        # if type(local_call) == str:
        #     st.text(local_call)
        
        #     # for key, value in local_call.items():
        #     #     st.text(key + " : " , value)
                    
        #     call_id = st.selectbox("Enter a ccapi value value to see details: ", options = local_call.keys())
        
        