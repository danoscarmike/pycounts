import matplotlib.pyplot as plt


def plot_words(word_counts, n=10):
   word, count = zip(*word_counts.most_common(n))
   fig = plt.bar(range(n), count)
   plt.xticks(range(n), labels=word, rotation=45)
   plt.xlabel("Words")
   plt.ylabel("Count") 
   return fig