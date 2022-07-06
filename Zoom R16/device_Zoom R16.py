# name=Zoom R16

import arrangement
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
        # Auto Punch I/O
        if event.controlNum == 54:
            pass
        # A-B Repeat
        elif event.controlNum == 55:
            pass
        # Go to previous marker
        elif event.controlNum == 56:
            pass
        # Go to next marker
        elif event.controlNum == 57:
            pass
        # Mark/Clear
        elif event.controlNum == 58:
            pass
        # Rewind
        elif event.controlNum == 91:
            # Start rewinding
            transport.rewind(2)
        # Fast-forward
        elif event.controlNum == 92:
            # Start fast-forwarding
            transport.fastForward(2)
        # Stop
        elif event.controlNum == 93:
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
        # Rewind
        if event.controlNum == 91:
            # Stop rewinding
            transport.rewind(0)
        # Fast-forward
        elif event.controlNum == 92:
            # Stop fast-forwarding
            transport.fastForward(0)


def OnPitchBend(event):
    """
    Handles all faders.
    """
    event.handled = True
