import math, time

global prev, pressed, mode, offset, message_time

def sign(x): return 1 if x >= 0 else -1

# conjugate quaternion
def conj(q):
  return [-q[0], -q[1], -q[2], q[3]]

# multiplication of quaternion
def multiply(a, b):
  x0, y0, z0, w0 = a
  x1, y1, z1, w1 = b
  return [x1 * w0 - y1 * z0 + z1 * y0 + w1 * x0,
      x1 * z0 + y1 * w0 - z1 * x0 + w1 * y0,
      -x1 * y0 + y1 * x0 + z1 * w0 + w1 * z0,
      -x1 * x0 - y1 * y0 - z1 * z0 + w1 * w0]

# convert quaternion to euler
def quaternion2euler(q):
  yaw_pitch_roll = [0.0, 0.0, 0.0]
  # roll (x-axis rotation)
  sinr = +2.0 * (q[3] * q[0] + q[1] * q[2])
  cosr = +1.0 - 2.0 * (q[0] * q[0] + q[1] * q[1])
  yaw_pitch_roll[2] = math.atan2(sinr, cosr)

  # pitch (y-axis rotation)
  sinp = +2.0 * (q[3] * q[1] - q[2] * q[0])
  if (abs(sinp) >= 1):
    yaw_pitch_roll[1] = math.copysign(M_PI / 2, sinp)
  else:
    yaw_pitch_roll[1] = math.asin(sinp)

  # yaw (z-axis rotation)
  siny = +2.0 * (q[3] * q[2] + q[0] * q[1]);
  cosy = +1.0 - 2.0 * (q[1] * q[1] + q[2] * q[2]);
  yaw_pitch_roll[0] = math.atan2(siny, cosy);

  return yaw_pitch_roll

# convert euler to quaternion
def euler2quaternion(yaw_pitch_roll):
  cy = math.cos(yaw_pitch_roll[0] * 0.5);
  sy = math.sin(yaw_pitch_roll[0] * 0.5);
  cr = math.cos(yaw_pitch_roll[2] * 0.5);
  sr = math.sin(yaw_pitch_roll[2] * 0.5);
  cp = math.cos(yaw_pitch_roll[1] * 0.5);
  sp = math.sin(yaw_pitch_roll[1] * 0.5);

  return [cy * sr * cp - sy * cr * sp,
  cy * cr * sp + sy * sr * cp,
  sy * cr * cp - cy * sr * sp,
  cy * cr * cp + sy * sr * sp]

def quaternion_rotate_vec(q, vec):
  return multiply(multiply(q, vec), conj(q))

# rotate specified vector using yaw_pitch_roll
def rotatevec(yaw_pitch_roll, vec):
  q = euler2quaternion(yaw_pitch_roll)
  return quaternion_rotate_vec(q, vec)

if starting:
  prev = [[False] * 30, [False] * 30]
  pressed = [[False] * 30, [False] * 30]
  mode = [0, 0]
  offset = [0.0, 0.0, 0.0]
  message_time = 0.0
  alvr.two_controllers = True

# change target controller
if keyboard.getPressed(Key.Z):
  controller = 1 - controller

map = [["system", Key.G], ["application_menu", Key.X], ["trigger", Key.T], ["a", Key.V], ["b", Key.B], ["x", Key.N], ["y", Key.M]
, ["grip", Key.F1], ["trackpad_click", Key.F2], ["back", Key.F3], ["guide", Key.F4], ["start", Key.F5]
, ["dpad_left", Key.F6], ["dpad_up", Key.F7], ["dpad_right", Key.F8], ["dpad_down", Key.F9], ["trackpad_touch", Key.F10]]

for k in map:
  alvr.buttons[0][alvr.Id(k[0])] = keyboard.getKeyDown(k[1])
  alvr.buttons[1][alvr.Id(k[0])] = keyboard.getKeyDown(k[1])

if time.time() - message_time > 2:
  # remove message after 2 seconds
  alvr.message = ""

for c in range(0, 2):
  for i in range(0, vrcontroller[c].BUTTONS):
    if prev[c][i] != vrcontroller[c].button[i]:
      prev[c][i] = vrcontroller[c].button[i]
      pressed[c][i] = prev[c][i]
    else:
      pressed[c][i] = False

  if pressed[c][vrcontroller[0].APP]:
    mode[c] = (mode[c] + 1) % 3
    # show messageo on display
    alvr.message = "mode left " + str(mode[0]) + "\nmode right " + str(mode[1])
    message_time = time.time()

  if mode[c] == 0:
    # trackpad guesture mode
    alvr.buttons[c][alvr.Id("trigger")] = alvr.buttons[c][alvr.Id("trigger")] or vrcontroller[c].trigger
    #alvr.buttons[c][alvr.Id("application_menu")] = alvr.buttons[c][alvr.Id("application_menu")] or alvr.input_buttons[alvr.InputId("back")]
  
    if vrcontroller[c].click:
      if vrcontroller[c].trackpad[0] + vrcontroller[c].trackpad[1] > 0.0:
        if vrcontroller[c].trackpad[0] - vrcontroller[c].trackpad[1] > 0.0:
          # right
          alvr.buttons[c][alvr.Id("system")] = True
        else:
          # top
          alvr.buttons[c][alvr.Id("trackpad_click")] = True
          alvr.buttons[c][alvr.Id("trackpad_touch")] = True
      else:
        if vrcontroller[c].trackpad[0] - vrcontroller[c].trackpad[1] > 0.0:
          # bottom
          alvr.buttons[c][alvr.Id("grip")] = True
        else:
          # left
          alvr.buttons[c][alvr.Id("application_menu")] = True
  elif mode[c] == 1:
    # fly mode (buggy)
    # press upper half of trackpad to forward. bottom half to back
    if vrcontroller[c].click:
      outvec = quaternion_rotate_vec(vrcontroller[c].quaternion, [0, 0, -1, 0])
      speed = 0.002 * sign(vrcontroller[c].trackpad[1])
      offset[0] += speed * outvec[0]
      offset[1] += speed * outvec[1]
      offset[2] += speed * outvec[2]
    if vrcontroller[c].trigger and vrcontroller[c].click:
      offset = [0.0, 0.0, 0.0]
  
    alvr.buttons[c][alvr.Id("trigger")] = alvr.buttons[c][alvr.Id("trigger")] or vrcontroller[c].trigger
  elif mode[c] == 2:
    # passthrough mode
    alvr.buttons[c][alvr.Id("trackpad_click")] = alvr.buttons[c][alvr.Id("trackpad_click")] or vrcontroller[c].click
    alvr.buttons[c][alvr.Id("trackpad_touch")] = alvr.buttons[c][alvr.Id("trackpad_touch")] or vrcontroller[c].touch
    alvr.buttons[c][alvr.Id("trigger")] = alvr.buttons[c][alvr.Id("trigger")] or vrcontroller[c].trigger
    alvr.trackpad[c][0] = vrcontroller[c].trackpad[0]
    alvr.trackpad[c][1] = vrcontroller[c].trackpad[1]
    alvr.buttons[c][alvr.Id("system")] = vrcontroller[c].volup
    alvr.buttons[c][alvr.Id("grip")] = vrcontroller[c].voldown
  
  # You need to set trigger value correctly to get trigger click work
  alvr.trigger[c] = 1.0 if alvr.buttons[c][alvr.Id("trigger")] else 0.0
  
  alvr.override_head_position = True
  
  alvr.head_position[0] = alvr.input_head_position[0] + offset[0]
  alvr.head_position[1] = alvr.input_head_position[1] + offset[1]
  alvr.head_position[2] = alvr.input_head_position[2] + offset[2]
  
  alvr.override_controller_position = True
  
  alvr.controller_position[c][0] = vrcontroller[c].position[0] + offset[0]
  alvr.controller_position[c][1] = vrcontroller[c].position[1] + offset[1]
  alvr.controller_position[c][2] = vrcontroller[c].position[2] + offset[2]
  #alvr.controller_position[1-controller][0] = alvr.input_controller_position[0] + offset[0] + 0.1
  #alvr.controller_position[1-controller][1] = alvr.input_controller_position[1] + offset[1] + 0.1
  #alvr.controller_position[1-controller][2] = alvr.input_controller_position[2] + offset[2] + 0.1
  #alvr.controller_orientation[1-controller][0] = android[0].yaw
  #alvr.controller_orientation[1-controller][1] = android[0].pitch
  #alvr.controller_orientation[1-controller][2] = android[0].roll
  
  alvr.override_controller_orientation = True
  yaw_pitch_roll = quaternion2euler(vrcontroller[c].quaternion)
  alvr.controller_orientation[c][0] = yaw_pitch_roll[0]
  alvr.controller_orientation[c][1] = yaw_pitch_roll[1]
  alvr.controller_orientation[c][2] = yaw_pitch_roll[2]

if True:
  # watch variables on FreePIE debugger
  diagnostics.watch(alvr.input_head_orientation[0])
  diagnostics.watch(alvr.input_head_orientation[1])
  diagnostics.watch(alvr.input_head_orientation[2])
  
  diagnostics.watch(alvr.input_controller_orientation[0])
  diagnostics.watch(alvr.input_controller_orientation[1])
  diagnostics.watch(alvr.input_controller_orientation[2])
  
  diagnostics.watch(alvr.input_head_position[0])
  diagnostics.watch(alvr.input_head_position[1])
  diagnostics.watch(alvr.input_head_position[2])
  
  diagnostics.watch(alvr.input_controller_position[0])
  diagnostics.watch(alvr.input_controller_position[1])
  diagnostics.watch(alvr.input_controller_position[2])
  
  diagnostics.watch(alvr.input_trackpad[0])
  diagnostics.watch(alvr.input_trackpad[1])
  
  diagnostics.watch(alvr.input_buttons[0])
  diagnostics.watch(alvr.input_buttons[1])
  diagnostics.watch(alvr.input_buttons[2])
  diagnostics.watch(alvr.input_buttons[3])
  diagnostics.watch(alvr.input_buttons[4])
  diagnostics.watch(alvr.input_buttons[5])

  diagnostics.watch(alvr.head_position[0])
  diagnostics.watch(alvr.head_position[1])
  diagnostics.watch(alvr.head_position[2])

  diagnostics.watch(alvr.buttons[c][alvr.Id("trigger")])
  diagnostics.watch(vrcontroller[1].magnetometer[0])
  diagnostics.watch(vrcontroller[1].magnetometer[1])
  diagnostics.watch(vrcontroller[1].magnetometer[2])
