import tkinter as tk


class NumericEntry(tk.Entry):
    """Number validating subclass of tk.Entry."""

    def __init__(self, parent, minval=0, maxval=1, maxchars=1, *args, **kwargs):
        """NumericEntry class constructor.
        :type minval: integer
        :type maxval: integer
        :type maxchars: integer
        """
        super().__init__(parent, *args, **kwargs)
        self.configure(
            validate='all',
            validatecommand=(self.register(self._validate), '%S', '%i', '%V',
                             '%d'),
            invalidcommand=(self.register(self._on_invalid), '%V')
        )
        self.min_value = minval
        self.max_value = maxval
        self.max_chars = maxchars
        self.has_error = True  # To guard against empty entries.

    def _toggle_error(self, error=''):
        """Turns on/off error state."""
        self.configure(foreground='red' if error else 'black')

    def _validate(self, char, index, event, action):
        """Validation function."""
        # Reset error state.
        self._toggle_error()
        self.has_error = False
        valid = True

        # Check keystrokes.
        if event == 'key':
            if action == '0':
                valid = True
            else:
                if char.isdigit():
                    valid = True
                else:
                    valid = False
                if int(index) + 1 > self.max_chars:
                    valid = False
        elif event == 'focusout':
            if str(self.get()):  # No empty entry box.
                value = int(self.get())
                if value < self.min_value:
                    valid = False
                if value > self.max_value:
                    valid = False
            else:  # Empty entry box.
                valid = False
        return valid

    def _on_invalid(self, event):
        """Invalid function."""
        if event != 'key':
            self._toggle_error('error')
            self.has_error = True
