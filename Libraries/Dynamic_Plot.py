def dp(setup_config, flap_data):
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.widgets import Slider

    # The function to be called anytime a slider's value changes or to initialize the plot
    def update(val=0):
        ax.clear()
        lines = []
        for i in range(len(setup_config[0])):
            lines.append(
                ax.plot(flap_data[i][setup_config[val][i]][0], flap_data[i][setup_config[val][i]][1], lw=2,
                        color='k'))
        ax.set_xlabel('X - [m]')
        ax.set_xlabel('Y - [m]')
        ax.set_xticks(np.arange(-0.4, 3, 0.4))
        ax.set_yticks(np.arange(-0.4, 1, 0.4))
        ax.set_aspect('equal', adjustable='box')
        fig.canvas.draw_idle()

    # Create the figure and the line that we will manipulate

    fig, ax = plt.subplots()

    update()

    # adjust the main plot to make room for the sliders
    fig.subplots_adjust(left=0.25)

    # Make a vertically oriented slider to control the amplitude
    axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
    amp_slider = Slider(
        ax=axamp,
        label="Setup",
        valmin=0,
        valmax=len(setup_config) - 1,
        valinit=0,
        valstep=1,
        orientation="vertical"
    )

    # register the update function with each slider
    amp_slider.on_changed(update)

    plt.show()
