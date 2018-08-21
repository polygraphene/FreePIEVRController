# only Daydream
diagnostics.watch(vrcontroller[0].orientation[0])
diagnostics.watch(vrcontroller[0].orientation[1])
diagnostics.watch(vrcontroller[0].orientation[2])

diagnostics.watch(vrcontroller[0].quaternion[0])
diagnostics.watch(vrcontroller[0].quaternion[1])
diagnostics.watch(vrcontroller[0].quaternion[2])
diagnostics.watch(vrcontroller[0].quaternion[3])

diagnostics.watch(vrcontroller[0].position[0])
diagnostics.watch(vrcontroller[0].position[1])
diagnostics.watch(vrcontroller[0].position[2])

diagnostics.watch(vrcontroller[0].touch)
diagnostics.watch(vrcontroller[0].click)
diagnostics.watch(vrcontroller[0].home)
diagnostics.watch(vrcontroller[0].app)
diagnostics.watch(vrcontroller[0].volup)
diagnostics.watch(vrcontroller[0].voldown)
# only GearVR
diagnostics.watch(vrcontroller[0].trigger)
diagnostics.watch(vrcontroller[0].button[0])

# Constants for button index
diagnostics.watch(vrcontroller[0].CLICK)
diagnostics.watch(vrcontroller[0].HOME)
diagnostics.watch(vrcontroller[0].APP)
diagnostics.watch(vrcontroller[0].TRIGGER)

diagnostics.watch(vrcontroller[0].acceleration[0])
diagnostics.watch(vrcontroller[0].acceleration[1])
diagnostics.watch(vrcontroller[0].acceleration[2])

diagnostics.watch(vrcontroller[0].gyroscope[0])
diagnostics.watch(vrcontroller[0].gyroscope[1])
diagnostics.watch(vrcontroller[0].gyroscope[2])

# only GearVR
diagnostics.watch(vrcontroller[0].magnetometer[0])
diagnostics.watch(vrcontroller[0].magnetometer[1])
diagnostics.watch(vrcontroller[0].magnetometer[2])

diagnostics.watch(vrcontroller[0].trackpad[0])
diagnostics.watch(vrcontroller[0].trackpad[1])

diagnostics.watch(vrcontroller[0].version)
diagnostics.watch(vrcontroller[0].type)
diagnostics.watch(vrcontroller[0].bdaddr)
diagnostics.watch(vrcontroller[0].deviceId)
diagnostics.watch(vrcontroller[0].temperature)

if vrcontroller[1]:
  # only Daydream
  diagnostics.watch(vrcontroller[1].orientation[0])
  diagnostics.watch(vrcontroller[1].orientation[1])
  diagnostics.watch(vrcontroller[1].orientation[2])
  
  diagnostics.watch(vrcontroller[1].quaternion[0])
  diagnostics.watch(vrcontroller[1].quaternion[1])
  diagnostics.watch(vrcontroller[1].quaternion[2])
  diagnostics.watch(vrcontroller[1].quaternion[3])
  
  diagnostics.watch(vrcontroller[1].position[0])
  diagnostics.watch(vrcontroller[1].position[1])
  diagnostics.watch(vrcontroller[1].position[2])
  
  diagnostics.watch(vrcontroller[1].touch)
  diagnostics.watch(vrcontroller[1].click)
  diagnostics.watch(vrcontroller[1].home)
  diagnostics.watch(vrcontroller[1].app)
  diagnostics.watch(vrcontroller[1].volup)
  diagnostics.watch(vrcontroller[1].voldown)
  # only GearVR
  diagnostics.watch(vrcontroller[1].trigger)
  diagnostics.watch(vrcontroller[1].button[0])
  
  diagnostics.watch(vrcontroller[1].acceleration[0])
  diagnostics.watch(vrcontroller[1].acceleration[1])
  diagnostics.watch(vrcontroller[1].acceleration[2])
  
  diagnostics.watch(vrcontroller[1].gyroscope[0])
  diagnostics.watch(vrcontroller[1].gyroscope[1])
  diagnostics.watch(vrcontroller[1].gyroscope[2])
  
  # only GearVR
  diagnostics.watch(vrcontroller[1].magnetometer[0])
  diagnostics.watch(vrcontroller[1].magnetometer[1])
  diagnostics.watch(vrcontroller[1].magnetometer[2])
  
  diagnostics.watch(vrcontroller[1].trackpad[0])
  diagnostics.watch(vrcontroller[1].trackpad[1])
  
  diagnostics.watch(vrcontroller[1].version)
  diagnostics.watch(vrcontroller[1].type)
  diagnostics.watch(vrcontroller[1].bdaddr)
  diagnostics.watch(vrcontroller[1].deviceId)
  diagnostics.watch(vrcontroller[1].temperature)
