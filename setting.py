import os 
import platform

startCmd = 'start cmd /k'
base_dir = os.getcwd()
# 主题样例 https://ttkbootstrap.readthedocs.io/en/latest/zh/themes/dark/
# 深色主题 solar superhero
# 浅色主题 sandstone united morph cosmo flatly journal litera lumen pulse yeti cerculean
themes = 'superhero'
# 每行工具按钮数量
line_count = 4
# UI 宽度
width = 1400
# UI 高度
height = 700
# 按钮宽度
button_width = 30
#路径设置
tools_path = os.getcwd()
if platform.system() == 'Windows' :
    java8_path = (tools_path + "\Java_path\jre_1.8_win\\bin\java").replace('\\','\\\\')
    java9_path = (tools_path + "\Java_path\java9_win\\bin\java").replace('\\','\\\\')
    java17_path = (tools_path + "\Java_path\java17\\bin\java").replace('\\','\\\\')
else:
    #MacOS和Linux的java绝对路径
    java8_path = tools_path + "/Java_path/java_1.8/bin/java"
    java9_path = tools_path + "/Java_path/java9/bin/java"
    java17_path = tools_path + "/Java_path/java17/bin/java"