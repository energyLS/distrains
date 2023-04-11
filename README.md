# **DISTRAINS** - Whisky **DIST**illeries and the distance to their closest **TRAIN** Stops

## Don't drink and drive! 
But, why not travel by train to see (every) whisky distillery in Scotland?

To determine the **nearest** railway station to each distillery, this repository uses geodata of Scotland's train stops and whisky distilleries.
Second, the distilleries are ranked based on their proximity to the closest train station.
The list of distilleries and their closest train station may be found in the files `output/distilleries_result.csv` and georeferenced in `output/distilleries_result.geojson`, respectively.

## Are you ready?

This analysis lists **136 distilleries**, with an average walking distance of **19 km** and
a minimum distance of **383 m** and a maximum distance of **123 km** 
between the distillery and the nearest train stop.
25% of the distilleries are reachable within 3 km.
If you want to visit all distilleries, you need to walk 2603 km: the equivalent of **62 marathons**.
The amount of whisky consumed assuming 3 x 35 ml per distillery is: **14.39 litres of whisky**.

Note: The distance listed here is the airline distance.

Enjoy!

![Distilleries](https://raw.githubusercontent.com/energyLS/distrains/main/plots/distilleries.png?token=GHSAT0AAAAAABYA4O645ELOTLC2J4UH7DESZA6DYNQ)
 

## Download, Install, and Run

With `git` run:

```sh
git clone https://github.com/energyLS/distrains.git
```


With `conda` run:

```sh
conda env create -f environment.yaml
```

Reproduce the results by running the Jupyter Notebook
`processing.ipynb`.
The map `plots/distilleries.pdf` is not an output of the Jupyter Notebook but created using [QGIS](https://www.qgis.org/en/site/).
## Live App

You can find results as a dashboard here:

https://distrains.streamlit.app/

## Licence
The raw data is licensed as specified in the distillery dataset [completely-smashed](https://github.com/mhamilt/completely-smashed/) and the train station dataset [uk-railway-stations](https://github.com/davwheat/uk-railway-stations).
The code in this repository is licensed under the MIT License, details can be found in the file `LICENCE`.

## Acknowledgements
Thanks to:
- [mhamlit](https://github.com/mhamilt) for the distillery dataset [completely-smashed](https://github.com/mhamilt/completely-smashed/),
- [davwheat](https://github.com/davwheat) for the train station dataset [uk-railway-stations](https://github.com/davwheat/uk-railway-stations),
- [fneum](https://github.com/fneum) for his [streamlit-tutorial](https://github.com/fneum/streamlit-tutorial) and
- CM for her advice and support creating the rendered map `distilleries.pdf`,
- The Icon "simple pot still" by Kristel Cornell from [The Noun Project](https://thenounproject.com/browse/icons/term/simple-pot-still/), CC BY 3.0.
