# name=Zoom R16

import arrangement
import channels
import mixer
import transport
import ui


def _previous(index: int, divisor: int, minimum: int) -> int:
    return max((
        index // divisor
        if index % divisor
        else index // divisor - 1
    ) * divisor, minimum)


def _next(index: int, divisor: int, maximum: int) -> int:
    return min((
        index // divisor + 1
    ) * divisor, maximum)


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
        # Status keys
        if 8 <= event.controlNum <= 15:
            # If the mixer is focused
            if ui.getFocused(0):
                # Toggle the mute status of the current mixer track
                mixer.muteTrack(
                    mixer.trackNumber() +
                    event.controlNum - 8
                )
            # If the channel rack is focused
            elif ui.getFocused(1):
                # Toggle the mute status of the current channel
                channels.muteChannel(
                    channels.selectedChannel() +
                    event.controlNum - 8
                )
        # Previous Bank, 1-8Tr
        elif event.controlNum == 46:
            # If the channel rack is focused
            if ui.getFocused(1):
                # Move to the previous block of 8 channels
                channels.selectOneChannel(
                    _previous(channels.selectedChannel(), 8, 0)
                )
        # Next Bank, 9-16Tr
        elif event.controlNum == 47:
            # If the channel rack is focused
            if ui.getFocused(1):
                # Move to the next block of 8 channels
                channels.selectOneChannel(
                    _next(channels.selectedChannel(),
                          8, channels.channelCount()-1)
                )
        # Auto Punch I/O
        elif event.controlNum == 54:
            pass
        # A-B Repeat
        elif event.controlNum == 55:
            pass
        # Go to previous marker
        elif event.controlNum == 56:
            arrangement.jumpToMarker(-1, 0)
        # Go to next marker
        elif event.controlNum == 57:
            arrangement.jumpToMarker(+1, 0)
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
