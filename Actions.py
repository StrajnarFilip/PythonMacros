from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from typing import Callable, Any
import time

from pynput import keyboard as KeyboardBase
from pynput import mouse as MouseBase

mouseController= MouseController()
keyboardController = KeyboardController()

class CursorPosition:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y

def BlankKeyboard(a: Any):
    pass

def BlankMouse(x:int,y:int):
    pass

def LeftClick():
    mouseController.press(Button.left)
    mouseController.release(Button.left)
    
def RightClick():
    mouseController.press(Button.right)
    mouseController.release(Button.right)
    
def MouseMove(x: int, y: int):
    mouseController.position=(x,y)
    
def MouseMoveRelative(x: int, y: int):
    mouseController.move(x,y)
    
def GetCursorPosition() -> CursorPosition:
    positionTuple: tuple[int,int]=mouseController.position
    return CursorPosition(positionTuple[0],positionTuple[1])

# Preses key down, and releases it
def KeyClick(key: Any):
    keyboardController.press(key)
    keyboardController.release(key)
    
def KeyDown(key: Any):
    keyboardController.press(key)
    
def KeyUp(key: Any):
    keyboardController.release(key)
    
def KeyboardType(string_to_type: str):
    keyboardController.type(string_to_type)

def NewKeyboardListener(on_press_function: Callable[[Any],None],on_release_function: Callable[[Any],None] = BlankKeyboard):
    keyboardListener=KeyboardBase.Listener(on_press=on_press_function, on_release=on_release_function)
    keyboardListener.start()

def NewKeybind(hotkey_string: str, function_to_call: Callable[[],None]):
    hotkeys=KeyboardBase.GlobalHotKeys({
        hotkey_string:function_to_call
    })
    hotkeys.start()
    
def NewMouseListener(on_click_function: Callable[[int,int,Any,bool],None],
                     on_move_function: Callable[[int,int],None] = BlankMouse):
    mouseListener=MouseBase.Listener(on_move=on_move_function,on_click=on_click_function)
    mouseListener.start()

def LogCoordinatesOnClick():  
    def LogOnClick(x:int,y:int,button:Any,isPressed:bool):
        if isPressed:
            print(f"Button {button} clicked at X: {y} Y: {y}")
    NewMouseListener(LogOnClick)

def BlockThread():
    while True:
        time.sleep(2000000)