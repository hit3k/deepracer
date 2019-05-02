def reward_function(params):

    '''
    180 mins training
    Hyperparameter  Value
    Gradient descent batch size	64
    Entropy	0.05
    Discount factor	0.995
    Loss type	Huber
    Learning rate	0.0003
    Number of experience episodes between each policy-updating iteration	20
    Number of epochs	10

    Speed up to 1m/s best result	00:01:20.254	100%
    '''

    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_15 = 0.15 * track_width
    marker_2 = 0.2 * track_width
    marker_25 = 0.25 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width
    marker_5 = 0.5 * track_width
    marker_6 = 0.6 * track_width
    marker_75 = 0.75 * track_width
    marker_85 = 0.85 * track_width


    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1 and speed > 1:
        reward = 1
    elif distance_from_center <= marker_15:
        reward = 0.9
    elif distance_from_center <= marker_2:
        reward = 0.8
    elif distance_from_center <= marker_25:
        reward = 0.6
    elif distance_from_center <= marker_3:
        reward = 0.4
    elif distance_from_center <= marker_4:
        reward = 0.2
    elif distance_from_center <= marker_5:
        reward = 0.1
    elif distance_from_center <= marker_6:
        reward = 0.07
    elif distance_from_center <= marker_75:
        reward = 0.05
    elif distance_from_center <= marker_85:
        reward = 0.02
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return float(reward)
