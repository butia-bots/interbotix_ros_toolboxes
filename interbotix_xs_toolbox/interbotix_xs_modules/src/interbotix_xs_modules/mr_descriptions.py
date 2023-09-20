# Modern Robotics Descriptions for all various Interbotix Arms.
# Note that the end-effector is positioned at '<robot_name>/ee_gripper_link'
# and that the Space frame is positioned at '<robot_name>/base_link'.

import numpy as np

class px100:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.0931, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.1931, 0.0, 0.035],
                      [0.0, 1.0, 0.0, -0.1931, 0.0, 0.135]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.248575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.1931],
                  [0.0, 0.0, 0.0, 1.0]])

class px150:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.10457, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.25457, 0.0, 0.05],
                      [0.0, 1.0, 0.0, -0.25457, 0.0, 0.2],
                      [1.0, 0.0, 0.0, 0.0, 0.25457, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.358575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.25457],
                  [0.0, 0.0, 0.0, 1.0]])

class rx150:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.10457, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.25457, 0.0, 0.05],
                      [0.0, 1.0, 0.0, -0.25457, 0.0, 0.2],
                      [1.0, 0.0, 0.0, 0.0, 0.25457, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.358575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.25457],
                  [0.0, 0.0, 0.0, 1.0]])

class rx200:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.10457, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.30457, 0.0, 0.05],
                      [0.0, 1.0, 0.0, -0.30457, 0.0, 0.25],
                      [1.0, 0.0, 0.0, 0.0, 0.30457, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.408575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.30457],
                  [0.0, 0.0, 0.0, 1.0]])

class vx250:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.12705, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.37705, 0.0, 0.06],
                      [0.0, 1.0, 0.0, -0.37705, 0.0, 0.31],
                      [1.0, 0.0, 0.0, 0.0, 0.37705, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.468575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.37705],
                  [0.0, 0.0, 0.0, 1.0]])

class vx300:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.12705, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.42705, 0.0, 0.05955],
                      [0.0, 1.0, 0.0, -0.42705, 0.0, 0.35955],
                      [1.0, 0.0, 0.0, 0.0, 0.42705, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.536494],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.42705],
                  [0.0, 0.0, 0.0, 1.0]])

class doris_arm:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.12705, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.42705, 0.0, 0.05955],
                      [0.0, 1.0, 0.0, -0.42705, 0.0, 0.35955],
                      [1.0, 0.0, 0.0, 0.0, 0.42705, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.536494],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.42705],
                  [0.0, 0.0, 0.0, 1.0]])

class vx300s:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.12705, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.42705, 0.0, 0.05955],
                      [1.0, 0.0, 0.0, 0.0, 0.42705, 0.0],
                      [0.0, 1.0, 0.0, -0.42705, 0.0, 0.35955],
                      [1.0, 0.0, 0.0, 0.0, 0.42705, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.536494],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.42705],
                  [0.0, 0.0, 0.0, 1.0]])

class wx200:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.11065, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.31065, 0.0, 0.05],
                      [0.0, 1.0, 0.0, -0.31065, 0.0, 0.25],
                      [1.0, 0.0, 0.0, 0.0, 0.31065, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.408575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.31065],
                  [0.0, 0.0, 0.0, 1.0]])

class wx250:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.11065, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.36065, 0.0, 0.04975],
                      [0.0, 1.0, 0.0, -0.36065, 0.0, 0.29975],
                      [1.0, 0.0, 0.0, 0.0, 0.36065, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.458325],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.36065],
                  [0.0, 0.0, 0.0, 1.0]])

class wx250s:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.11065, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.36065, 0.0, 0.04975],
                      [1.0, 0.0, 0.0, 0.0, 0.36065, 0.0],
                      [0.0, 1.0, 0.0, -0.36065, 0.0, 0.29975],
                      [1.0, 0.0, 0.0, 0.0, 0.36065, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.458325],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.36065],
                  [0.0, 0.0, 0.0, 1.0]])

class mobile_px100:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.08518, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.18518, 0.0, 0.035],
                      [0.0, 1.0, 0.0, -0.18518, 0.0, 0.135]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.248575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.18518],
                  [0.0, 0.0, 0.0, 1.0]])


class mobile_wx200:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.104825, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.304825, 0.0, 0.05],
                      [0.0, 1.0, 0.0, -0.304825, 0.0, 0.25],
                      [1.0, 0.0, 0.0, 0.0, 0.304825, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.408575],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.304825],
                  [0.0, 0.0, 0.0, 1.0]])

class mobile_wx250s:
    Slist = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.104825, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -0.354825, 0.0, 0.04975],
                      [1.0, 0.0, 0.0, 0.0, 0.354825, 0.0],
                      [0.0, 1.0, 0.0, -0.354825, 0.0, 0.29975],
                      [1.0, 0.0, 0.0, 0.0, 0.354825, 0.0]]).T

    M = np.array([[1.0, 0.0, 0.0, 0.458325],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.354825],
                  [0.0, 0.0, 0.0, 1.0]])
