# Safe Navigation Robotics Project

This project aims to create an algorithm to allow safe, autonomous
navigation for a single robot in an unknown environment.

## Running the simulator
Before running the simulator, make sure install every packages needed for this project. Otherwise you will get a list of errors.

Pedestrian ID are indexed from 1 instead of 0. First, you need to specify some other pedestrian on the command line. For example, run:

```
python3 Main.py --ped-id-to-replace 3
```

Question: Why the simulator is looking for a specific pedestrian?

Answer: The specific pedestrian will replace with a robot and then run a navigation algorithm(e.g. DeepMotion and SFM)

To run the simulator, first `cd` into the directory you cloned this
repository to, then run:

```
./run_once.sh
```

The above command will generate a lot of frames so that you can visually know how robot naviation works. To start the SVG viewer, you can run:

```
eog *.svg
```

There are many settings that can be configured from the command line. To
see which flags are available, just run:

```
python3 Main.py --help
```

### Unit tests

There are some (but not many) unit tests available in the `testcode` module. These can be run with `python3 -m testcode.<test-file-name>`. For example, to run the geometry unit tests in `testcode/geometry_test.py`, you would use:
```
python3 -m testcode.geometry_test
```

### DeepMotion Training

To train the neural network(s) for the DeepMotion navigation algorithm (`DeepPredNavAlgo` class), go into the `human_action` directory and run `python3 train_C.py action data/training_human_data.json`. The networks will be saved in the `dnns` folder. The `DeepPredNavAlgo` class takes a `net_load_file` parameter that specifies the file to load the network from.

## Contributing

Use tabs, never spaces. Spaces break the Cython compilation. Also, use Unix line endings.



