from libqtile import bar, widget
from colors import *


widget_defaults = dict(
    font="Roboto",
    fontsize=12,
    padding=5,
)

mainBar = bar.Bar([
    widget.Clock(
        #background=colors[0],
        foreground=colors[1],
        format="   %d.%m.%Y"
    ),
    widget.Spacer(
        length=20
    ),
    widget.CPU(
        #background=colors[0],
        foreground=colors[1],
        format='   {load_percent}%',
        update_interval=30.0
    ),
    widget.Spacer(
        length=20
    ),
    widget.Memory(
        #background=colors[0],
        foreground=colors[1],
        format='   {MemPercent}%',
        update_interval=30.0
    ),
    widget.Spacer(
        length=20
    ), 
    widget.CurrentLayout(
        #background=colors[0],
        foreground=colors[1],
        fmt='{}',
        font="JetBrains Mono Bold",
        fontsize=13,
    ),
    widget.Spacer(
        length=20
    ),
    # widget.WindowName(
    #     background=colors[-1],
    #     foreground=colors[0],
    #     format="{name}",
    # ),
    widget.Spacer(
        length=bar.STRETCH
    ),

    # widget.TextBox(
    #     text="\ue0b6",
    #     font="Roboto Mono",
    #     foreground=colors[0],
    #     fontsize=17,
    #     padding=0
    # ),

    # widget.GroupBox(
    #     fontsize=14,
    #     borderwidth=0,
    #     #highlight_method='block',
    #     active='#CAA9E0',
    #     block_highlight_text_color="#91B1F0",
    #     highlight_color='#4B427E',
    #     inactive='#282738',
    #     foreground='#4B427E',
    #     background='#353446',
    #     this_current_screen_border='#353446',
    #     this_screen_border='#353446',
    #     other_current_screen_border='#353446',
    #     other_screen_border='#353446',
    #     urgent_border='#353446',
    #     rounded=True,
    #     disable_drag=True,
    # ),

    # widget.TextBox(
    #     text="\ue0b4",
    #     font="Roboto Mono",
    #     foreground=colors[0],
    #     fontsize=17,
    #     padding=0
    # ),

    # 
    widget.GroupBox(
        active='#CAA9E0',
        block_highlight_text_color="#91B1F0",
        highlight_color='#4B427E',
        inactive='#282738',
        #foreground=colors[1],

        this_current_screen_border='#353446',
        this_screen_border='#353446',
        
        other_current_screen_border='#353446',
        other_screen_border='#353446',
        urgent_border='#353446',

        spacing=6,
        fontsize=14,
        margin=3,
        borderwidth=1,
        
        highlight_method='block',
        rounded=True,
    ),

    widget.Spacer(
        length=bar.STRETCH
    ),
    widget.Systray(
      
    ),
    widget.Spacer(
        length=20
    ),
    widget.CheckUpdates(
        #background=colors[0],
        foreground=colors[1],
        distro='Arch_checkupdates',
        display_format='!    {updates}',
        no_update_string='',
        update_interval=1000,
    ),
    widget.Spacer(
        length=20
    ),
    widget.Volume(
        #background=colors[0],
        foreground=colors[1],
        emoji=True,
        emoji_list=['', '', '', ''],
        volume_app="pavucontrol",
    ),
    widget.Volume(
        #background=colors[0],
        foreground=colors[1],
        volume_app="pavucontrol",
    ),
    widget.Spacer(
        length=20
    ),
    widget.Battery(
        # background=colors[0],
        foreground=colors[1],
        charge_char='',
        full_char='',
        not_charging_char='',
        discharge_char='',
        unknown_char='',
        format="{char}     {percent: 2.0%}",
        max_chars=0
    ),
    widget.Spacer(
        length=20
    ),
    widget.Clock(
        #background=colors[0],
        foreground=colors[1],
        format="   %H:%M",
    )],
    24,

    background=colors[-1],
    margin=[4, 6, 2, 6],
    border_width=[0, 0, 0, 0],  # Draw top and bottom borders
    border_color=[colors[-1], colors[-1], colors[-1], colors[-1]]  # Borders are magenta
)





# secondBar = bar.Bar([
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Clock(
#         background=colors[0],
#         foreground=colors[1],
#         format="   %d.%m.%Y"
#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Spacer(
#         length=20
#     ),
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.CPU(
#         background=colors[0],
#         foreground=colors[1],
#         format='   {load_percent}%',
#         update_interval=30.0
#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Spacer(
#         length=20
#     ),
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Memory(
#         background=colors[0],
#         foreground=colors[1],
#         format='   {MemPercent}%',
#         update_interval=30.0
#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Spacer(
#         length=20
#     ),
#     widget.WindowName(
#         background=colors[-1],
#         foreground=colors[0],
#         format="{name}",
#     ),
#     widget.Spacer(
#         length=bar.STRETCH
#     ),
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.GroupBox(
#         background=colors[0],
#         foreground=colors[1],
#         spacing=6,
#         fontsize=14,
#         margin=3,
#         borderwidth=1,
#         inactive=colors[1],
#         active=colors[1],
#         this_current_screen_border='#6C7086',
#         highlight_method='block',
#         rounded=True,       
#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Spacer(
#         length=bar.STRETCH
#     ),
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.CheckUpdates(
#         background=colors[0],
#         foreground=colors[1],
#         distro='Arch_checkupdates',
#         display_format='!    {updates}',
#         no_update_string='',
#         update_interval=300,

#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Spacer(
#         length=20
#     ),
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Volume(
#         background=colors[0],
#         foreground=colors[1],
#         emoji=True,
#         emoji_list=['', '', '', ''],
#         volume_app="pavucontrol",
#     ),
#     widget.Volume(
#         background=colors[0],
#         foreground=colors[1],
#         volume_app="pavucontrol",
#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Spacer(
#         length=20
#     ),
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Battery(
#         background=colors[0],
#         foreground=colors[1],
#         charge_char='',
#         full_char='',
#         not_charging_char='',
#         discharge_char='',
#         unknown_char='',
#         format="{char}     {percent: 2.0%}",
#         max_chars=0
#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     ),
#     widget.Spacer(
#         length=20
#     ),
#     widget.TextBox(
#         text="\ue0b6",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0,
#     ),
#     widget.Clock(
#         background=colors[0],
#         foreground=colors[1],
#         format="   %H:%M",
#     ),
#     widget.TextBox(
#         text="\ue0b4",
#         font="Roboto Mono",
#         foreground=colors[0],
#         fontsize=17,
#         padding=0
#     )],
#     24,
#     background=colors[-1],
#     margin=[4, 6, 2, 6],
#     border_width=[0, 0, 0, 0],  # Draw top and bottom borders
#     border_color=[colors[-1], colors[-1], colors[-1], colors[-1]]  # Borders are magenta
# )
