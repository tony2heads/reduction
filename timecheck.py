#!/usr/bin/env python

import sys
import h5py
#filename="/var/kat/archive/data/RTS/telescope_products/2015/07/27/1437985794.h5"
#filename="/var/kat/archive/data/RTS/telescope_products/2015/07/03/1435921279.h5"
filename=sys.argv[1]

print "      "+str(filename)

raw_h5 = h5py.File(filename, 'r')
corr_timestamps = raw_h5['Data/timestamps'].value
print "====================M063============="
"""
 for m063
"""
activity = raw_h5['TelescopeModel/m063/activity'].value
azim = raw_h5['TelescopeModel/m063/pos_actual_scan_azim'].value
elev = raw_h5['TelescopeModel/m063/pos_actual_scan_elev'].value
print 'offset between data and activity timestamps is ', corr_timestamps[0]-activity['timestamp'][0]
print 'offset between data and elev timestamps is ', corr_timestamps[0]-elev['timestamp'][0]
print 'offset between data and azim timestamps is ', corr_timestamps[0]-azim['timestamp'][0]


print "====================M062============="

"""
 for m062
"""
activity = raw_h5['TelescopeModel/m062/activity'].value

azim = raw_h5['TelescopeModel/m062/pos_actual_scan_azim'].value
elev = raw_h5['TelescopeModel/m062/pos_actual_scan_elev'].value
print 'offset between data and activity timestamps is ', corr_timestamps[0]-activity['timestamp'][0]
print 'offset between data and elev timestamps is ', corr_timestamps[0]-elev['timestamp'][0]
print 'offset between data and azim timestamps is ', corr_timestamps[0]-azim['timestamp'][0]
