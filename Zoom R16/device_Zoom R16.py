# name=Zoom R16


def OnControlChange(event):
    """
    Handles the dial.
    """
    event.handled = True


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
