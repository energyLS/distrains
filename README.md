# **DISTRAINS** - Whisky **DIST**illeries and the distance to their closest **TRAIN** Stop

## Don't drink and drive! 
But why not taking the train to visit (all) whisky distilleries in Scotland?

This repository uses geodata of Scotlands train stops and
whisky distilleries to find the
**nearest** train stop to each distillery.
Second, the distilleries are ranked by lowest distance to the nearest train stop.
You can find the list of distilleries and the nearest train stop in `output/distilleries_result.csv` or 
georeferenced in `output/distilleries_result.geojson`.

## Are you ready?

This analysis lists **136 distilleries**, with an average walking distance of **19 km** and
a minimum distance of **383 m** and a maximum distance of **123 km** 
between the distillery and the nearest train stop.
25% of the distilleries are reachable within 3 km.
If you want to visit all distilleries, you need to walk 2603 km: the equivalent of **62 marathons**.
The amount of whisky consumed assuming 3 x 35 ml per distillery is: **14.39 litres of whisky**.

Note: The distance listed here is the airline distance.

Enjoy!

![Distilleries](distilleries.svg)

## Acknowledgements
Thanks to:
- [@mhamlit](https://github.com/mhamilt) for the distillery dataset [completely-smashed](https://github.com/mhamilt/completely-smashed/)
- [@davwheat](https://github.com/davwheat) for the train station dataset [uk-railway-stations](https://github.com/davwheat/uk-railway-stations)
- [fneum](https://github.com/fneum) for his [streamlit-tutorial](https://github.com/fneum/streamlit-tutorial) and
- CM for her advice and support creating the rendered map `distilleries_rendered.pdf`.  

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