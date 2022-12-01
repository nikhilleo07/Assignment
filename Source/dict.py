'''Function for fetching vendor details'''
venodr_dict={'c8:4b:d6':'DELL',
    '18:68:cb':'HANGZHOU',
    'b8:27:eb':'RASPBERRY',
    'bc:5f:f4':'ASROCK',
    'a4:4c:c8':'DELL',
    'c0:25:a5':'DELL',}

def find_vend(mac_addr):
    """Function for fetching vendor details"""
    try:
        dev=venodr_dict[mac_addr]
    except Exception as err:
        return err
    return dev


if __name__ == '__main__':
    print("This module executes as a standalone script")
    MAC_ADDRESS = str(input("Please enter the Full Mac address details, exp b8:27:eb:b4:81:6d : "))
    OUI=MAC_ADDRESS[0:8]
    print(f"MacAddress : {(MAC_ADDRESS)} Vendor : {find_vend(OUI)}")
else:
    pass
