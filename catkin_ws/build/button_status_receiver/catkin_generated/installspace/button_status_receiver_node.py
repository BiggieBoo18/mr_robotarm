import rospy
from std_msgs.msg import Int8

def callback(data):
    with open("./button_status.txt", "w+") as fp:
        fp.write(str(data.data))

def receiver():
    rospy.init_node('button_status_receiver_node', anonymous=True)

    rospy.Subscriber("button_status", Int8, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    receiver()
