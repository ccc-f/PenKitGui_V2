set ws=WScript.CreateObject("WScript.Shell")
currentpath = createobject("Scripting.FileSystemObject").GetFolder(".").Path
PenKitGui = currentpath & "\penkitgui.bat"
ws.Run PenKitGui,0