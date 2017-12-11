import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

from ipywidgets import Button, HBox, VBox
from IPython.display import display

def on_button_clicked(b):
    v = Twist()
    if b.description=='forward':
        v.linear.x = 2.0
    elif b.description=='backward':
        v.linear.x = -2.0
    elif b.description=='left':
        v.angular.z = 2.0
    elif b.description=='right':
        v.angular.z = -2.0
    pub.publish(v)

words = ['forward', 'backward', 'left', 'right']
items = [Button(description=w) for w in words]
for button in items:
    button.on_click(on_button_clicked)

left_box = VBox([items[0], items[1]])
right_box = VBox([items[2], items[3]])
display(HBox([left_box, right_box]))