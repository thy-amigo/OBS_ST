from lxml import etree
from requests import Session
from requests.auth import HTTPBasicAuth
import sys
import urllib3
import time
from zeep import Client, Settings, Plugin, xsd
from zeep.transports import Transport
from zeep.exceptions import Fault

# Edit .env file to specify your Webex site/user details
import os
# os.chdir(r'D:\Python\Anaconda Project\nornir\cucm_axl')
# os.getcwd()

# from dotenv import load_dotenv
# load_dotenv()

# Change to true to enable output of request/response headers and XML
DEBUG = False

# The WSDL is a local file in the working directory, see README

# print(os.path.dirname(__file__))
WSDL_FILE = os.path.dirname(__file__) + '/schema/AXLAPI.wsdl'
# print('WSDL FIlE: ', WSDL_FILE)
# This class lets you view the incoming and outgoing http headers and XML

class MyLoggingPlugin( Plugin ):

    def egress( self, envelope, http_headers, operation, binding_options ):

        # Format the request body as pretty printed XML
        xml = etree.tostring( envelope, pretty_print = True, encoding = 'unicode')

        print( f'\nRequest\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}' )

    def ingress( self, envelope, http_headers, operation ):

        # Format the response body as pretty printed XML
        xml = etree.tostring( envelope, pretty_print = True, encoding = 'unicode')

        print( f'\nResponse\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}' )


# The first step is to create a SOAP client session
session = Session()

# We avoid certificate verification by default
# And disable insecure request warnings to keep the output clear
session.verify = False
urllib3.disable_warnings( urllib3.exceptions.InsecureRequestWarning )

# To enable SSL cert checking (recommended for production)
# place the CUCM Tomcat cert .pem file in the root of the project
# and uncomment the two lines below

# CERT = 'changeme.pem'
# session.verify = CERT

session.auth = HTTPBasicAuth( os.getenv( 'AXL_USERNAME' ), os.getenv( 'AXL_PASSWORD' ) )

transport = Transport( session = session, timeout = 10 )

# strict=False is not always necessary, but it allows Zeep to parse imperfect XML
settings = Settings( strict = False, xml_huge_tree = True )

# If debug output is requested, add the MyLoggingPlugin callback
plugin = [ MyLoggingPlugin() ] if DEBUG else []

# Create the Zeep client with the specified settings
client = Client( WSDL_FILE, settings = settings, transport = transport,
        plugins = plugin )

# Create the Zeep service binding to AXL at the specified CUCM
service = client.create_service('{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',
                                f'https://{os.getenv("CUCM_ADDRESS")}:8443/axl/')

def get_load(name):
    
    try:
        resp = service.getPhone(name= name)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
    
    print(f'\nPhone Load on Device({name}): ', resp['return']['phone']['loadInformation']['_value_1'])


def get_line(dn):
    
    try:
        resp = service.getLine(pattern = dn, routePartitionName='None')
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
    
    print(f'\nLine details for ({dn}): ', resp)


def get_phone(name):
    
    try:
        resp = service.getPhone(name= name)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
    
    print(f'\nPhone Load on Device({name}): ', resp['return']['phone'])
        
    
def update_load(name, load):
    
    try:
        resp = service.updatePhone(name= name, loadInformation = load)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
        
    print(f'\n[Update PhoneLoad] on Device: {name}')

def read_vendorconfig(resp):
    for elem in resp['return']['phone']['vendorConfig']._value_1:
    
        if elem.find( '*' ) is None:
            print( f'{ elem.tag }: { elem.text }' )
        else:

            print( f'{ elem.tag }:' )

            for subElem in elem.findall( '*' ):
                print( f'\t{ subElem.tag }: { subElem.text }' )

def update_vendorconfig(name, param, value):
    
    
    try:
        resp = service.getPhone(name= name)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
    
    vconfig = resp['return']['phone']['vendorConfig']['_value_1']
    
    
    for elem in vconfig:
        if elem.tag == param:
            print(f'\n[Current Value] of {param} : ', elem.text)
            elem.text = value
            
            print(f'\n[Updated Value] of {param} : ', elem.text)

    vendorConfig = vconfig    
        
    # CREATE UI ELEMENT FOR VENDORCONFIG
    # webex_join = etree.Element( 'UIFeaturesCallJoinWebex' )
    # webex_join.text = 'Hidden'
    
    # # Append each top-level element to an array
    # vendorConfig = []
    # vendorConfig.append( webex_join )
    

    # Create a Zeep xsd type object of type XVendorConfig from the client object
    xvcType = client.get_type( 'ns0:XVendorConfig' )

    # Use the XVendorConfig type object to create a vendorConfig object
    #   using the array of vendorConfig elements from above, and set as
    #   phone.vendorConfig
    config = xvcType( vendorConfig )
        
    try:
        resp = service.updatePhone(name = name, vendorConfig = config)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
        
    print(f'\n{param} updated on Device : {name}')
 

def apply_config(name):
    
    try:
        resp = service.applyPhone(name= name)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
        
    print(f'\n[Apply Config] on Device : {name}')


def reset_device(name):
    
    try:
        resp = service.resetPhone(name= name)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
        
    print(f'\n[Reset Device] : {name}')
    
def add_phone(mac,
              description,
              device_pool,
              device_type,
              sec_profile,
              sip_profile,
              dn,
              line_display,
              location,
              ep_user,
              ep_pass,
              route_partition = None,
              line_css = None,
              rate = '2048',
              phonebook_server_type = 'UDS',
              phonebook_server = ''):
    
    line = {
            'pattern': dn,
            'description': line_display,
            'alertingName': line_display,
            'asciiAlertingName': line_display,
            'usage': 'Device',
            'routePartitionName': route_partition,
            'callForwardAll': {
                'forwardToVoiceMail': 'false'
                },
            'shareLineAppearanceCssName': line_css
            }
    
    # Execute the addLine request
    try:
        resp = service.addLine( line )
    
    except Fault as err:
        print( f'Zeep error: addLine: { err }' )
        sys.exit( 1 )
        
    print(f'\nAdded Line: {dn}')
    
    time.sleep(1)
    
    ## SAMPLE PHONE CONFIG
    '''
    {
            'name': 'SEP'+mac,
            'product': device_type,
            'description': description,
            'model': xsd.SkipValue,
            'class': 'Phone',
            'protocol': 'SIP',
            'protocolSide': 'User',
            'devicePoolName': 'Default',
            'locationName': location,
            'securityProfileName': sec_profile,
            'sipProfileName': sip_profile,
            'commonPhoneConfigName': xsd.SkipValue,
            'phoneTemplateName': xsd.SkipValue,
            'primaryPhoneName': xsd.SkipValue,
            'useTrustedRelayPoint': xsd.SkipValue,
            'builtInBridgeStatus': xsd.SkipValue,
            'packetCaptureMode': xsd.SkipValue,
            'certificateOperation': xsd.SkipValue,
            'deviceMobilityMode': xsd.SkipValue,
            'lines': {
                'line': [
                    {
                        'index': '1',
                        'display': line_display,
                        'dirn': {
                            'pattern': dn,
                            'routePartitionName': route_partition,
                            },
                        'displayAscii': line_display,
                        'e164Mask': dn
                        
                        }
                    ]
                }
            }
    
    '''
    
    
    phone = {
            'name': 'SEP'+mac,
            'product': device_type,
            'description': description,
            'model': xsd.SkipValue,
            'class': 'Phone',
            'protocol': 'SIP',
            'protocolSide': 'User',
            'devicePoolName': 'Default',
            'locationName': location,
            'securityProfileName': sec_profile,
            'sipProfileName': sip_profile,
            'commonPhoneConfigName': xsd.SkipValue,
            'phoneTemplateName': xsd.SkipValue,
            'primaryPhoneName': xsd.SkipValue,
            'useTrustedRelayPoint': xsd.SkipValue,
            'builtInBridgeStatus': xsd.SkipValue,
            'packetCaptureMode': xsd.SkipValue,
            'certificateOperation': xsd.SkipValue,
            'deviceMobilityMode': xsd.SkipValue,
            'lines': {
                'line': [
                    {
                        'index': '1',
                        'display': line_display,
                        'dirn': {
                            'pattern': dn,
                            'routePartitionName': route_partition,
                            },
                        'displayAscii': line_display
                        
                        }
                    ]
                }
            }
    
    # CREATE VENDORCONFIG
    web_access = etree.Element( 'webAccess' )
    web_access.text = '0'
    
    
    ssh_access = etree.Element( 'sshAccess' )
    ssh_access.text = '0'
    
    
    down_rate = etree.Element( 'MaxTotalDownstreamRate' )
    down_rate.text = rate
    
    up_rate = etree.Element( 'MaxTotalUpstreamRate' )
    up_rate.text = rate
    
    sys_name = etree.Element( 'SystemName' )
    sys_name.text = description
    
    pb_type = etree.Element( 'AlternatePhonebookServerType' )
    pb_type.text = phonebook_server_type
    
    pb_server = etree.Element( 'AlternatePhonebookServerAddress' )
    pb_server.text = phonebook_server
    
    facility_grp = etree.Element( 'FacilityServiceGroup' )
    facility_type = etree.SubElement( facility_grp, 'FacilityServiceType' )
    facility_name = etree.SubElement( facility_grp, 'FacilityServiceName' )
    facility_number = etree.SubElement( facility_grp, 'FacilityServiceNumber' )
    facility_call_type = etree.SubElement( facility_grp, 'FacilityServiceCallType' )
    facility_type.text = 'Helpdesk'
    facility_name.text = 'Helpdesk'
    facility_number.text = '0170480368'
    facility_call_type.text = 'Audio'  
    
    login_grp = etree.Element( 'AdminLoginDetails' )
    login_user = etree.SubElement( login_grp, 'adminUserId' )
    login_pass = etree.SubElement( login_grp, 'adminPassword' )
    
    login_user.text = ep_user
    login_pass.text = ep_pass
    
    # Append each top-level element to an array
    vendorConfig = []
    vendorConfig.append( web_access )
    vendorConfig.append( ssh_access )
    vendorConfig.append( down_rate )
    vendorConfig.append( up_rate )
    vendorConfig.append( sys_name )
    vendorConfig.append( pb_type )
    vendorConfig.append( pb_server )
    vendorConfig.append( facility_grp )
    vendorConfig.append( login_grp )
    
    
    # Create a Zeep xsd type object of type XVendorConfig from the client object
    xvcType = client.get_type( 'ns0:XVendorConfig' )
    
    # Use the XVendorConfig type object to create a vendorConfig object
    #   using the array of vendorConfig elements from above, and set as
    #   phone.vendorConfig
    phone['vendorConfig'] = xvcType( vendorConfig )
    
    print(f'\nPhone Details: {phone}')
    
    
    try:
        resp = service.addPhone(phone)
        #resp = service.getDeviceProfile(name= name)
    except Exception as err:
        print( f'\nZeep error: GetDeviceProfile: { err }' )
        sys.exit( 1 )
        
    print(f'\nAdded Device: {description}')
    
class Arms_session:
    
    def __init__(self):

        pass

    def login(self, ip, ver):
        
        # self.dotenv_file = os.getcwd() +'\\1.env' #os.path.dirname(sys.argv[0])+'\\1.env'
        # load_dotenv(self.dotenv_file, override=True)
        
        cucm_ip = ip
        # The WSDL is a local file in the working directory, see README
        WSDL_FILE = f'{os.path.dirname(__file__)}/schema/{ver}/AXLAPI.wsdl'
        
        print(WSDL_FILE)
        
        # print(os.environ['AXL_USERNAME'])
        # print(os.environ['AXL_PASSWORD'])
        # The first step is to create a SOAP client session
        session = Session()

        # We avoid certificate verification by default
        # And disable insecure request warnings to keep the output clear
        session.verify = False
        urllib3.disable_warnings( urllib3.exceptions.InsecureRequestWarning )

        session.auth = HTTPBasicAuth( os.getenv( 'AXL_USERNAME' ), os.getenv( 'AXL_PASSWORD' ) )

        transport = Transport( session = session, timeout = 10 )

        # strict=False is not always necessary, but it allows Zeep to parse imperfect XML
        settings = Settings( strict = False, xml_huge_tree = True )

        # If debug output is requested, add the MyLoggingPlugin callback
        plugin = [ MyLoggingPlugin() ] if DEBUG else []

        # Create the Zeep client with the specified settings
        client = Client( WSDL_FILE, settings = settings, transport = transport,
                plugins = plugin )

        # Create the Zeep service binding to AXL at the specified CUCM
        self.service = client.create_service('{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',
                                        f'https://{cucm_ip}:8443/axl/')

    def get_appuser(self, user):
    
        try:
            resp = self.service.getAppUser(userid = user)
        except Exception as err:
            
            if 'not found' in str(err):
                print('\n[User Not Found]: Users Doesnt Exists!')
                resp = 404
            
            else:                
                print( f'\nZeep error: getAppUser: { err }' )
                sys.exit( 1 )
            
        return resp
        print(f'\nAppUser details for ({user}): ', resp)
    
    def add_appuser(self, user, password, groups = None):
        
        app_user = {
            'userid': user,
            'password': password,
            'associatedGroups': {              
            }
        }
        
        usergroup = {'userGroup': groups}
        app_user['associatedGroups'] = usergroup
    
        # Execute the addAppUser request
        try:
            resp = self.service.addAppUser( app_user )
            
        except Exception as err:
            
            if 'duplicate value' in str(err):
                print('\n[Duplicate User]: Users Exists!')
            
            else:                
                print("\nZeep error: addAppUser: {0}".format( err ) )
                sys.exit( 1 )
        
        print( "\naddAppUser response:\n" )
        print( resp,"\n" )
    
    def del_appuser(self, user):
        
        app_user = user
        
        try:
            resp = self.service.removeAppUser( userid = app_user )
        except Exception as err:
            if 'not found' in str(err):
                print('\n[User Not Found]: Users Doesnt Exists!')
                resp = 404
            
            else:
                print("\nZeep error: RemoveAppUser: {0}".format( err ) )
                sys.exit( 1 )
    
        print( "\nRemoveAppUser response:\n" )
        print( resp,"\n" )
            
    def get_siptrunk(self, uid):
        
        try:
            resp = self.service.getSipTrunk(uuid  = uid)
        except Exception as err:
            if 'not found' in str(err):
                print('\n[User Not Found]: SIP Trunk Exists!')
                resp = 404
            
            else:
                print("\nZeep error: Get Sip Trunk: {0}".format( err ) )
                sys.exit( 1 )
        
        return resp
    
        print( "\nGet SIP Trunk response:\n" )
        print( resp,"\n" )
    
    def get_listSipTrunk(self):
        
        try:
            resp = self.service.listSipTrunk(searchCriteria = { 'name': '%' }, returnedTags = { 'name': xsd.String })
            
        except Exception as err:
            if 'not found' in str(err):
                print('\n[User Not Found]: SIP Trunk Exists!')
                resp = 404
            
            else:
                print("\nZeep error: Get Sip Trunk: {0}".format( err ) )
                sys.exit( 1 )
        
        return resp
        print( "\nGet SIP Trunk response:\n" )
        print( resp,"\n" )
        
if __name__ == '__main__':
    
    # get_phone('SEPAABBCCDDFFAA')
    
    # get_line('33155235595')
    os.environ['AXL_USERNAME'] = 'jarvis_axl'
    os.environ['AXL_PASSWORD'] = 'Qazwsx@123456'
    arms_task = Arms_session()
    arms_task.login('192.168.82.10', '12.5')
    sample_user_resp = arms_task.get_listSipTrunk()
    sample_sip_resp = arms_task.get_siptrunk('A0B8BF64-2545-CA18-C3DA-0E8F7FBEDB56')
    print(sample_user_resp)
    print(sample_sip_resp)