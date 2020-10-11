
def get_labels(labels_path):
    """
    Extract classes from label.txt
    
    :param labels_path: str, path to file with labels
    :return : list with labels
    """
    labelsfile = open(labels_path, 'r')
    labels = []
    line = labelsfile.readline()
    while line:
        labels.append(line.split(' ', 1)[1].rstrip())
        line = labelsfile.readline()
    labelsfile.close()
    return labels