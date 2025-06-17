import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# XML 数据
xml_data = '''<positions>
    <position x="3796.3" y="5847.6" z="367.1" />
    <position x="3795.5" y="5852.5" z="367.1" />
    <position x="3794.6" y="5857.4" z="367.1" />
    <position x="3793.8" y="5862.4" z="367.1" />
    <position x="3792.9" y="5867.3" z="367.1" />
    <position x="3792.1" y="5872.2" z="367.1" />
    <position x="3791.2" y="5877.2" z="367.1" />
    <position x="3790.4" y="5882.1" z="367.1" />
    <position x="3793.0" y="5887.6" z="367.1" />
    <position x="3792.2" y="5892.5" z="367.1" />
    <position x="3791.3" y="5897.5" z="367.1" />
    <position x="3790.5" y="5902.4" z="367.2" />
    <position x="3789.6" y="5907.3" z="367.2" />
    <position x="3788.8" y="5912.2" z="367.2" />
    <position x="3787.9" y="5917.2" z="367.2" />
    <position x="3787.1" y="5922.1" z="367.2" />
    <position x="3786.2" y="5927.0" z="367.2" />
    <position x="3788.8" y="5932.5" z="367.2" />
    <position x="3788.0" y="5937.5" z="367.2" />
    <position x="3787.2" y="5942.4" z="367.2" />
    <position x="3786.3" y="5947.3" z="367.2" />
    <position x="3785.5" y="5952.3" z="367.2" />
    <position x="3784.6" y="5957.2" z="367.2" />
    <position x="3783.8" y="5962.1" z="367.2" />
</positions>'''

# 解析 XML 数据
root = ET.fromstring(xml_data)

# 提取所有的 x 和 y 坐标
x_values = []
y_values = []
for position in root.findall('position'):
    x = float(position.get('x'))
    y = float(position.get('y'))
    x_values.append(x)
    y_values.append(y)

# 绘制路径
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

# 标出起始点和终止点
plt.scatter(x_values[0], y_values[0], color='g', label='Start', zorder=5)  # 起始点
plt.scatter(x_values[-1], y_values[-1], color='r', label='End', zorder=5)  # 终止点
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('XY Coordinates Visualization')
plt.legend()
plt.savefig("/opt/data/private/jurunkun-flash/pangyp/OmniDrive/leaderboard/data_visual/route_for_test_3")