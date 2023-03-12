# **DISTRAINS** - Whisky **DIST**illeries and their closest **TRAIN** Stop Distance

## Don't drink and drive! 
But why not taking the train to visit (all) whisky distilleries in Scotland?

This repository uses geodata of Scotlands train stops and
whisky distilleries to find the
**nearest** train stop to each distillery.
Second, the distilleries are ranked by lowest distance to the nearest train stop.
You can find the list of distilleries and the nearest train stop in `output/distilleries_result.csv`.

## Are you ready?

This analysis finds 136 distilleries, with an average walking distance of 19 km and
a minimum distance of **383 m** and a maximum distance of **123 km** 
between the distillery and the nearest train stop.
25% of the distilleries are reachable within 3 km.
If you want to visit all distilleries, you need to walk 2603 km: the equivalent of **62 marathons**.
The amount of whisky consumed assuming 3 x 35 ml per distillery is: **14.39 litres of whisky**.

Note: "Walking distance"

Enjoy!

![Distilleries](https://github.com/energyLS/distrains/blob/main/distilleries_rendered.pdf)

## Acknowledgements
- Fabian Neumann?
- Data providers?

## Download, Install, and Run

With `git` run:

```sh
git clone https://github.com/energyLS/distrains.git
```


With `pip` run:

```sh
pip install -r requirements.txt
```


Reproduce the results by running the Jupyter Notebook
`processing.ipynb`.
The map `distilleries_rendered.pdf` is not an output of the Jupyter Notebook but created using [QGIS](https://www.qgis.org/en/site/).
## Live App

You can find results as a dashboard here:

https://distrains.streamlit.app/