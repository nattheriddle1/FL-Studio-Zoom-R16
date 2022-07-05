# name=Zoom R16

import transport
import ui


def OnControlChange(event):
    """
    Handles the dial.
    """
    event.handled = True
    # If the dial was turned counterclockwise
    if event.controlVal == 1:
        pass
    # If the dial was turned clockwise
    elif event.controlVal == 65:
        pass


def OnNoteOn(event):
    """
    Handles all keys.
    """
    event.handled = True
    # If the key was pressed
    if event.controlVal == 127:
        # Stop
        if event.controlNum == 93:
            transport.stop()
        # Play
        elif event.controlNum == 94:
            transport.start()
        # Record
        elif event.controlNum == 95:
            transport.record()
        # Up Arrow
        elif event.controlNum == 96:
            ui.up()
        # Down Arrow
        elif event.controlNum == 97:
            ui.down()
        # Left Arrow
        elif event.controlNum == 98:
            ui.left()
        # Right Arrow
        elif event.controlNum == 99:
            ui.right()
    # If the key was released
    elif event.controlVal == 0:
        pass


def OnPitchBend(event):
    """
    Handles all faders.
    """
    event.handled = True
