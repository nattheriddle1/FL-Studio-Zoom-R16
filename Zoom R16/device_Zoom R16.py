# name=Zoom R16


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
        pass
    # If the key was released
    elif event.controlVal == 0:
        pass


def OnPitchBend(event):
    """
    Handles all faders.
    """
    event.handled = True
