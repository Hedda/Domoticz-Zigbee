#!/usr/bin/env python3
# coding: utf-8 -*-
#
# Author: zaraki673 & pipiche38
#
"""
    Module: schneider_wiser.py

    Description: 

"""

from time import time
import json
import os.path

import Domoticz
import Modules.output
import struct

from Modules.logging import loggingOutput
from Modules.zigateConsts import ZIGATE_EP,MAX_LOAD_ZIGATE


def pollingSchneider( self, key ):

    """
    This fonction is call if enabled to perform any Manufacturer specific polling action
    The frequency is defined in the pollingSchneider parameter (in number of seconds)
    """

    rescheduleAction = False

    return rescheduleAction


def callbackDeviceAwake_Schneider(self, NwkId, EndPoint, cluster):

    """
    This is fonction is call when receiving a message from a Manufacturer battery based device.
    The function is called after processing the readCluster part
    """

    Domoticz.Log("callbackDeviceAwake_Schneider - Nwkid: %s, EndPoint: %s cluster: %s" \
            %(NwkId, EndPoint, cluster))
    if cluster == '0201':
        callbackDeviceAwake_Schneider_SetPoints( self, NwkId, EndPoint, cluster)

    return

def callbackDeviceAwake_Schneider_SetPoints( self, NwkId, EndPoint, cluster):

    # Schneider Wiser Valve Thermostat is a battery device, which receive commands only when it has sent a Report Attribute
    if 'Model' in self.ListOfDevices[NwkId]:
        if self.ListOfDevices[NwkId]['Model'] == 'EH-ZB-VACT':
            now = time()
            # Manage SetPoint
            if '0201' in self.ListOfDevices[NwkId]['Ep'][EndPoint]:
                if '0012' in self.ListOfDevices[NwkId]['Ep'][EndPoint]['0201']:
                    if 'Schneider' not in self.ListOfDevices[NwkId]:
                        self.ListOfDevices[NwkId]['Schneider'] = {}
                    if 'Target SetPoint' in self.ListOfDevices[NwkId]['Schneider']:
                        if self.ListOfDevices[NwkId]['Schneider']['Target SetPoint'] and self.ListOfDevices[NwkId]['Schneider']['Target SetPoint'] != int( self.ListOfDevices[NwkId]['Ep'][EndPoint]['0201']['0012'] * 100):
                            # Protect against overloading Zigate
                            if now > self.ListOfDevices[NwkId]['Schneider']['TimeStamp SetPoint'] + 15:
                                schneider_setpoint( self, NwkId, self.ListOfDevices[NwkId]['Schneider']['Target SetPoint'] )

            # Manage Zone Mode
                if 'e010' in self.ListOfDevices[NwkId]['Ep'][EndPoint]['0201']:
                    if 'Target Mode' in self.ListOfDevices[NwkId]['Schneider']:
                        EHZBRTS_THERMO_MODE = { 0: 0x00, 10: 0x01, 20: 0x02, 30: 0x03, 40: 0x04, 50: 0x05, 60: 0x06, }
                        if self.ListOfDevices[NwkId]['Schneider']['Target Mode'] is not None:
                            if EHZBRTS_THERMO_MODE[self.ListOfDevices[NwkId]['Schneider']['Target Mode']] == int(self.ListOfDevices[NwkId]['Ep'][EndPoint]['0201']['e010'],16):
                                self.ListOfDevices[NwkId]['Schneider']['Target Mode'] = None
                                self.ListOfDevices[NwkId]['Schneider']['TimeStamp Mode'] = None
                            else:
                                if now > self.ListOfDevices[NwkId]['Schneider']['TimeStamp Mode'] + 15:
                                    schneider_EHZBRTS_thermoMode( self, NwkId, self.ListOfDevices[NwkId]['Schneider']['Target Mode'] )


    return

def schneider_wiser_registration( self, key ):
    """
    This method is called during the pairing/discovery process.
    Purpose is to do some initialisation (write) on the coming device.
    """

    loggingOutput( self, 'Log', "schneider_wiser_registration for device %s" %key)

    EPout = '01'
    for tmpEp in self.ListOfDevices[key]['Ep']:
        if "0000" in self.ListOfDevices[key]['Ep'][tmpEp]:
            EPout= tmpEp

    if 'Model' not in self.ListOfDevices[key]:
        Domoticz.Error("Undefined Model, registration !!!")
        return

    # Set Commissioning as Done
    manuf_id = "105e"
    manuf_spec = "01"
    cluster_id = "%04x" %0x0000
    Hattribute = "%04x" %0xe050
    data_type = "10" # Bool
    data = "%02x" %True
    loggingOutput( self, 'Log', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
            %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
    Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)

    if self.ListOfDevices[key]['Model'] == 'EH-ZB-RTS': # Thermostat
        # Set Language
        manuf_id = "105e"
        manuf_spec = "01"
        cluster_id = "%04x" %0x0000
        Hattribute = "%04x" %0x5011
        data_type = "42" # String
        data = '656e'  # 'en'
        loggingOutput( self, 'Log', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
                %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
        Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)


    if self.ListOfDevices[key]['Model'] in ( 'EH-ZB-VACT'): # Thermostatic Valve
        cluster_id = "%04x" %0x0201
        manuf_id = "0000"
        manuf_spec = "00"
        # Set 0x01 to 0x0201/0xe013 : ATTRIBUTE_THERMOSTAT_OPEN_WINDOW_DETECTION_THRESHOLD
        Hattribute = "%04x" %0xe013
        data_type = "20"
        # 0x00  After a first Pairing
        # 0x04  After a restart of the Hub or when changing battery of Valve
        data = '00'  
        loggingOutput( self, 'Log', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
                %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
        Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)

    if self.ListOfDevices[key]['Model'] in ( 'EH-ZB-HACT', 'EH-ZB-VACT' ): # Actuator, Valve
        # Set no Calibration
        manuf_id = "0000"
        manuf_spec = "00"
        cluster_id = "%04x" %0x0201
        # Set 0x00 to 0x0201/0x0010
        Hattribute = "%04x" %0x0010
        data_type = "28" 
        data = '00'  
        loggingOutput( self, 'Log', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
                %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
        Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)

    if self.ListOfDevices[key]['Model'] in ( 'EH-ZB-HACT', 'EH-ZB-VACT'): # Actuator 
        # ATTRIBUTE_THERMOSTAT_ZONE_MODE
        cluster_id = "%04x" %0x0201
        manuf_id = "105e"
        manuf_spec = "01"
        # Set 0x01 to 0x0201/0xe010
        Hattribute = "%04x" %0xe010
        data_type = "30"
        # 0x01 User Mode Manual
        # 0x02 User Mode Schedule
        # 0x03 User Mode Manual Energy Saver
        data = '01'  
        loggingOutput( self, 'Log', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
                %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
        Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)

    if self.ListOfDevices[key]['Model'] in ( 'EH-ZB-HACT' ): # Actuator
        # ATTRIBUTE_THERMOSTAT_HACT_CONFIG
        cluster_id = "%04x" %0x0201
        manuf_id = "105e"
        manuf_spec = "01"
        # Set 0x01 to 0x0201/0xe011
        Hattribute = "%04x" %0xe011
        data_type = "18"
        data = '03'   # By default register as CONVENTIONEL mode
                      # E attente pour @hairv en FIP
        loggingOutput( self, 'Log', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
            %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
        Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)

    # Write Location to 0x0000/0x5000 for all devices
    manuf_id = "0000"
    manuf_spec = "00"
    cluster_id = "%04x" %0x0000
    Hattribute = "%04x" %0x0010
    data_type = "42"
    data = 'Zigate zone'.encode('utf-8').hex()  # Zigate zone 
    loggingOutput( self, 'Debug', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
            %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
    Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)

    #if self.ListOfDevices[key]['Model'] in ( 'EH-ZB-VACT' ): # Valve
    #    setpoint = 2000
    #    if 'Schneider' in self.ListOfDevices[key]:
    #        if 'Target SetPoint' in self.ListOfDevices[key]['Schneider']:
    #            if self.ListOfDevices[key]['Schneider']['Target SetPoint'] is not Null:
    #                setpoint = self.ListOfDevices[key]['Schneider']['Target SetPoint']
    #
    #    schneider_setpoint( self, key, setpoint)
    #    self.ListOfDevices[key]['Heartbeat'] = 0

    if self.ListOfDevices[key]['Model'] in ( 'EH-ZB-LMACT'): # Pilotage Chaffe eau
        Modules.output.sendZigateCmd(self, "0092","02" + key + ZIGATE_EP + EPout + "01")
        Modules.output.sendZigateCmd(self, "0092","02" + key + ZIGATE_EP + EPout + "00")
        self.ListOfDevices[key]['Heartbeat'] = 0

def schneider_thermostat_behaviour( self, key, mode ):
    """
    Allow switching between Conventionel and FIP mode
    Set 0x0201/0xe011
    HAC into Fil Pilot FIP 0x03, in Covential Mode 0x00
    """

    MODE = { 'conventionel': 0x00, 'setpoint' : 0x02, 'FIP': 0x03 }

    loggingOutput( self, 'Log', "schneider_thermostat_behaviour for device %s requesting mode: %s" %(key, mode))
    if mode not in MODE:
        Domoticz.Error("schneider_thermostat_behaviour - %s unknown mode %s" %(key, mode))
        return

    EPout = '01'
    for tmpEp in self.ListOfDevices[key]['Ep']:
        if "0000" in self.ListOfDevices[key]['Ep'][tmpEp]:
            EPout= tmpEp
    manuf_id = "105e"
    manuf_spec = "01"
    cluster_id = "%04x" %0x0201
    Hattribute = "%04x" %0xe011
    data_type = "18"
    data = '%02X' %MODE[ mode ]
    loggingOutput( self, 'Log', "Schneider Write Attribute %s with value %s / cluster: %s, attribute: %s type: %s"
            %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
    Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)
    # Reset Heartbeat in order to force a ReadAttribute when possible
    self.ListOfDevices[key]['Heartbeat'] = 0

def schneider_fip_mode( self, key, mode):

    # APS Data: 0x00 0x0b 0x01 0x02 0x04 0x01 0x0b 0x45 0x11 0xc1 0xe1 0x00 0x01 0x03

    MODE = { 'Confort': 0x00,
            'Confort -1': 0x01,
            'Confort -2': 0x02,
            'Eco': 0x03,
            'Frost Protection': 0x04,
            'Off': 0x05 }

    if mode not in MODE:
        Domoticz.Error("schneider_fip_mode - %s unknown mode: %s" %mode)

    # determine which Endpoint
    EPout = '01'
    for tmpEp in self.ListOfDevices[key]['Ep']:
        if "0201" in self.ListOfDevices[key]['Ep'][tmpEp]:
            EPout= tmpEp

    # Make sure that we are in FIP Mode
    setFIPModeRequired = True
    if EPout in self.ListOfDevices[ key ]['Ep']:
        if '0201' in  self.ListOfDevices[ key ]['Ep'][EPout]:
            if 'e011' in  self.ListOfDevices[ key ]['Ep'][EPout]['0201']:
                if self.ListOfDevices[ key ]['Ep'][EPout]['0201'] == '03':
                    setFIPModeRequired = False

    if setFIPModeRequired:
        schneider_thermostat_behaviour( self, key, 'FIP')

    cluster_frame = '11'
    sqn = '00'
    if 'SQN' in self.ListOfDevices[key]:
        if self.ListOfDevices[key]['SQN'] != {} and self.ListOfDevices[key]['SQN'] != '':
            sqn = '%02x' %(int(self.ListOfDevices[key]['SQN'],16) + 1)
    cmd = 'e1'

    zone_mode = '01' # Heating
    fipmode = '%02X' %MODE[ mode ]
    prio = '01' # Prio

    payload = cluster_frame + sqn + cmd + zone_mode + fipmode + prio + 'ff'

    Modules.output.raw_APS_request( self, key, EPout, '0201', '0104', payload, zigate_ep=ZIGATE_EP)
    self.ListOfDevices[key]['Heartbeat'] = 0


def schneider_setpoint_thermostat( self, key, setpoint):

    EPout = '0b'
    ClusterID = '0201'
    attr = '0012'
    NWKID = key
    if EPout not in self.ListOfDevices[NWKID]['Ep']:
        self.ListOfDevices[NWKID]['Ep'][EPout] = {}
    if ClusterID not in self.ListOfDevices[NWKID]['Ep'][EPout]:
        self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID] = {}
    if not isinstance( self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID] , dict):
        self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID] = {}
    if attr not in self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID]:
        self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID][attr] = {}
    if 'Ep' in self.ListOfDevices[NWKID]:
        if EPout in self.ListOfDevices[NWKID]['Ep']:
            if ClusterID in self.ListOfDevices[NWKID]['Ep'][EPout]:
                if attr in self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID]:
                    self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID][attr] = setpoint
    importSchneiderZoning(self)
    for zone in self.SchneiderZone:
        loggingOutput(self, 'Log', "schneider_setpoint - Zone Information: %s " %zone )
        if self.SchneiderZone[ zone ]['Thermostat']['NWKID'] == NWKID :
            loggingOutput( self, 'Log', "schneider_setpoint - found %s " %zone )
            for hact in self.SchneiderZone[ zone ]['Thermostat']['HACT']:
                loggingOutput( self, 'Log', "schneider_setpoint - found hact %s " %hact )
                schneider_setpoint_actuator(self, hact, setpoint)


def schneider_setpoint_actuator( self, key, setpoint):
    # SetPoint 21°C ==> 2100 => 0x0834
    # APS Data: 0x00 0x0b 0x01 0x02 0x04 0x01 0x0b 0x45 0x11 0xc1 0xe0 0x00 0x01 0x34 0x08 0xff
    #                                                                            |---------------> LB HB Setpoint
    #                                                             |--|---------------------------> Command 0xe0
    #                                                        |--|--------------------------------> SQN
    #                                                   |--|-------------------------------------> Cluster Frame

    cluster_frame = '11'
    sqn = '00'
    if 'SQN' in self.ListOfDevices[key]:
        if self.ListOfDevices[key]['SQN'] != {} and self.ListOfDevices[key]['SQN'] != '':
            sqn = '%02x' % (int(self.ListOfDevices[key]['SQN'],16) + 1)
    cmd = 'e0'

    setpoint = int(( setpoint * 2 ) / 2)   # Round to 0.5 degrees
    if 'Schneider' not in self.ListOfDevices[key]:
        self.ListOfDevices[key]['Schneider'] = {}
    self.ListOfDevices[key]['Schneider']['Target SetPoint'] = setpoint
    self.ListOfDevices[key]['Schneider']['TimeStamp SetPoint'] = int(time())

    setpoint = '%04X' %setpoint
    zone = '01'

    payload = cluster_frame + sqn + cmd + '00' + zone + setpoint[2:4] + setpoint[0:2] + 'ff'

    EPout = '01'
    for tmpEp in self.ListOfDevices[key]['Ep']:
        if "0201" in self.ListOfDevices[key]['Ep'][tmpEp]:
            EPout= tmpEp

    Modules.output.raw_APS_request( self, key, EPout, '0201', '0104', payload, zigate_ep=ZIGATE_EP)
    self.ListOfDevices[key]['Heartbeat'] = 0


def schneider_setpoint( self, key, setpoint):

    if 'Model' in self.ListOfDevices[key]:
        if self.ListOfDevices[key]['Model'] == 'EH-ZB-RTS':
            schneider_setpoint_thermostat(self, key, setpoint)
        else:
            schneider_setpoint_actuator( self,key, setpoint)


def schneider_temp_Setcurrent( self, key, setpoint):

    # SetPoint 21°C ==> 2100 => 0x0834
    # APS Data: 0x00 0x0b 0x01 0x02 0x04 0x01 0x0b 0x45 0x11 0xc1 0xe0 0x00 0x01 0x34 0x08 0xff
    #                                                                            |---------------> LB HB Setpoint
    #                                                             |--|---------------------------> Command 0xe0
    #                                                        |--|--------------------------------> SQN
    #                                                   |--|-------------------------------------> Cluster Frame

    cluster_frame = '18'
    attr = '0000'
    sqn = '00'
    dataType = '29'
    if 'SQN' in self.ListOfDevices[key]:
        if self.ListOfDevices[key]['SQN'] != {} and self.ListOfDevices[key]['SQN'] != '':
            sqn = '%02x' % (int(self.ListOfDevices[key]['SQN'],16) + 1)
    cmd = '0a'

    setpoint = int(( setpoint * 2 ) / 2)   # Round to 0.5 degrees
    setpoint = '%04X' %setpoint

    payload = cluster_frame + sqn + cmd + attr + dataType + setpoint[2:4] + setpoint[0:2] 

    EPout = '01'
    for tmpEp in self.ListOfDevices[key]['Ep']:
        if "0402" in self.ListOfDevices[key]['Ep'][tmpEp]:
            EPout= tmpEp

    Modules.output.raw_APS_request( self, key, EPout, '0402', '0104', payload, zigate_ep=ZIGATE_EP)
    self.ListOfDevices[key]['Heartbeat'] = 0



def schneider_EHZBRTS_thermoMode( self, key, mode):


    # Attribute 0x0201 / 0xE010 ==> 0x01 ==> Mode Manuel   / Data Type 0x30
    #                               0x02 ==> Mode Programme
    #                               0x03 ==> Mode Economie
    #                               0x06 ==> Mode Vacances
    
    EHZBRTS_THERMO_MODE = { 0: 0x00,
            10: 0x01,
            20: 0x02,
            30: 0x03,
            40: 0x04,
            50: 0x05,
            60: 0x06,
            }


    Domoticz.Log("schneider_EHZBRTS_thermoMode - %s Mode: %s" %(key, mode))


    if mode not in EHZBRTS_THERMO_MODE:
        Domoticz.Error("Unknow Thermostat Mode %s for %s" %(mode, key))
        return

    if 'Schneider' not in self.ListOfDevices[key]:
        self.ListOfDevices[key]['Schneider'] = {}
    self.ListOfDevices[key]['Schneider']['Target Mode'] = mode
    self.ListOfDevices[key]['Schneider']['TimeStamp Mode'] = int(time())

    manuf_id = "105e"
    manuf_spec = "01"
    cluster_id = "%04x" %0x0201
    Hattribute = "%04x" %0xe010
    data_type = "30" # Uint8
    data = "%02x" %EHZBRTS_THERMO_MODE[ mode ]

    EPout = '01'
    for tmpEp in self.ListOfDevices[key]['Ep']:
        if "0201" in self.ListOfDevices[key]['Ep'][tmpEp]:
            EPout= tmpEp

    loggingOutput( self, 'Log', "Schneider EH-ZB-RTS Thermo Mode  %s with value %s / cluster: %s, attribute: %s type: %s"
            %(key,data,cluster_id,Hattribute,data_type), nwkid=key)
    Modules.output.write_attribute( self, key, ZIGATE_EP, EPout, cluster_id, manuf_id, manuf_spec, Hattribute, data_type, data)
    self.ListOfDevices[key]['Heartbeat'] = 0

def schneiderRenforceent( self, NWKID):
    
    rescheduleAction = False
    if 'Model' in self.ListOfDevices[NWKID]:
        if self.ListOfDevices[NWKID]['Model'] == 'EH-ZB-VACT':
            pass
    if 'Schneider Wiser' in self.ListOfDevices[NWKID]:
        if 'HACT Mode' in self.ListOfDevices[NWKID]['Schneider Wiser']:
            if not self.busy and len(self.ZigateComm.zigateSendingFIFO) <= MAX_LOAD_ZIGATE:
                schneider_thermostat_behaviour( self, NWKID, self.ListOfDevices[NWKID]['Schneider Wiser']['HACT Mode'])
            else:
                rescheduleAction = True
        if 'HACT FIP Mode' in self.ListOfDevices[NWKID]['Schneider Wiser']:
            if not self.busy and len(self.ZigateComm.zigateSendingFIFO) <= MAX_LOAD_ZIGATE:
                schneider_fip_mode( self, NWKID,  self.ListOfDevices[NWKID]['Schneider Wiser']['HACT FIP Mode'])
            else:
                rescheduleAction = True

    return rescheduleAction

def schneiderSendReadAttributesResponse(self, NWKID, EPout, ClusterID, sqn, rawAttr):
    loggingOutput( self, 'Log', "Schneider send attributes: nwkid %s ep: %s , clusterId: %s, sqn: %s,data: %s" \
            %(NWKID, EPout, ClusterID, sqn, rawAttr ), NWKID)

    attr = rawAttr[2:4] + rawAttr[0:2]
    data = ''
    dataType = ''
    payload = ''
    if attr == 'e010':
        dataType = '30'
        data = '01'
    elif attr == '0015': #min setpoint temp
        dataType = '29'
        data = '0032' #0.5 degree
    elif attr == '0016': #max setpoint temp
        dataType = '29'
        data = '0DAC' #35.00 degree
    elif attr == '0012': #occupied setpoint temp
        dataType = '29'

        if EPout not in self.ListOfDevices[NWKID]['Ep']:
            self.ListOfDevices[NWKID]['Ep'][EPout] = {}
        if ClusterID not in self.ListOfDevices[NWKID]['Ep'][EPout]:
            self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID] = {}
        if not isinstance( self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID] , dict):
            self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID] = {}
        if attr not in self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID]:
            self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID][attr] = {}
        if 'Ep' in self.ListOfDevices[NWKID]:
            if EPout in self.ListOfDevices[NWKID]['Ep']:
                if ClusterID in self.ListOfDevices[NWKID]['Ep'][EPout]:
                    if attr in self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID]:
                        if self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID][attr] == {}:
                            loggingOutput( self, 'Log', "Schneider send attributes: could not find value, setting 20",NWKID)
                            self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID][attr] = 2000
                        loggingOutput( self, 'Log', "Schneider send attributes: FOUND value %s"%(self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID][attr]),NWKID)
                        value = self.ListOfDevices[NWKID]['Ep'][EPout][ClusterID][attr]
                        data = '%04X' %value

    cmd = "01"
    status = "00"
    cluster_frame = "18"

    loggingOutput( self, 'Log', "Schneider send attributes: nwkid %s ep: %s , clusterId: %s, sqn: %s, attr: %s, dataType: %s, data: %s" \
            %(NWKID, EPout, ClusterID, sqn, attr, dataType, data ), NWKID)

    if dataType == '29':
        payload = cluster_frame + sqn + cmd + rawAttr + status + dataType + data[2:4] + data[0:2]
    elif dataType == '30':
        payload = cluster_frame + sqn + cmd + rawAttr + status + dataType + data

    loggingOutput( self, 'Log', "Schneider calls raw_APS_request payload %s" \
            %(payload), NWKID)

    Modules.output.raw_APS_request( self, NWKID, EPout, ClusterID, '0104', payload, zigate_ep=ZIGATE_EP)


def schneiderUpdateThermostat (self, Devices, NWKID, srcEp, ClusterID, data):

    # Check if nwkid is the ListOfDevices

    if NWKID not in self.ListOfDevices:
        return
    sTemp = data [4:8]
    temp = struct.unpack('h',struct.pack('>H',int(sTemp,16)))[0]
    domoTemp = round(temp/100,1)

    loggingOutput( self, 'Log', "Schneider updateThermostat data:%s , temp:%s , domoTemp : %s" \
            %(data, temp, domoTemp), NWKID)

    # Look for TargetSetPoint
    from Modules.domoticz import MajDomoDevice
    MajDomoDevice(self, Devices, NWKID,  srcEp, ClusterID, domoTemp, '0012')
    if 'Ep' in self.ListOfDevices[NWKID]:
        if srcEp in self.ListOfDevices[NWKID]['Ep']:
            if ClusterID in self.ListOfDevices[NWKID]['Ep'][srcEp]:
                if '0012' in self.ListOfDevices[NWKID]['Ep'][srcEp][ClusterID]:
                    self.ListOfDevices[NWKID]['Ep'][srcEp][ClusterID]['0012'] = temp


def schneiderReadRawAPS(self, Devices, srcNWKID, srcEp, ClusterID, dstNWKID, dstEP, MsgPayload):


    loggingOutput( self, 'Log', "Schneider read raw APS nwkid: %s ep: %s , clusterId: %s, dstnwkid: %s, dstep: %s, payload: %s" \
            %(srcNWKID, srcEp, ClusterID, dstNWKID, dstEP, MsgPayload), srcNWKID)

    fcf = MsgPayload[0:2] # uint8
    sqn = MsgPayload[2:4] # uint8
    cmd = MsgPayload[4:6] # uint8
    data = MsgPayload[6:] # all the rest

    if cmd == '00': #read attributes
        loggingOutput( self, 'Log','Schneider cmd 0x00',srcNWKID)
        schneiderSendReadAttributesResponse(self, srcNWKID, srcEp, ClusterID, sqn, data)
    elif cmd == 'e0': # setpoint from thermostat
        schneiderUpdateThermostat(self, Devices, srcNWKID, srcEp, ClusterID, data)

    loggingOutput( self, 'Log', "         -- FCF: %s, SQN: %s, CMD: %s, Data: %s" \
            %( fcf, sqn, cmd, data), srcNWKID)

    return

def importSchneiderZoning( self ):
    """
    Import Schneider Zoning Configuration, and populate the corresponding datastructutre

{
	"zone1": {
		"ieee_thermostat": "ieee of my thermostat",
		"actuator": ["IEEE1","IEEE2"]
	},
	"zone2": {
		"ieee_thermostat": "ieee of my thermostat",
		"actuator": ["IEEE1","IEEE2"]
	}
}
    """

    if self.SchneiderZone is not None:
        # Alreday imported. We do it only once
        return

    SCHNEIDER_ZONING = 'schneider_zoning.json'

    self.SchneiderZoningFilename = self.pluginconf.pluginConf['pluginConfig'] + SCHNEIDER_ZONING

    if not os.path.isfile( self.SchneiderZoningFilename ) :
        loggingOutput(self, 'Debug', "importSchneiderZoning - Nothing to import from %s" %self.SchneiderZoningFilename)
        return

    with open( self.SchneiderZoningFilename, 'rt') as handle:
        SchneiderZoning = json.load( handle)

    self.SchneiderZone = {}
    for zone in SchneiderZoning:
        if 'ieee_thermostat' not in SchneiderZoning[zone]:
            # Missing Thermostat
            loggingOutput( self, 'Error', "importSchneiderZoning - Missing Thermostat entry in %s" %SchneiderZoning[zone])
            continue

        if SchneiderZoning[zone]['ieee_thermostat'] not in self.IEEE2NWK:
            # Thermostat IEEE not known!
            loggingOutput(self,  'Error', "importSchneiderZoning - Thermostat IEEE %s do not exist" %SchneiderZoning[zone]['ieee_thermostat'])
            continue
        
        self.SchneiderZone[ zone ] = {}
        self.SchneiderZone[ zone ]['Thermostat'] = {}

        self.SchneiderZone[ zone ]['Thermostat']['IEEE'] = SchneiderZoning[zone]['ieee_thermostat']
        self.SchneiderZone[ zone ]['Thermostat']['NWKID'] = self.IEEE2NWK[ SchneiderZoning[zone]['ieee_thermostat'] ]
        self.SchneiderZone[ zone ]['Thermostat']['HACT'] = {}
        
        if 'actuator' not in SchneiderZoning[zone]:
            # We just have a simple Thermostat
            loggingOutput(self,  'Debug', "importSchneiderZoning - No actuators for this Zone: %s" %zone)
            continue

        for hact in SchneiderZoning[zone]['actuator']:
            _nwkid = self.IEEE2NWK[ hact ]
            if hact not in self.IEEE2NWK:
                # Unknown in IEEE2NWK
                loggingOutput(self,  'Error', "importSchneiderZoning - Unknown HACT: %s" %hact)
                continue

            if self.IEEE2NWK[ hact ] not in self.ListOfDevices:
                # Unknown in ListOfDevices
                loggingOutput(self,  'Error', "importSchneiderZoning - Unknown HACT: %s" %_nwkid)
                continue
            
            self.SchneiderZone[ zone ]['Thermostat']['HACT'][ _nwkid ] = {}
            self.SchneiderZone[ zone ]['Thermostat']['HACT'][ _nwkid ]['IEEE'] = hact

    # At that stage we have imported all informations
    loggingOutput(self, 'Log', "importSchneiderZoning - Zone Information: %s " %self.SchneiderZone )

    return

