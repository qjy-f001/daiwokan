import json
# from poco.drivers.unity3d import UnityPoco as poco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

auto_setup(__file__)

# poco = poco()
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
ui = poco.agent.hierarchy.dump()
print(json.dumps(ui, indent=4))

poco("android:id/content").offspring("com.miui.home:id/workspace").offspring("带我看")[0].offspring(
    "com.miui.home:id/icon_icon").click()
