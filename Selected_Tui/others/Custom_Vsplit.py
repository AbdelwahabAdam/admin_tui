
class Vertical_listbox (VSplit):
    def __init__(self,
                 children: Sequence[AnyContainer],
                 window_too_small: Optional[Container] = None,
                 align: HorizontalAlign = ...,
                 padding: AnyDimension = 0,
                 padding_char: Optional[str] = None,
                 padding_style: str = "",
                 width: AnyDimension = None,
                 height: AnyDimension = None,
                 z_index: Optional[int] = None,
                 modal: bool = False,
                 key_bindings: Optional[KeyBindingsBase] = None,
                 style: Union[str, Callable[[], str]] = ""
                 ) -> None:
        super().__init__(children, window_too_small, align, padding, padding_char,
                         padding_style, width, height, z_index, modal, key_bindings, style)

    def write_to_screen(
        self,
        screen: Screen,
        mouse_handlers: MouseHandlers,
        write_position: WritePosition,
        parent_style: str,
        erase_bg: bool,
        z_index: Optional[int],
    ) -> None:
        """
        Render the prompt to a `Screen` instance.

        :param screen: The :class:`~prompt_toolkit.layout.screen.Screen` class
            to which the output has to be written.
        """
        if not self.children:
            return

        children = self._all_children
        sizes = self._divide_widths(write_position.width)
        style = parent_style + " " + to_str(self.style)
        z_index = z_index if self.z_index is None else self.z_index

        # If there is not enough space.
        if sizes is None:
            self.window_too_small.write_to_screen(
                screen, mouse_handlers, write_position, style, erase_bg, z_index
            )
            return

        # Calculate heights, take the largest possible, but not larger than
        # write_position.height.
        heights = [
            child.preferred_height(width, write_position.height).preferred
            for width, child in zip(sizes, children)
        ]
        height = max(write_position.height, min(
            write_position.height, max(heights)))

        #
        ypos = write_position.ypos
        xpos = write_position.xpos

        # Draw all child panes.
        for s, c in zip(sizes, children):
            c.write_to_screen(
                screen,
                mouse_handlers,
                WritePosition(xpos, ypos, s, height),
                style,
                erase_bg,
                z_index,
            )
            xpos += s

        # Fill in the remaining space. This happens when a child control
        # refuses to take more space and we don't have any padding. Adding a
        # dummy child control for this (in `self._all_children`) is not
        # desired, because in some situations, it would take more space, even
        # when it's not required. This is required to apply the styling.
        remaining_width = write_position.xpos + write_position.width - xpos
        if remaining_width > 0:
            self._remaining_space_window.write_to_screen(
                screen,
                mouse_handlers,
                WritePosition(xpos, ypos, remaining_width, height),
                style,
                erase_bg,
                z_index,
            )

