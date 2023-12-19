"""Smiley.py: contains Smiley component."""

# We will use `importlib.resources` to read in the data from
# `resources/facial_data.csv`.
from importlib import resources as importlib_resources

# We will use pandas to read `facial_data.csv`.
# Admittedly, this is extremely overkill.
# Python's built-in `csv` package or even standard string
# parsing operations would be a better tool for this job.
# But here we use pandas so that I have a chance to demonstrate
# how to declare external dependencies in `pyproject.toml`.
import pandas as pd
import pycif as pc

# Here we import the local `resources` module
from pc_smiley import resources

# And this is how we read in the facial_data.csv file.
# The last .loc[0, :] line is there just to convert
# the Dataframe into a Series (since there's only one row)
facial_data = pd.read_csv(
    importlib_resources.files(resources) / 'facial_data.csv'
    ).loc[0, :]


class Smiley(pc.Component):
    """
    Smiley
    A smiley face component
    """

    class Layers(pc.Component.Layers):
        face = pc.Layer(
            "The face layer"
            )
        eyes = pc.Layer(
            "The eyes layer"
            )
        mouth = pc.Layer(
            "The mouth layer"
            )

    class Options(pc.Component.Options):
        happiness = pc.Option.Functional(
            5,
            "Happiness, from -10 to 10"
            )
        eye_size = pc.Option.Geometric(
            5,
            "Eye radius"
            )

    class Marks(pc.Component.Marks):
        left_eye = pc.Mark("Left eye center")
        right_eye = pc.Mark("Right eye center")

    def _make(self):
        face = pc.Circle(50)
        eye_l = pc.Circle(self.options.eye_size)
        eye_r = eye_l.copy()

        smile = pc.Arc(
            angle_start=pc.degrees(-90 - abs(self.options.happiness) * 4),
            angle_end=pc.degrees(-90 + abs(self.options.happiness) * 4),
            radius_inner=40,
            radius_outter=45
            )

        if self.options.happiness < 0:
            smile.bbox.mid.hflip()

        eye_l.marks.center.to(
            face.bbox.interpolate(
                facial_data.interocular_distance,
                0.7
                )
            )

        eye_r.marks.center.to(
            face.bbox.interpolate(
                1 - facial_data.interocular_distance,
                0.7)
            )

        smile.bbox.mid.to(
            face.bbox.interpolate(0.5, facial_data.mouth_offset)
            )

        self.add_subpolygon(face, self.layers.face)
        self.add_subpolygon(eye_l, self.layers.eyes)
        self.add_subpolygon(eye_r, self.layers.eyes)
        self.add_subpolygon(smile, self.layers.mouth)

        self.marks.left_eye = eye_l.marks.center
        self.marks.right_eye = eye_r.marks.center

