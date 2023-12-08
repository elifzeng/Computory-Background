create a scatter plot with margninal histograms
ref:  
https://seaborn.pydata.org/generated/seaborn.jointplot.html    
![image](https://github.com/elifzeng/Computory-Background/assets/52747634/755bc279-1188-4d7f-af39-c9e581ac789e)

```python
import seaborn as sns
df = sns.load_dataset("penguins")
# single data frame
g=sns.jointplot(data = df,
              x = "bill_length_mm",
              y = "bill_depth_mm",
            #   marker = "x",
              alpha = 0.5,
              s = 1.5,
              hue = "species"
            #   color = "dimgray",
            #   marginal_kws = dict(edgecolor="white"),
            #   kind = "hex",
              )
g.plot_marginals(sns.histplot, edgecolor="white")
```
