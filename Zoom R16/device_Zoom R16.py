# name=Zoom R16

import arrangement
import channels
import mixer
import plugins
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
            # If a plugin is focused
            elif ui.getFocused(5):
                id_ = ui.getFocusedFormID()
                name = ui.getFocusedPluginName()
                # If a generator plugin is focused
                if ui.getFocused(7):
                    if name == "Sakura":
                        # Toggle the resonators
                        plugins.setParamValue(
                            float(not bool(plugins.getParamValue(
                                event.controlNum + 47, id_))),
                            event.controlNum + 47, id_
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
    # If the mixer is focused
    if ui.getFocused(0):
        # Control the mixer faders
        mixer.setTrackVolume(
            0 if event.midiChan == 8 else
            mixer.trackNumber() + event.midiChan,
            (event.controlVal / 127), 1
        )
    # If the channel rack is focused
    elif ui.getFocused(1):
        # Control the channel volume knobs
        channels.setChannelVolume(
            channels.selectedChannel() +
            event.midiChan,
            event.controlVal / 100, 1
        )
    # If a plugin is focused
    elif ui.getFocused(5):
        id_ = ui.getFocusedFormID()
        name = ui.getFocusedPluginName()
        # If a generator plugin is focused
        if ui.getFocused(7):
            if name == "FLEX":
                # Only 8 sliders, so exclude master
                if 0 <= event.midiChan <= 7:
                    # Control the 8 macro sliders
                    plugins.setParamValue(
                        event.controlVal / 100,
                        event.midiChan + 10, id_
                    )
            elif name == "Sakura":
                # Control the 8 resonator frequency sliders
                plugins.setParamValue(
                    event.controlVal / 100,
                    event.midiChan + 39, id_
                )
        # If an effects plugin is focused
        elif ui.getFocused(6):
            index = mixer.trackNumber()
            slot = (id_ - index * 4194304) // 65536
            if name in {"Fruity parametric EQ",
                        "Fruity parametric EQ 2",
                        "Fruity 7 Band Equalizer"}:
                # Only 7 sliders, so exclude 8 and master
                if 0 <= event.midiChan <= 6:
                    # Control the 7 equalizer handles
                    plugins.setParamValue(
                        event.controlVal / 100,
                        event.midiChan,
                        index, slot
                    )
