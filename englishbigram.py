# Here we use the mapreduce design to create a bigram frequency table based on the
# english training text.
from mapper import createbigrams
from reducer import mergebigrams