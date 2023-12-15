"""Smiley.py: contains Smiley component."""

from importlib import resources as importlib_resources

import pandas as pd
import pycif as pc

from pc_smiley import resources

facial_data = pd.read_csv(
    importlib_resources.files(resources) / 'facial_data.csv'
    ).loc[0, :]


class Smiley(pc.Component):
    """A smiley face component"""

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

