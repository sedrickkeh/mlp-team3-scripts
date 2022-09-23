import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score

def plot_prk_curve(logits, labels, interval=0.1, save_name='prk_curve.png', plot_title='PR-k curve'):
    assert(len(logits)==len(labels))
    y_vals = sorted([(i,j) for i,j in zip(logits, labels)])
    y_vals.reverse()
    labels_sorted = [i[1] for i in y_vals]

    scores = []
    num_bins = int(1 / interval)
    for i in range(num_bins):
        idx = int(i*interval*len(labels))
        preds = [0 if j>=idx else 1 for j in range(len(y_vals))]
        precision = precision_score(labels_sorted, preds, pos_label=1, average='binary')
        recall = recall_score(labels_sorted, preds, pos_label=1, average='binary')
        scores.append((i*interval,precision,recall))
    
    # add 1.0 to right end of curve
    preds = [1 for j in range(len(y_vals))]
    precision = precision_score(labels_sorted, preds, pos_label=1, average='binary')
    recall = recall_score(labels_sorted, preds, pos_label=1, average='binary')
    scores.append((1.0,precision,recall))
    print("Precision-recall scores:", scores)

    # plot
    fracs = [i[0] for i in scores]
    precisions = [i[1] for i in scores]
    precisions[0] = 1          # not sure if this makes sense, but it looks weird otherwise
    recalls = [i[2] for i in scores]
    plt.plot(fracs, precisions, label="precision")
    plt.plot(fracs, recalls, label="recall", color='red')
    plt.xticks(fracs)
    plt.xlabel("Percent of population")
    plt.title(plot_title)
    plt.legend()
    plt.savefig(save_name)

### Sample code to plot PR-k curve
# import numpy as np
# import random
# aa = np.random.uniform(size=100)
# bb = [random.choice([0,1]) for _ in range(100)]
# plot_prk_curve(aa, bb)