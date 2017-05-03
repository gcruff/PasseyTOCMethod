import matplotlib.pyplot as plt
import json

with open('litocodes.json', 'r') as f:
    jsoncodigos = json.load(f)

with open('litopatterns.json', 'r') as f:
    jsonpadroes = json.load(f)

# classes = [4, 6, 7, 8, 42, 44, 49, 54, 56, 57, 58, 66, 82]
classes = [4, 6, 8, 30, 42, 49, 54, 57, 58, 66, 82]
nrows = 2
ncols = 6
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(11, 1), dpi=200)
fig.subplots_adjust(top=0.99, bottom=0.01, left=0.005, right=0.995, wspace=0.0)

for k, cls in enumerate(sorted(classes, key=lambda x: jsoncodigos['codigo']["{:0>3}".format(x)]['nome'].lower())):
    
    nome = jsoncodigos['codigo']["{:0>3}".format(cls)]['nome'].lower()
    color = [float(a)/255.0 for a in jsonpadroes[nome]['color']]
    hatch = jsonpadroes[nome]['hatch']
    
    col = k // ncols
    line = k % ncols
    
    ax = axes[col][line]
    
    ax.fill([0.75, 0.75, 1, 1], [0.0, 1.0, 1.0, 0.0], color=color)
    ax.fill([0.75, 0.75, 1, 1], [0.0, 1.0, 1.0, 0.0], fill=False, hatch=hatch)
    ax.text(0.725, 0.5, nome, va='center', ha='right', fontsize=12)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

for axs in axes:
    for ax in axs:
        ax.set_axis_off()

plt.savefig('legendafacies.png', dpi=200)