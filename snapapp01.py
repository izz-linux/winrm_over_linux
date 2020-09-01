#!/usr/bin/python3

import winrm
import base64

def decode_pass(encoded_pass):
    decoded_pass = base64.b64decode(encoded_pass)
    return decoded_pass.decode('utf-8')


def main():

    clear_pass = decode_pass('*************')
    #print('The value of the password is: {}'.format(clear_pass))
    winrmsession = winrm.Session('RXMSAUTO01',auth=('rxscripter','{}'.format(clear_pass)))
    result = winrmsession.run_ps('C:\scripts\snapshotVM.ps1 GC RXAPP01 Snapshot')
    yesno = result.std_out
    yesno = yesno.decode('utf-8')

    with open ('Results.log', 'w') as log_file:
        print('The following snapshots are currently available for RXAPP01:\n{}'.format(yesno), file=log_file)
    

if __name__ == "__main__":
    main()
