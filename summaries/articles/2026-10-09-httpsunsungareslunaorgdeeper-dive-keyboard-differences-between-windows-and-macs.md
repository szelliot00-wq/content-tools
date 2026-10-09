# Keyboard differences between Windows and Macs

Source: https://unsung.aresluna.org/deeper-dive-keyboard-differences-between-windows-and-macs/

## Summary
This article is a reference guide cataloging the key differences in keyboard behavior between Windows and macOS, aimed at developers building cross-platform web apps. It covers naming conventions, modifier key layouts, shortcut display styles, function key usage, text field shortcuts, and platform-reserved key combinations. The author draws on years of experience encountering these gotchas to compile them in one place.

## Key takeaways
- **Key naming differs**: Windows uses "Backspace/Delete/Enter" while Mac uses "Delete/Forward Delete/Return" — saying "Delete" without context is ambiguous.
- **Macs have one extra modifier key**: Mac offers Command, Option, Control, and Shift, giving more shortcut space than Windows's Ctrl, Alt, and Shift.
- **Shortcut display conventions differ**: Windows uses `Ctrl+Shift+G` style notation; Mac uses `⌃⇧G` (symbols, no plus sign).
- **Option key on Mac outputs extra characters** (e.g., ⌥Q = œ), which varies by locale — avoid ⌥-based shortcuts in text fields to prevent conflicts. Windows's equivalent is AltGr on non-US keyboards.
- **Function keys are used differently**: Windows apps traditionally claim F-keys as shortcuts; on Mac, F-keys were historically reserved for users, not apps.
- **Text field navigation shortcuts differ**: Mac supports Unix-style Control key shortcuts (e.g., Ctrl+A to go to line start); Windows uses Home/End for the same purpose.
- **Redo and refresh shortcuts differ**: Mac uses ⌘⇧Z for redo and ⌘R for refresh; Windows uses Ctrl+Y and F5 respectively.
- **Tab key behavior differs**: Windows tabs through all UI elements; Mac tabs only to keyboard-operable elements by default.
- **PgUp/PgDn and Home/End behave differently**: On Mac they scroll the view; on Windows they move the text cursor.
- **Avoid Ctrl+Alt shortcuts on Windows** (especially for non-US keyboards), just as you'd avoid ⌥-based shortcuts on Mac — both can conflict with language-specific character input.