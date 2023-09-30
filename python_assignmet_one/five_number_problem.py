# import pyautogui
# rows = int(input(""))
# for i in range(1,rows+1):
#     for j in range(i):
#         pyautogui.write('*', interval=0.10)
# pyautogui.press('enter')
    



import pyautogui

rows = int(input(""))

for i in range(1, rows + 1):
    for j in range(i):
        pyautogui.write('#', interval=0.50)
    pyautogui.press('enter')






