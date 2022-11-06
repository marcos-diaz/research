import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import norm

STRIDE = 3

def pdf(x):
    sigma = 0.3
    scale = 0.75
    return norm.pdf(x, 0, sigma) * scale

def w(x):
    return x * pdf(x)

def plot_noise(savepath, show=False):
    resolution = 0.01
    x = np.arange(0, np.pi*4, resolution)
    y = []
    real =  np.sin(x) / 2
    for i in range(4):
        np.random.seed(i)
        value = np.random.normal(0, 0.5, len(x)) + real
        y.append(value)
    def multisample(sensors, samples_per_sensor):
        base = np.zeros(len(x))
        for i in range(sensors):
            for j in range(samples_per_sensor):
                signal = np.append(np.zeros(j), y[i])[0:len(x)]
                base += signal
        return base / (samples_per_sensor * sensors)
    fig = []
    ax = []
    for i in range(5):
        fig_, ax_ = plot.subplots()
        fig.append(fig_)
        ax.append(ax_)
    # plot.title(f'Data: NumPy simulation "plot.py#plot_noise()"', fontsize=8)
    ax[0].plot(x, y[0],              color='grey', label='S=1 L=1')
    ax[1].plot(x, multisample(1, 4), color='grey', label='S=1 L=4')
    ax[2].plot(x, multisample(2, 2), color='grey', label='S=2 L=2')
    ax[3].plot(x, multisample(2, 4), color='grey', label='S=2 L=4')
    ax[4].plot(x, multisample(3, 4), color='grey', label='S=3 L=4')
    for i in range(5):
        ax[i].set_xlabel('Time')
    for i in range(5):
        ax[i].plot(x, real, color='black')
    for i in range(5):
        ax[i].set_ylabel('Output')
    for i in range(5):
        ax[i].set_ylim(-1, 1)
    for i in range(5):
        ax[i].set_xticks([])
    for i in range(5):
        ax[i].figure.set_size_inches(5, 1)
    # for i in range(5):
    #     ax[i].legend(loc='upper right')
    if show:
        plot.show()
        return
    for i in range(5):
        fig[i].savefig(f'{savepath}_{i+1}.png', bbox_inches='tight')

def plot_drift_1a(savepath, show=False):
    resolution = 0.01
    x = np.arange(-1, 1, resolution)
    y1 = x
    y2 = pdf(x)
    y3 = y1 * y2
    fig, ax = plot.subplots()
    # plot.title(f'Data: NumPy integration with {resolution} resolution', fontsize=8)
    ax.plot(x, y1, color='black', label='f1(x): For any value of drift', linestyle='dotted')
    ax.plot(x, y2, color='black', label='f2(x): Probability Density Function' )
    ax.plot(x, y3, color='grey', label='f3(x): Probability-weighted drift ')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('Drift')
    ax.grid()
    ax.legend()
    if show:
        plot.show()
        return
    fig.savefig(savepath, bbox_inches='tight')

def plot_drift_1b(savepath, show=False):
    resolution = 0.01
    x = np.arange(-1, 1, resolution)
    y1 = x
    y2 = pdf(x)
    w = y1 * y2
    wi = np.average(abs(w), axis=0)
    print(wi)
    wim = np.repeat(wi, len(x))
    fig, ax = plot.subplots()
    # plot.title(f'Data: NumPy integration with {resolution} resolution', fontsize=8)
    ax.plot(x, abs(w), color='black', label='f(x): Abs probability-weighted drift')
    ax.plot(x, wim, color='black', label='Mean', linestyle='dotted')
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 0.2)
    ax.set_xlabel('Drift')
    ax.set_ylabel('Probability-weighted drift')
    ax.grid()
    ax.legend()
    if show:
        plot.show()
        return
    fig.savefig(savepath, bbox_inches='tight')

def plot_drift_2(savepath, show=False):
    resolution = 0.01
    x = np.arange(-1, 1, resolution)
    w1 = x * pdf(x)
    w2 = w1
    w1m, w2m = np.meshgrid(w1, w2)
    q = (w1m + w2m) / 2
    qi = np.average(q, axis=0)
    qii = np.average(abs(qi), axis=0)
    print(qii)
    qiim = np.repeat(qii, len(x))
    fig, ax = plot.subplots()
    # plot.title(f'Data: NumPy integration with {resolution} resolution', fontsize=8)
    ax.plot(x, abs(qi), color='black', label='f(x): Abs probability-weighted drift with 2 sensors')
    ax.plot(x, qiim, color='black', label='Mean', linestyle='dotted')
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 0.2)
    ax.set_xlabel('Drift')
    ax.set_ylabel('Probability-weighted drift')
    ax.grid()
    ax.legend()
    if show:
        plot.show()
        return
    fig.savefig(savepath, bbox_inches='tight')

def plot_drift_3(savepath, show=False):
    resolution = 0.02
    gx = np.arange(-1, 1, resolution)
    gy = gx
    gxm, gym = np.meshgrid(gx, gy)
    x1 = w(gx)
    # x2 = w(gx)
    y1 = w(gy)
    # y2 = w(gy)
    x1m, y1m = np.meshgrid(x1, y1)
    # y1m, y2m = np.meshgrid(y1, y2)
    # x = (x1m + x2m) / 2
    # y = (y1m + y2m) / 2
    # xi = np.average(x, axis=0)
    # yi = np.average(y, axis=0)
    # xm, ym = np.meshgrid(xi, yi)
    z = np.sqrt(x1m**2 + y1m**2)
    zi = np.average(z, axis=0)
    zii = np.average(zi, axis=0)
    print(zii)
    # zii = np.average(zi, axis=0)
    # qiim = np.repeat(qii, len(x))
    fig = plot.figure()
    ax = plot.axes(projection='3d')
    # plot.title(f'Data: NumPy integration with {resolution} resolution', fontsize=8)
    ax.plot_wireframe(
        gxm, gym, z,
        color="grey",
        rstride=STRIDE,
        cstride=STRIDE,
        label='f(x): Probability-weighted\ndrift on 2 axis'
    )
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('Drift X')
    ax.set_ylabel('Drift Y')
    ax.set_zlabel('Probability-weighted drift')
    ax.set_xticks(np.arange(-1, 1.1, 0.5))
    ax.set_yticks(np.arange(-1, 1.1, 0.5))
    # ax.legend()
    if show:
        plot.show()
        return
    fig.savefig(savepath, bbox_inches='tight', pad_inches=0.25)

def plot_drift_4(savepath, show=False):
    resolution = 0.02
    gx = np.arange(-1, 1, resolution)
    gy = gx
    gxm, gym = np.meshgrid(gx, gy)
    x1 = w(gx)
    x2 = w(gx)
    y1 = w(gy)
    y2 = w(gy)
    x1m, x2m, y1m, y2m = np.meshgrid(x1, x2, y1, y2, copy=False)
    z = np.sqrt(
        ( (x1m + x2m) / 2 ) ** 2 +
        ( (y1m + y2m) / 2 ) ** 2
    )
    zi = np.average(z, axis=0)
    zii = np.average(zi, axis=0)
    ziii = np.average(zii, axis=0)
    ziiii = np.average(ziii, axis=0)
    print(ziiii)
    fig = plot.figure()
    ax = plot.axes(projection='3d')
    # plot.title(f'Data: NumPy integration with {resolution} resolution', fontsize=8)
    ax.plot_wireframe(
        gxm, gym, zii,
        color="grey",
        rstride=STRIDE,
        cstride=STRIDE,
        label='f(x): Probability-weighted drift\non 2 axis and 2 sensors'
    )
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('Drift X')
    ax.set_ylabel('Drift Y')
    ax.set_zlabel('Probability-weighted drift')
    ax.set_xticks(np.arange(-1, 1.1, 0.5))
    ax.set_yticks(np.arange(-1, 1.1, 0.5))
    # ax.legend()
    if show:
        plot.show()
        return
    fig.savefig(savepath, bbox_inches='tight', pad_inches=0.25)

def plot_scale(savepath, show=False):
    resolution = 0.1
    x = np.arange(0, np.pi*16, resolution)
    y = []
    real =  np.sin(x) * x * 5
    def noise(seed):
        np.random.seed(seed)
        return np.random.normal(0, 8*2.5, len(x))
    a = real + noise(7)
    b = real + (noise(14) / 2)
    half = int(len(x) / 2)
    z = np.append( b[0:half], a[half:] )
    fig = []
    ax = []
    for i in range(4):
        fig_, ax_ = plot.subplots()
        fig.append(fig_)
        ax.append(ax_)
    ax[0].plot(x, real, color='grey', label='Real input')
    ax[1].plot(x, a,    color='grey', label='Sensor A, scale=250')
    ax[2].plot(x, b,    color='grey', label='Sensor B, scale=125')
    ax[3].plot(x, z,    color='grey', label='Dynamic switch between A & B')
    ax[0].set_ylim(-250, 250)
    ax[1].set_ylim(-250, 250)
    ax[2].set_ylim(-125, 125)
    ax[3].set_ylim(-250, 250)
    for i in range(4):
        ax[i].set_xlabel('Time')
    for i in range(4):
        ax[i].set_ylabel('Output (DPS)')
    for i in range(4):
        ax[i].set_xticks([])
    for i in range(4):
        ax[i].figure.set_size_inches(5, 1)
    # for i in range(4):
    #     ax[i].legend(loc='upper left')
    if show:
        plot.show()
        return
    for i in range(4):
        fig[i].savefig(f'{savepath}_{i+1}.png', bbox_inches='tight')


plot_noise('multiple_ars/figure_noise')
plot_drift_1a('multiple_ars/figure_drift_1a.png')
plot_drift_1b('multiple_ars/figure_drift_1b.png')
plot_drift_2('multiple_ars/figure_drift_2.png')
plot_drift_3('multiple_ars/figure_drift_3.png')
plot_drift_4('multiple_ars/figure_drift_4.png')
plot_scale('multiple_ars/figure_scale')
