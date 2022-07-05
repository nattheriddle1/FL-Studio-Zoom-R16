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


def OnPitchBend(event):
    """
    Handles all faders.
    """
    event.handled = True
