import matplotlib.pyplot as plt
import json

with open('litocodes.json', 'r') as f:
    jsoncodigos = json.load(f)

with open('litopatterns.json', 'r') as f:
    jsonpadroes = json.load(f)

classes = [4, 6, 7, 8, 42, 44, 49, 54, 56, 57, 58, 66, 82]
fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(9, 4), dpi=200)
fig.subplots_adjust(top=0.99, bottom=0.01, left=0.01, right=0.99, wspace=0.0)

for k, cls in enumerate(classes):
    
    abreviacao = jsoncodigos['codigo']["{:0>3}".format(cls)]['abreviacao']
    nome = jsoncodigos['codigo']["{:0>3}".format(cls)]['nome'].lower()
    color = [float(a)/255.0 for a in jsonpadroes[nome]['color']]
    hatch = jsonpadroes[nome]['hatch']
    
    i = k % 5
    j = k // 5
    
    ax = axes[i][j]
    
    ax.fill([0.75, 0.75, 1, 1], [0.0, 1.0, 1.0, 0.0], color=color)
    ax.fill([0.75, 0.75, 1, 1], [0.0, 1.0, 1.0, 0.0], fill=False, hatch=hatch)
    ax.text(0.725, 0.5, '{} - {} - {}'.format(nome, abreviacao, cls), va='center', ha='right', fontsize=12)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

for axs in axes:
    for ax in axs:
        ax.set_axis_off()

plt.savefig('legendafacies.png', dpi=200)